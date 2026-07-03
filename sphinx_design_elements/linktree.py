import sys
import traceback
from typing import List

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.errors import SphinxError
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

from sphinx_design_elements.lib.linktree import LinkTree

logger = logging.getLogger(__name__)


def setup_linktree(app: Sphinx):
    """
    Set up the `linktree` directive.
    """
    app.add_node(linktree)
    app.add_directive("linktree", LinkTreeDirective)
    app.connect("doctree-resolved", LinkTreeProcessor)


class linktree(nodes.General, nodes.Element):
    """
    The docutils node representing a `linktree` directive.
    """

    pass


class LinkTreeDirective(SphinxDirective):
    """
    The link tree is similar to a toc tree, but programmable.

    The `linktree` directive works similar like the `toctree` directive, by first
    collecting all occurrences, and serializing them into a surrogate representation.
    After that, the `LinkTreeProcessor` will actually render the directive using the
    LinkTree utility.
    """

    has_content = True
    required_arguments = 0
    optional_arguments = 1
    # TODO: Maybe rename `title` to `caption`?
    # TODO: Implement `target` directive option, in order to link to arbitrary places by ref or URI.
    option_spec = {
        "docname": directives.unchanged,
        "title": directives.unchanged,
        "maxdepth": directives.unchanged,
    }

    def run(self) -> List[nodes.Node]:
        """
        Translate `linktree` directives into surrogate representation,
        carrying over all the directive options.
        """

        if self.content:
            message = (
                f"The 'linktree' directive currently does not accept content. "
                f"The offending node is:\n{self.block_text}"
            )
            self.reporter.severe(message)  # type: ignore[attr-defined]
            raise SphinxError(message)

        # Create a surrogate node element.
        surrogate = linktree("")

        # Set the `freeflow` flag, which will signal to wrap the result element into
        # a corresponding container to make it render properly, like in the sidebar.
        surrogate["freeflow"] = True

        # Propagate directive options 1:1.
        for option in self.option_spec.keys():
            if option in self.options:
                surrogate[option] = self.options[option]

        return [surrogate]


class LinkTreeProcessor:
    """
    Process surrogate `linktree` nodes, and render them using the `LinkTree` utility.
    """

    def __init__(self, app: Sphinx, doctree: nodes.document, docname: str) -> None:
        self.app = app
        self.builder = app.builder
        self.config = app.config
        self.env = app.env

        try:
            self.process(doctree, docname)
        except Exception:
            logger.exception("Unable to render LinkTree")

    def process(self, doctree: nodes.document, docname: str) -> None:
        """
        Process surrogate <linktree/> nodes.

        TODO: In this rendering mode, somehow the mechanics provided by Furo get lost.
        """
        for node in list(doctree.findall(linktree)):
            if "docname" in node:
                docname = node["docname"]

            # TODO: Discuss different container node type.
            container: nodes.Element = nodes.section()
            if "freeflow" in node and node["freeflow"]:
                container["classes"].append("sidebar-tree")
            container.append(self.produce(node, docname))
            node.replace_self(container)

    def produce(self, node: nodes.Element, docname: str) -> nodes.Element:
        """
        Produce rendered node tree, effectively a document's toc tree.
        """
        lt = LinkTree.from_app(builder=self.builder, docname=docname)
        title = None
        if "title" in node:
            title = node["title"]
        project = lt.project(title=title)
        try:
            project.toctree(maxdepth=int(node.get("maxdepth", -1)))
        except Exception as ex:
            exc_type, exc_value, exc_tb = sys.exc_info()
            tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
            message = (
                f"Error producing a toc tree for document using the 'linktree' directive: {docname}. "
                f"The offending node is:\n{node}\nThe exception was:\n{tb}"
            )
            raise SphinxError(message) from ex
        return lt.container
