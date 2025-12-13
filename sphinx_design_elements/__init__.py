"""A sphinx extension for designing beautiful, view size responsive web components."""

from importlib import metadata
from typing import TYPE_CHECKING

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:  # pragma: no cover
    # Case where package metadata is not available.
    __version__ = "0.0.0"
del metadata  # optional, avoids polluting the results of dir(__package__)


if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: "Sphinx") -> dict:
    from .extension import setup_extension

    setup_extension(app)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
