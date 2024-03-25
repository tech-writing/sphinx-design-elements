import re

import pytest
from sphinx_pytest.plugin import CreateDoctree

from tests.util import render_reference


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
    assert (
        ptree
        == """
<pending_xref refdoc="index" refdomain="std" refexplicit="True" reftarget="foobar" reftype="ref" refwarn="True">
    <inline classes="xref std std-ref">
        foobar
""".lstrip()
    )


def test_hyper_intersphinx(sphinx_doctree_no_tr: CreateDoctree):
    content = "{hyper}`foo:bar`"
    ptree = render_reference(sphinx_doctree_no_tr, content)
    assert (
        ptree
        == """
<pending_xref refdoc="index" refdomain="std" refexplicit="False" reftarget="foo:bar" reftype="ref" refwarn="True">
    <inline classes="xref std std-ref">
        foo:bar
""".lstrip()
    )


def test_hyper_myst(sphinx_doctree_no_tr: CreateDoctree):
    content = "{hyper}`project:index.md`"
    ptree = render_reference(sphinx_doctree_no_tr, content)
    assert (
        ptree
        == """
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
    assert (
        ptree
        == """
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
    assert (
        render(content)
        == """
<reference id_link="True" refid="foobar" reftitle="foobar">
    <image alt="foobar" candidates="{'?': 'https://img.shields.io/badge/foobar-blue'}" uri="https://img.shields.io/badge/foobar-blue">
""".lstrip()
    )


def test_hyper_shield_open(render):
    content = """
(foobar)=
{hyper-open}`foobar`
"""
    assert (
        render(content)
        == """
<reference id_link="True" refid="foobar" reftitle="foobar">
    <image alt="foobar" candidates="{'?': 'https://img.shields.io/badge/Open-foobar-darkblue'}" uri="https://img.shields.io/badge/Open-foobar-darkblue">
""".lstrip()
    )


def test_hyper_unknown_type(render):
    with pytest.raises(NotImplementedError) as ex:
        render("{hyper}`foobar {type=foobar}`")
    assert ex.match(re.escape("Hyperref type not implemented: foobar.Viable choices: ['shield']"))
