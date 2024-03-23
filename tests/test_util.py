import dataclasses
from typing import List, Union

import pytest
from docutils import nodes

from sphinx_design_elements.util.directive import MarkdownWrapper, SmartReference, link_to_markdown


@dataclasses.dataclass
class TestItem:
    input: str
    output: Union[bool, str]

    @staticmethod
    def ids(data) -> List[str]:
        return [item.input for item in data]


url_tests = [
    TestItem(input="https://example.org/", output=True),
    TestItem(input="foobar://example.org/", output=False),
]


intersphinx_tests = [
    # That's an intersphinx reference.
    TestItem(input="foo:bar", output=True),
    # Not an intersphinx reference at all.
    TestItem(input="foo/bar", output=False),
    # Too many components.
    TestItem(input="foo:bar:baz", output=False),
    # MyST references are not (traditional) intersphinx references.
    TestItem(input="#foobar", output=False),
    TestItem(input="inv:project#remote-label", output=False),
]


indirect_tests = [
    TestItem(input="[indirect-label]", output=True),
    TestItem(input="unknown-label", output=False),
    TestItem(input="#local-label", output=False),
]


myst_tests = [
    # Project-local references.
    TestItem(input="#local-label", output=True),
    # Specific references.
    TestItem(input="inv:project#remote-label", output=True),
    TestItem(input="path:/to/file.txt", output=True),
    TestItem(input="project:acme42", output=True),
    # Others.
    TestItem(input="[indirect-label]", output=False),
    TestItem(input="unknown-label", output=False),
]


translate_references = [
    # Translate project-local and intersphinx references.
    TestItem(input="document", output="#document"),
    TestItem(input="guide:document", output="inv:guide#document"),
    # Pass-through all others verbatim.
    TestItem(input="#local-label", output="#local-label"),
    TestItem(input="https://example.org", output="https://example.org"),
    TestItem(input="inv:guide#document", output="inv:guide#document"),
    TestItem(input="[document]", output="[document]"),
]


translate_links = [
    # Translate project-local and intersphinx references.
    TestItem(input="document", output="[](#document)"),
    TestItem(input="guide:document", output="[](inv:guide#document)"),
    # Pass-through all others verbatim.
    TestItem(input="#local-label", output="[](#local-label)"),
    TestItem(input="https://example.org", output="[](https://example.org)"),
    TestItem(input="inv:guide#document", output="[](inv:guide#document)"),
    TestItem(input="[document]", output="[][document]"),
]


@pytest.mark.parametrize("item", url_tests, ids=TestItem.ids(url_tests))
def test_reference_url(item: TestItem):
    assert SmartReference(item.input).is_url() == item.output


@pytest.mark.parametrize("item", intersphinx_tests, ids=TestItem.ids(intersphinx_tests))
def test_reference_intersphinx(item: TestItem):
    assert SmartReference(item.input).is_traditional_intersphinx_reference() == item.output


@pytest.mark.parametrize("item", indirect_tests, ids=TestItem.ids(indirect_tests))
def test_reference_indirect(item: TestItem):
    assert SmartReference(item.input).is_indirect_reference() == item.output


@pytest.mark.parametrize("item", myst_tests, ids=TestItem.ids(myst_tests))
def test_reference_myst(item: TestItem):
    assert SmartReference(item.input).is_myst_reference() == item.output


@pytest.mark.parametrize("item", translate_references, ids=TestItem.ids(translate_references))
def test_reference_to_myst(item: TestItem):
    assert SmartReference(item.input).reference_to_myst() == item.output


@pytest.mark.parametrize("item", translate_links, ids=TestItem.ids(translate_links))
def test_link_to_markdown(item: TestItem):
    assert link_to_markdown(item.input) == item.output


def test_link_to_markdown_all_options():
    assert link_to_markdown(ref="document", label="label", title="title") == '[label](#document "title")'


def test_markdown_wrapper():
    mw = MarkdownWrapper()
    outcome = mw.render('[label](#document "title")')[0].next_node(nodes.reference)
    assert str(outcome) == '<reference id_link="True" reftitle="title" refuri="#document">label</reference>'
