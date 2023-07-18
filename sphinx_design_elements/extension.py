import hashlib
from importlib.resources import read_text
from pathlib import Path

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx_design.extension import depart_container, visit_container

from . import compiled as static_module
from .gridtable import setup_gridtable
from .infocard import setup_infocard
from .tag import setup_tags


def setup_extension(app: Sphinx) -> None:
    """Set up the sphinx extension."""

    app.connect("builder-inited", update_css_js)
    app.connect("env-updated", update_css_links)
    # we override container html visitors, to stop the default behaviour
    # of adding the `container` class to all nodes.container
    app.add_node(nodes.container, override=True, html=(visit_container, depart_container))

    setup_gridtable(app)
    setup_infocard(app)
    setup_tags(app)


def update_css_js(app: Sphinx):
    """Copy the CSS to the build directory."""
    # reset changed identifier
    app.env.settings["sphinx_design_elements_css_changed"] = False
    # setup up new static path in output dir
    static_path = (Path(app.outdir) / "_sphinx_design_elements_static").absolute()
    static_existed = static_path.exists()
    static_path.mkdir(exist_ok=True)
    app.config.html_static_path.append(str(static_path))
    # Read the css content and hash it
    content = read_text(static_module, "style.css")
    digest = hashlib.md5(content.encode("utf8")).hexdigest()  # noqa: S324
    # Write the css file
    css_path = static_path / f"elements-style.{digest}.min.css"
    app.add_css_file(css_path.name)
    if css_path.exists():
        return
    if static_existed:
        app.env.settings["sphinx_design_elements_css_changed"] = True
    for path in static_path.glob("*.css"):
        path.unlink()
    css_path.write_text(content, encoding="utf8")


def update_css_links(app: Sphinx, env: BuildEnvironment):
    """If CSS has changed, all files must be re-written, to include the correct stylesheets."""
    if app.env.settings.get("sphinx_design_elements_css_changed"):
        return list(env.all_docs.keys())
    return []
