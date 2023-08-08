import hashlib
from importlib.resources import read_text
from pathlib import Path

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx_design.extension import depart_container, visit_container

from . import compiled as static_module
from .dropdown_group import setup_dropdown_group
from .gridtable import setup_gridtable
from .infocard import setup_infocard
from .tag import setup_tags


def setup_extension(app: Sphinx) -> None:
    """
    Set up the sphinx extension.
    """

    app.connect("builder-inited", add_assets)
    app.connect("env-updated", update_asset_links)

    # Override container html visitors, to stop the default behaviour
    # of adding the `container` class to all `nodes.container`.
    app.add_node(nodes.container, override=True, html=(visit_container, depart_container))

    setup_gridtable(app)
    setup_infocard(app)
    setup_tags(app)
    setup_dropdown_group(app)


def add_assets(app: Sphinx):
    """
    Copy JS and CSS assets to the build directory.
    """

    # Reset "changed" identifier.
    app.env.settings["sphinx_design_elements_assets_changed"] = False

    # Set up new static path in output dir.
    static_path = (Path(app.outdir) / "_sphinx_design_elements_static").absolute()
    static_existed = static_path.exists()
    static_path.mkdir(exist_ok=True)
    app.config.html_static_path.append(str(static_path))

    # Add asset files.
    add_asset(app, static_path, "addon.js")
    add_asset(app, static_path, "style.css")

    if not static_existed:
        app.env.settings["sphinx_design_elements_assets_changed"] = True


def add_asset(app: Sphinx, static_path: Path, filename: str):
    """
    Copy asset file to the build directory.
    """
    content = read_text(static_module, filename)
    extension = Path(filename).suffix.lstrip(".")
    digest = hashlib.md5(content.encode("utf8")).hexdigest()  # noqa: S324
    path = static_path / f"design-elements.{digest}.{extension}"
    if extension == "js":
        app.add_js_file(path.name)
    elif extension == "css":
        app.add_css_file(path.name)
    else:
        raise ValueError(f"Unable to add asset file, unknown extension: {filename}")
    if not path.exists():
        app.env.settings["sphinx_design_elements_assets_changed"] = True
        for path_delete in static_path.glob(f"*.{extension}"):
            path_delete.unlink()
        path.write_text(content, encoding="utf8")


def update_asset_links(app: Sphinx, env: BuildEnvironment):
    """
    If JS or CSS assets changed, rewrite all files.
    """
    if app.env.settings.get("sphinx_design_elements_assets_changed"):
        return list(env.all_docs.keys())
    return []
