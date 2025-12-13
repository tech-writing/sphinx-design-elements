import os
from unittest.mock import patch

import docutils
from docutils import nodes
from sphinx import addnodes
from sphinx.errors import SphinxError
from sphinx.testing.util import SphinxTestApp
from sphinx_pytest.plugin import AppWrapper, CreateDoctree
from verlib2 import Version

from sphinx_design_elements.hyper import setup_hyper
from tests.conftest import SphinxBuilder
from tests.test_snippets import write_assets


class HyperTestApp(SphinxTestApp):
    def __init__(self, *args, **kwargs):
        setup_rformat()
        setup_hyper(app=self)
        super().__init__(*args, **kwargs)
        self.config.intersphinx_disabled_reftypes = []


def setup_rformat():
    p = patch("sphinx_pytest.plugin.AppWrapper.rformat", rformat, create=True)
    p.start()


def rformat(self: AppWrapper, docname: str = "index", pop_doc_attrs=("translation_progress",)) -> str:
    """
    Return an indented pseudo-XML representation of a reference node.

    It is similar to `pformat`, but does not return a document, but
    a nested child node instead.
    """
    doctree = self.doctrees[docname].deepcopy()

    # Extract reference node.
    results = list(doctree.findall(lambda node: isinstance(node, (nodes.reference, addnodes.pending_xref))))
    if not results:
        text = doctree.pformat().replace(str(self._app.srcdir) + os.sep, "<src>/").rstrip()
        raise SphinxError(f"Rendering failed: {text}")

    doctree = results[0]

    for attr_name in pop_doc_attrs:
        doctree.attributes.pop(attr_name, None)
    text = doctree.pformat()
    return text


def find_reference(node: nodes.Node) -> nodes.Node:
    results = list(node.findall(lambda _node: isinstance(_node, (nodes.reference, addnodes.pending_xref))))
    if results:
        return results[0]
    return node


def clean_doctree(doctree, pop_doc_attrs=("translation_progress",)):
    for attr_name in pop_doc_attrs:
        doctree.attributes.pop(attr_name, None)
    return doctree


def render_reference(doctree: CreateDoctree, content: str) -> str:
    doctree._app_cls = HyperTestApp
    doctree.set_conf(
        {"extensions": ["myst_parser"]},
        # {"extensions": ["myst_parser"], "myst_enable_extensions": ["dollarmath"]}  # noqa: ERA001
    )
    result = doctree(content, "index.md")
    payload = result.rformat()
    result.app.cleanup()
    return payload


def render_reference_builder(builder: SphinxBuilder, content: str) -> str:
    """Test snippets written in MyST Markdown (after post-transforms)."""

    builder.src_path.joinpath("index.md").write_text(content, encoding="utf8")
    write_assets(builder.src_path)
    builder.build()

    return find_reference(clean_doctree(builder.get_doctree("index", post_transforms=True))).pformat()


def patch_snippet_docutils_forward(snippet: str) -> str:
    """
    docutils 0.22 returns a few boolean values as integer values.
    """
    if Version(docutils.__version__) >= Version("0.22"):
        snippet = (
            snippet.replace('has_title="True"', 'has_title="1"')
            .replace('id_link="True"', 'id_link="1"')
            .replace('is_div="True"', 'is_div="1"')
            .replace('refexplicit="True"', 'refexplicit="1"')
            .replace('refexplicit="False"', 'refexplicit="0"')
            .replace('refwarn="True"', 'refwarn="1"')
            .replace('opened="False"', 'opened="0"')
        )
    return snippet


def patch_snippet_docutils_reverse(snippet: str) -> str:
    """
    docutils 0.22 returns a few boolean values as integer values.
    """
    if Version(docutils.__version__) >= Version("0.22"):
        snippet = (
            snippet.replace('has_title="1"', 'has_title="True"')
            .replace('id_link="1"', 'id_link="True"')
            .replace('is_div="1"', 'is_div="True"')
            .replace('refexplicit="1"', 'refexplicit="True"')
            .replace('refexplicit="0"', 'refexplicit="False"')
            .replace('refwarn="1"', 'refwarn="True"')
            .replace('opened="0"', 'opened="False"')
        )
    return snippet
