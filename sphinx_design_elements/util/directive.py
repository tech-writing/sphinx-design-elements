import typing as t
from unittest.mock import patch

from docutils import nodes
from myst_parser.config.main import MdParserConfig
from myst_parser.mdit_to_docutils.base import REGEX_SCHEME
from myst_parser.mdit_to_docutils.sphinx_ import SphinxRenderer
from myst_parser.parsers.mdit import create_md_parser


class MarkdownWrapper:
    """
    Poor-mans reStructuredText -> MyST bridge.

    Usage: When in reStructuredText, but an extension needs to parse something
    in MyST.

    Details: For example, `shield` / `hyper` machineries are heavily based on
    Markdown for sub-element rendering, so they need the MyST machinery when
    invoked from reStructuredText.
    """

    def __init__(self):
        self.config = MdParserConfig()
        self.config.suppress_warnings = []
        self.parser = create_md_parser(self.config, SphinxRenderer)

    def render(self, content: str) -> t.List[nodes.Element]:
        """
        Render a Markdown expression / markup.
        """
        with self.renderer_patch():
            res = self.parser.render(content)
            return res.children

    def renderer_patch(self):
        """
        Because the Sphinx MyST renderer has not been initialized fully, work around it.
        """
        return patch("myst_parser.mdit_to_docutils.sphinx_.SphinxRenderer.__getattr__")


# A global instance, so it does not need to be created per element.
mw = MarkdownWrapper()


class SmartReference:
    """
    Evaluate and resolve all kinds of references.
    """

    def __init__(self, ref: str):
        self.ref = ref

    def is_url(self) -> bool:
        """
        Check if reference is an URL, according to its scheme prefix.

        Sphinx' understanding is defined per:

        :REGEX_SCHEME:
            ^([a-zA-Z][a-zA-Z0-9+.-]*):

        :url_schemes:
            One of http, https, mailto, ftp.
        """
        scheme_match = REGEX_SCHEME.match(self.ref)
        scheme = None if scheme_match is None else scheme_match.group(1)
        if scheme in mw.config.url_schemes:
            return True
        return False

    def is_traditional_intersphinx_reference(self) -> bool:
        """
        Check if reference is an intersphinx one, like `<inventory>:<label>`?
        """
        if self.is_myst_reference():
            return False
        if ":" in self.ref and len(self.ref.split(":")) == 2:
            return True
        return False

    def is_myst_reference(self) -> bool:
        """
        Check if link expression is a MyST link.

        Parse `<http://link.com>` or `[text](link "title")` syntax to docutils AST,
        stolen from `myst_parser.mdit_to_docutils.base.DocutilsRenderer.render_link`.
        """

        if self.ref.startswith("#"):
            return True

        scheme_match = REGEX_SCHEME.match(self.ref)
        scheme = None if scheme_match is None else scheme_match.group(1)

        if scheme in ["inv", "path", "project"]:
            return True

        return False

    def is_indirect_reference(self) -> bool:
        """
        Check if reference is an indirect reference.

        Indirect references are defined out-of-band from the link definition, for example
        at the end of the page.

        - In MyST, it is defined by `[label]: URL`.
        - In reST, it is defined by `.. _label: URL`.
        """
        return self.ref.startswith("[") and self.ref.endswith("]")

    def reference_to_myst(self) -> str:
        """
        Convert traditional Sphinx reference format to MyST,
        suitable for both local, and intersphinx references.

        Examples:

          In:  document
          Out: #document

          In:  guide:document
          Out: inv:guide#document

        """
        if self.is_url() or self.is_myst_reference() or self.is_indirect_reference():
            ref = self.ref
        elif self.is_traditional_intersphinx_reference():
            inventory, label = self.ref.split(":")
            ref = f"inv:{inventory}#{label}"
        else:
            ref = f"#{self.ref}"
        return ref


def link_to_markdown(ref: str, label: t.Union[str, None] = None, title: t.Union[str, None] = None) -> str:
    """
    Given a Sphinx reference of different sorts, render a Markdown link representation.
    """
    label = label or ""
    smartref = SmartReference(ref=ref)
    if smartref.is_indirect_reference():
        return f"[{label}]{ref}"
    link_effective = smartref.reference_to_myst()
    if title:
        link_effective += f' "{title}"'
    return f"[{label}]({link_effective})"
