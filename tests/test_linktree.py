from typing import Callable

import docutils
from verlib2 import Version

from sphinx_design_elements.navigation import demo_tree
from tests.conftest import SphinxBuilder


def test_directive(sphinx_builder: Callable[..., SphinxBuilder]):
    """Quickly test `linktree` directive."""
    builder = sphinx_builder()
    content = "# Heading" + "\n\n\n" + ":::{linktree}\n:::\n\n"
    builder.src_path.joinpath("index.md").write_text(content, encoding="utf8")
    builder.build(assert_pass=False)
    assert "Producing link tree for: index" in builder.status
    assert "build succeeded, 1 warning" in builder.status
    assert "WARNING: toctree is empty" in builder.warnings


def test_linktree_demo_tree(sphinx_html_builder):
    builder = sphinx_html_builder()
    builder.init()
    builder.init_templates()
    builder.init_highlighter()

    tree = demo_tree(builder=builder, context={})
    html = tree.render()

    assert '<p class="caption" role="heading"><span class="caption-text">Project-local page links</span></p>' in html
    # FIXME: Apparently, references to documents can not be resolved yet, in testing mode.
    if Version(docutils.__version__) >= Version("0.22"):
        assert '<li class="toctree-l2"><a class="reference internal" href="#"></a></li>' in html
    else:
        assert '<li class="toctree-l2"><a class="reference internal" href="#">None</a></li>' in html

    assert '<p class="caption" role="heading"><span class="caption-text">Intersphinx links</span></p>' in html
    assert (
        '<li class="toctree-l2"><a class="reference internal" href="https://sphinx-design.readthedocs.io/en/latest/index.html">sphinx-design</a></li>'
        in html
    )

    assert '<p class="caption" role="heading"><span class="caption-text">URL links</span></p>' in html
    assert (
        '<li class="toctree-l2"><a class="reference internal" href="https://example.com">https://example.com</a></li>'
        in html
    )
