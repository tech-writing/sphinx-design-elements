"""
Link tree defaults and examples.

A link tree is a navigation tree component based on docutils, Sphinx toctree, and Furo.
"""

import typing as t

from sphinx.builders import Builder

from sphinx_design_elements.lib.linktree import LinkTree


def default_tree(builder: Builder, context: t.Dict[str, t.Any], docname: t.Optional[str] = None) -> LinkTree:
    """
    The default link tree is just a toc tree.
    """
    # Create LinkTree component.
    linktree = LinkTree.from_context(builder=builder, context=context)

    if docname is not None:
        linktree.docname = docname

    # Add section about current project (self).
    project_name = context["project"]
    project = linktree.project(docname=project_name, title=project_name)

    # Add project toctree.
    project.toctree()

    return linktree


def demo_tree(builder: Builder, context: t.Dict[str, t.Any], docname: t.Optional[str] = None) -> LinkTree:
    """
    The demo link tree showcases some features what can be done.

    It uses regular page links to documents in the current project, a few
    intersphinx references, and a few plain, regular, URL-based links.
    """
    linktree = LinkTree.from_context(builder=builder, context=context)
    doc = linktree.api.doc
    ref = linktree.api.ref
    link = linktree.api.link

    linktree.title("Project-local page links").add(
        doc(name="gridtable"),
        doc(name="infocard"),
    )

    linktree.title("Intersphinx links").add(
        ref("sd:index"),
        ref("sd:badges", label="sphinx{design} badges"),
        # rST link syntax.
        ref("myst:syntax/images_and_figures", "MyST » Images and figures"),
        ref("myst:syntax/referencing", "MyST » Cross references"),
        # MyST link syntax.
        # ref("myst#syntax/images_and_figures"),  # noqa: ERA001
    )

    linktree.title("URL links").add(
        link(uri="https://example.com"),
        link(uri="https://example.com", label="A link to example.com, using a custom label ⚽."),
    )

    return linktree
