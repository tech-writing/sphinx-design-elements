import os
from pathlib import Path
from typing import Any, Callable, Dict, Optional

import pytest
from docutils import nodes
from docutils.parsers.rst import roles
from sphinx import addnodes
from sphinx.testing.path import path as sphinx_path
from sphinx.testing.util import SphinxTestApp
from sphinx_design._compat import findall

pytest_plugins = "sphinx.testing.fixtures"


class SphinxBuilder:
    """
    Sphinx builder fixture implementation for pytest.

    TODO: Currently copied from `sphinx-design`. Maybe import from there instead?
    """

    def __init__(self, app: SphinxTestApp, src_path: Path):
        self.app = app
        self._src_path = src_path

    @property
    def src_path(self) -> Path:
        return self._src_path

    @property
    def out_path(self) -> Path:
        return Path(self.app.outdir)

    def build(self, assert_pass=True):
        self.app.build()
        if assert_pass:
            assert self.warnings == "", self.status
        return self

    @property
    def status(self):
        return self.app._status.getvalue()

    @property
    def warnings(self):
        return self.app._warning.getvalue()

    def get_doctree(self, docname: str, post_transforms: bool = False) -> nodes.document:
        doctree = self.app.env.get_doctree(docname)
        if post_transforms:
            self.app.env.apply_post_transforms(doctree, docname)
        # make source path consistent for test comparisons
        for node in findall(doctree)(include_self=True):
            if not ("source" in node and node["source"]):
                continue
            node["source"] = Path(node["source"]).relative_to(self.src_path).as_posix()
            if node["source"].endswith(".rst"):
                node["source"] = node["source"][:-4]
            elif node["source"].endswith(".md"):
                node["source"] = node["source"][:-3]
        # remove mathjax classes added by myst parser
        if doctree.children and isinstance(doctree.children[0], nodes.section):
            doctree.children[0]["classes"] = []
        return doctree


@pytest.fixture()
def sphinx_builder(tmp_path: Path, make_app, monkeypatch):
    """
    Sphinx builder fixture entrypoint for pytest.

    TODO: Currently copied from `sphinx-design`. Maybe import from there instead?
    """

    def _create_project(buildername: str = "html", conf_kwargs: Optional[Dict[str, Any]] = None):
        src_path = tmp_path / "srcdir"
        src_path.mkdir()
        conf_kwargs = conf_kwargs or {
            "extensions": ["myst_parser", "sphinx_design", "sphinx_design_elements"],
            "myst_enable_extensions": ["colon_fence"],
        }
        content = "\n".join([f"{key} = {value!r}" for key, value in conf_kwargs.items()])
        src_path.joinpath("conf.py").write_text(content, encoding="utf8")
        app = make_app(srcdir=sphinx_path(os.path.abspath(str(src_path))), buildername=buildername)
        return SphinxBuilder(app, src_path)

    yield _create_project


@pytest.fixture
def render(sphinx_builder: Callable[..., SphinxBuilder]):
    roles._roles.clear()

    def do(content, with_container: bool = False):
        builder = sphinx_builder()
        return render_reference_builder(builder, content, with_container=with_container)

    return do


def clean_doctree(doctree, pop_doc_attrs=("translation_progress",)):
    for attr_name in pop_doc_attrs:
        doctree.attributes.pop(attr_name, None)
    return doctree


def render_reference_builder(builder: SphinxBuilder, content: str, with_container: bool = False):
    """Test snippets written in MyST Markdown (after post-transforms)."""
    from tests.test_snippets import write_assets

    builder.app.config.intersphinx_disabled_reftypes = []
    builder.src_path.joinpath("index.md").write_text(content, encoding="utf8")
    write_assets(builder.src_path)
    builder.build()

    text = find_reference(
        clean_doctree(builder.get_doctree("index", post_transforms=True)), with_container=with_container
    ).pformat()
    return text


def find_reference(node: nodes.Node, with_container: bool = False):
    constraint = (nodes.reference, addnodes.pending_xref)
    if with_container:
        constraint = (nodes.container,)
    results = list(node.findall(lambda _node: isinstance(_node, constraint)))
    if results:
        return results[0]
    return node
