import re

import pytest
from sphinx_pytest.plugin import CreateDoctree

from tests.util import patch_snippet_docutils_forward, render_reference


def test_hyper_unknown_type(render):
    with pytest.raises(NotImplementedError) as ex:
        render("{hyper}`foobar {type=foobar}`")
    assert ex.match(
        re.escape("Hyperref type not implemented: foobar. Viable choices: ['badge', 'button', 'card', 'shield']")
    )


def test_hyper_http_url_valid(sphinx_doctree_no_tr: CreateDoctree):
    content = "{hyper}`https://example.org`"
    ptree = render_reference(sphinx_doctree_no_tr, content)
    assert (
        ptree
        == """
<reference refuri="https://example.org">
    Example Domain
""".lstrip()
    )


def test_hyper_http_url_invalid(sphinx_doctree_no_tr: CreateDoctree):
    content = "{hyper}`https://randomfoobarunknown.org`"
    ptree = render_reference(sphinx_doctree_no_tr, content)
    assert (
        ptree
        == """
<reference refuri="https://randomfoobarunknown.org">
    https://randomfoobarunknown.org
""".lstrip()
    )


def test_hyper_mailto_url(sphinx_doctree_no_tr: CreateDoctree):
    content = "{hyper}`mailto:test@example.org`"
    ptree = render_reference(sphinx_doctree_no_tr, content)
    assert (
        ptree
        == """
<reference refuri="mailto:test@example.org">
    mailto:test@example.org
""".lstrip()
    )


def test_hyper_label_pending(sphinx_doctree_no_tr: CreateDoctree):
    content = "{hyper}`foobar`"
    ptree = render_reference(sphinx_doctree_no_tr, content)
    assert ptree == patch_snippet_docutils_forward(
        """
<pending_xref refdoc="index" refdomain="std" refexplicit="True" reftarget="foobar" reftype="ref" refwarn="True">
    <inline classes="xref std std-ref">
        foobar
""".lstrip()
    )


def test_hyper_intersphinx(sphinx_doctree_no_tr: CreateDoctree):
    content = "{hyper}`foo:bar`"
    ptree = render_reference(sphinx_doctree_no_tr, content)
    assert ptree == patch_snippet_docutils_forward(
        """
<pending_xref refdoc="index" refdomain="std" refexplicit="False" reftarget="foo:bar" reftype="ref" refwarn="True">
    <inline classes="xref std std-ref">
        foo:bar
""".lstrip()
    )


def test_hyper_myst(sphinx_doctree_no_tr: CreateDoctree):
    content = "{hyper}`project:index.md`"
    ptree = render_reference(sphinx_doctree_no_tr, content)
    assert ptree == patch_snippet_docutils_forward(
        """
<pending_xref refdoc="index" refdomain="doc" refexplicit="True" reftarget="index" reftargetid="True" reftype="myst">
    <inline classes="xref myst">
        project:index.md
""".lstrip()
    )


def test_hyper_indirect(render):
    content = """
{hyper}`Example Domain <[foobar]>`

[foobar]: https://example.org/
"""
    ptree = render(content)
    assert (
        ptree
        == """
<reference refuri="https://example.org/">
    Example Domain
""".lstrip()
    )


def test_hyper_explicit_title(sphinx_doctree_no_tr: CreateDoctree):
    content = """
(foobar)=
{hyper}`title <foobar>`
"""
    ptree = render_reference(sphinx_doctree_no_tr, content)
    assert ptree == patch_snippet_docutils_forward(
        """
<pending_xref refdoc="index" refdomain="std" refexplicit="True" reftarget="foobar" reftype="ref" refwarn="True">
    <inline classes="xref std std-ref">
        title
""".lstrip()
    )


def test_hyper_shield_label(render):
    content = """
(foobar)=
{hyper}`foobar {type=shield}`
"""
    assert render(content) == patch_snippet_docutils_forward(
        """
<reference id_link="True" refid="foobar" reftitle="foobar">
    <image alt="foobar" candidates="{'?': 'https://img.shields.io/badge/foobar-blue'}" uri="https://img.shields.io/badge/foobar-blue">
""".lstrip()
    )


def test_hyper_shield_open(render):
    content = """
(foobar)=
{hyper-open}`foobar`
"""
    assert render(content) == patch_snippet_docutils_forward(
        """
<reference id_link="True" refid="foobar" reftitle="foobar">
    <image alt="foobar" candidates="{'?': 'https://img.shields.io/badge/Open-foobar-darkblue'}" uri="https://img.shields.io/badge/Open-foobar-darkblue">
""".lstrip()
    )


def test_hyper_button_basic(render):
    content = """
{hyper}`https://example.org {type=button}`
"""
    assert (
        render(content)
        == """
<reference classes="sd-sphinx-override sd-btn sd-text-wrap sd-btn-primary" refuri="https://example.org">
    <inline>
        Example Domain
""".lstrip()
    )


def test_hyper_button_with_icon(render):
    content = """
{hyper}`https://example.org {type=button,icon=octicon:report}`
"""
    text = render(content)

    assert '<raw format="html"' in text
    assert '<svg version="1.1"' in text
    assert "example.org" in text
    assert "Example Domain" in text


def test_hyper_button_icon_only(render):
    content = """
{hyper}`https://example.org {type=button,icon=octicon:report,notext=true}`
"""
    text = render(content)

    assert '<raw format="html"' in text
    assert '<svg version="1.1"' in text
    assert "example.org" in text
    assert "Example Domain" not in text


def test_hyper_badge(render):
    content = """
{hyper}`https://example.org {type=badge}`
"""
    text = render(content)

    assert (
        text
        == """
<reference classes="sd-sphinx-override sd-badge sd-bg-primary sd-bg-text-primary" refuri="https://example.org">
    <inline>
        Example Domain
""".lstrip()
    )


def test_hyper_card_minimal(render):
    content = """
{hyper}`https://example.org {type=card}`
"""
    text = render(content, with_container=True)

    assert text == patch_snippet_docutils_forward(
        """
<container classes="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm sd-card-hover" design_component="card" is_div="True">
    <container classes="sd-card-body" design_component="card-body" is_div="True">
        <paragraph classes="sd-card-text">
            Example Domain
    <PassthroughTextElement>
        <reference classes="sd-stretched-link sd-hide-link-text" refuri="https://example.org">
            <inline>
                https://example.org
""".lstrip()  # noqa: E501
    )


def test_hyper_card_full(render):
    content = """
{hyper}`https://example.org {type=card,title=title,header=header,footer=footer}`
"""
    text = render(content, with_container=True)

    assert text == patch_snippet_docutils_forward(
        """
<container classes="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm sd-card-hover" design_component="card" is_div="True">
    <container classes="sd-card-header" design_component="card-header" is_div="True">
        <paragraph classes="sd-card-text">
            header
    <container classes="sd-card-body" design_component="card-body" is_div="True">
        <container classes="sd-card-title sd-font-weight-bold" design_component="card-title" is_div="True">
            <PassthroughTextElement>
                title
        <paragraph classes="sd-card-text">
            Example Domain
    <container classes="sd-card-footer" design_component="card-footer" is_div="True">
        <paragraph classes="sd-card-text">
            footer
    <PassthroughTextElement>
        <reference classes="sd-stretched-link sd-hide-link-text" refuri="https://example.org">
            <inline>
                https://example.org
""".lstrip()  # noqa: E501
    )
