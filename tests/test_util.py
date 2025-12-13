import dataclasses
from typing import List, Union

import pytest
from docutils import nodes

from sphinx_design_elements.util.directive import MarkdownWrapper, SmartReference, link_to_markdown
from tests.util import patch_snippet_docutils_forward


@dataclasses.dataclass
class ReferenceItem:
    input: str
    output: Union[bool, str]

    @staticmethod
    def ids(data) -> List[str]:
        return [item.input for item in data]


url_tests = [
    ReferenceItem(input="https://example.org/", output=True),
    ReferenceItem(input="foobar://example.org/", output=False),
]


intersphinx_tests = [
    # That's an intersphinx reference.
    ReferenceItem(input="foo:bar", output=True),
    # Not an intersphinx reference at all.
    ReferenceItem(input="foo/bar", output=False),
    # Too many components.
    ReferenceItem(input="foo:bar:baz", output=False),
    # MyST references are not (traditional) intersphinx references.
    ReferenceItem(input="#foobar", output=False),
    ReferenceItem(input="inv:project#remote-label", output=False),
]


indirect_tests = [
    ReferenceItem(input="[indirect-label]", output=True),
    ReferenceItem(input="unknown-label", output=False),
    ReferenceItem(input="#local-label", output=False),
]


myst_tests = [
    # Project-local references.
    ReferenceItem(input="#local-label", output=True),
    # Specific references.
    ReferenceItem(input="inv:project#remote-label", output=True),
    ReferenceItem(input="path:/to/file.txt", output=True),
    ReferenceItem(input="project:acme42", output=True),
    # Others.
    ReferenceItem(input="[indirect-label]", output=False),
    ReferenceItem(input="unknown-label", output=False),
]


translate_references = [
    # Translate project-local and intersphinx references.
    ReferenceItem(input="document", output="#document"),
    ReferenceItem(input="guide:document", output="inv:guide#document"),
    # Pass-through all others verbatim.
    ReferenceItem(input="#local-label", output="#local-label"),
    ReferenceItem(input="https://example.org", output="https://example.org"),
    ReferenceItem(input="inv:guide#document", output="inv:guide#document"),
    ReferenceItem(input="[document]", output="[document]"),
]


translate_links = [
    # Translate project-local and intersphinx references.
    ReferenceItem(input="document", output="[](#document)"),
    ReferenceItem(input="guide:document", output="[](inv:guide#document)"),
    # Pass-through all others verbatim.
    ReferenceItem(input="#local-label", output="[](#local-label)"),
    ReferenceItem(input="https://example.org", output="[](https://example.org)"),
    ReferenceItem(input="inv:guide#document", output="[](inv:guide#document)"),
    ReferenceItem(input="[document]", output="[][document]"),
]


@pytest.mark.parametrize("item", url_tests, ids=ReferenceItem.ids(url_tests))
def test_reference_url(item: ReferenceItem):
    assert SmartReference(item.input).is_url() == item.output


@pytest.mark.parametrize("item", intersphinx_tests, ids=ReferenceItem.ids(intersphinx_tests))
def test_reference_intersphinx(item: ReferenceItem):
    assert SmartReference(item.input).is_traditional_intersphinx_reference() == item.output


@pytest.mark.parametrize("item", indirect_tests, ids=ReferenceItem.ids(indirect_tests))
def test_reference_indirect(item: ReferenceItem):
    assert SmartReference(item.input).is_indirect_reference() == item.output


@pytest.mark.parametrize("item", myst_tests, ids=ReferenceItem.ids(myst_tests))
def test_reference_myst(item: ReferenceItem):
    assert SmartReference(item.input).is_myst_reference() == item.output


@pytest.mark.parametrize("item", translate_references, ids=ReferenceItem.ids(translate_references))
def test_reference_to_myst(item: ReferenceItem):
    assert SmartReference(item.input).reference_to_myst() == item.output


@pytest.mark.parametrize("item", translate_links, ids=ReferenceItem.ids(translate_links))
def test_link_to_markdown(item: ReferenceItem):
    assert link_to_markdown(item.input) == item.output


def test_link_to_markdown_all_options():
    assert link_to_markdown(ref="document", label="label", title="title") == '[label](#document "title")'


def test_markdown_wrapper():
    mw = MarkdownWrapper()
    outcome = mw.render('[label](#document "title")')[0].next_node(nodes.reference)
    assert str(outcome) == patch_snippet_docutils_forward(
        '<reference id_link="True" reftitle="title" refuri="#document">label</reference>'
    )
