from functools import lru_cache
from typing import Any, Optional, Union

from docutils import nodes
from myst_parser.mocking import MockInliner
from sphinx import addnodes
from sphinx.environment import BuildEnvironment
from sphinx.ext.intersphinx import resolve_reference_detect_inventory


def resolve_reference(
    env: BuildEnvironment, document: nodes.document, target: str, label: Optional[str] = None, level: int = 2, **kwargs
) -> nodes.Element:
    """
    Create node layout for a link to a Sphinx intersphinx reference.
    """

    refnode_content = nodes.TextElement(reftarget=target, reftype="any")
    refnode_xref = addnodes.pending_xref(reftarget=target, reftype="any")

    ref = resolve_reference_detect_inventory(
        env=env,
        node=refnode_xref,
        contnode=refnode_content,
    )
    # TODO: Add option to handle unresolved intersphinx references gracefully.
    if ref is None:
        raise ReferenceError(f"Unable to resolve intersphinx reference: {target}")
    refuri = ref["refuri"]
    if label is None:
        label = label_from_reference_element(ref)
    return nodes.reference(refuri=refuri, text=label, internal=True, level=level, **kwargs)


def label_from_reference_element(ref: nodes.Node) -> str:
    """
    Get link label from `nodes.reference` element.

    <reference internal="True" level="2"
        refuri="https://cratedb.com/docs/guide/domain/document/index.html#document">Document Store</reference>
    <reference internal="False" reftitle="(in CrateDB: Guide vlatest)"
        refuri="https://cratedb.com/docs/guide/domain/document/index.html#document"><TextElement>Document Store</TextElement></reference>
    """  # noqa: E501

    """
    txt = ref.next_node(nodes.TextElement).next_node()
    if txt:
        txt = ref.next_node(nodes.TextElement)
    if txt:
        return txt.astext()
    return ref.astext()
    """

    try:
        txt = next(ref.findall(nodes.TextElement, include_self=False))
    except StopIteration:
        txt = ref.next_node(nodes.TextElement)
    if txt:
        return txt.astext()
    return ref.astext()


def link_type(link: Union[str, None]) -> Union[str, None]:
    if link is None:
        return None
    elif link.startswith("http://") or link.startswith("https://"):
        return "url"
    else:
        return "ref"


@lru_cache(maxsize=8192)
def get_html_page_title(url: str) -> str:
    """
    Retrieve HTML page via HTTP, and extract value of <title>TEXT</title>.
    """
    if not (url.startswith("http://") or url.startswith("https://")):
        return url

    from urllib.request import urlopen

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(urlopen(url), "html.parser")  # noqa: S310
    return soup.title and soup.title.get_text() or url


def parse_block_myst(
    self: MockInliner, text: str, lineno: int, memo: Any, parent: nodes.Element
) -> tuple[list[nodes.Node], list[nodes.system_message]]:
    """
    Parse the text and return a list of nodes.

    Similar to `myst_parser.mocking.MockInliner.parse`, but uses
    `inline=False` for rendering, and returns only the inner node.
    """
    with self._renderer.current_node_context(parent):
        container = nodes.Element()
        with self._renderer.current_node_context(container):
            self._renderer.nested_render_text(text, lineno, inline=False)

    # Extract the reference node from the container paragraph node.
    ref = container.next_node().next_node()
    return [ref], []


def parse_block_rst(  # pragma: nocover
    self: MockInliner, text: str, lineno: int, memo: Any, parent: nodes.Element
) -> tuple[list[nodes.Node], list[nodes.system_message]]:
    """
    mw = MarkdownWrapper()
    res = mw.render(text)
    return res, []

    memo.reporter = self.reporter
    memo.document = self.document
    memo.language = self.language
    memo2 = Struct(
        document=self.document,
        reporter=self.reporter,
        language=self.language,
        title_styles=[],
        section_level=0,
        section_bubble_up_kludge=False,
        inliner=self)
    return self.parse(text=text, lineno=lineno, memo=memo, parent=parent)
    """

    error = NotImplementedError("The `hyper` role does not work with reStructuredText yet")
    msg = self.reporter.error(error)
    prb = self.problematic(text, text, msg)
    return [prb], [msg]
