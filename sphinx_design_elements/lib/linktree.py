import typing as t

from docutils import nodes
from furo import get_navigation_tree
from sphinx import addnodes
from sphinx.builders import Builder
from sphinx.builders.html import StandaloneHTMLBuilder

try:
    # Sphinx 8.x+
    from sphinx.environment.adapters.toctree import TocTree
except ImportError:
    # Sphinx 7.x and earlier
    from sphinx.environment import TocTree  # type: ignore[attr-defined,no-redef]
from sphinx.errors import SphinxError
from sphinx.ext.intersphinx import resolve_reference_detect_inventory
from sphinx.util import logging

logger = logging.getLogger(__name__)


class LinkTree:
    """
    Link tree implementation.

    A link tree is a navigation tree component based on docutils, Sphinx toctree, and Furo.
    It is similar to a toc tree, but programmable.
    """

    def __init__(
        self,
        builder: Builder,
        docname: t.Optional[str] = None,
        project_name: t.Optional[str] = None,
        root_doc: t.Optional[str] = None,
        pathto: t.Optional[t.Callable] = None,
    ):
        self.builder = builder

        self.docname = docname
        self.project_name = project_name
        self.root_doc = root_doc
        self.pathto = pathto

        self.api = Api(root=self)
        self.util = Util(root=self)

        # Which string to strip from each link label.
        # Can be used to get rid of label/title prefixes.
        self.strip_from_label: t.Optional[str] = None

        # Runtime setup.
        self.setup()

        # The root node of a link tree is actually a toc tree.
        self.container = addnodes.compact_paragraph(toctree=True)

        logger.info(f"Producing link tree for: {self.docname}")

    @classmethod
    def from_context(cls, builder: Builder, context: t.Dict[str, t.Any]) -> "LinkTree":
        """
        Create a link tree instance from the current Sphinx context.
        """
        page_name = context.get("pagename")
        project_name = context.get("project")
        root_doc = context.get("root_doc", context.get("master_doc"))
        pathto = context.get("pathto")
        return cls(builder=builder, docname=page_name, project_name=project_name, root_doc=root_doc, pathto=pathto)

    @classmethod
    def from_app(cls, builder: Builder, docname: t.Optional[str] = None) -> "LinkTree":
        """
        Create a link tree instance without a Sphinx context.
        """
        try:
            if docname is None:
                docname = builder.app.env.docname
        except Exception:
            logger.warning("Unable to derive docname from application environment")

        return cls(builder=builder, docname=docname)

    def setup(self) -> None:
        """
        Link tree runtime setup.
        """

        # When not running on behalf of a Sphinx context, `pathto` is not available.
        # TODO: Is there some other way to get it?
        if self.pathto is None:
            logger.info("WARNING: Running without Sphinx context, unable to compute links using `pathto`")
            self.pathto = lambda x: None

    def remove_from_title(self, text: t.Optional[str]) -> None:
        """
        Set the string which should be stripped from each link label.
        """
        self.strip_from_label = text

    def title(self, text: str) -> "LinkTree":
        """
        Add a title node to the link tree.
        """
        self.container.append(self.util.title(text))
        return self

    def add(self, *items) -> None:
        """
        Add one or many elements or nodes to the link tree.
        """
        for item in items:
            if hasattr(item, "container"):
                real = item.container
            else:
                real = item
            self.container.append(real)

    def project(self, docname: t.Optional[str] = None, title: t.Optional[str] = None) -> "ProjectSection":
        """
        Add a project section to the link tree.
        """
        docname = docname or self.docname
        logger.info(f"New project with name={docname}, title={title}")
        p = ProjectSection(root=self, name=docname, title=title)
        self.add(p)
        return p

    def render(self) -> str:
        """
        Enhance and render link tree using Furo UI mechanics and styles.

        - https://github.com/pradyunsg/furo/blob/2023.05.20/src/furo/navigation.py
        - https://github.com/pradyunsg/furo/blob/2023.05.20/src/furo/__init__.py#L164-L220
        """
        if not isinstance(self.builder, StandaloneHTMLBuilder):
            raise SphinxError(f"Sphinx builder needs to be of type StandaloneHTMLBuilder: {type(self.builder)}")
        linktree_html = self.builder.render_partial(self.container)["fragment"]
        return get_navigation_tree(linktree_html)


class ProjectSection:
    """
    A section within the link tree which represents a whole project.
    """

    def __init__(self, root: LinkTree, name: t.Optional[str], title: t.Optional[str]):
        env = root.builder.app.env

        self.root = root
        self.name = name
        self.title = title

        # When no title is given, try to resolve it from the environment.
        if self.title is None and name in env.titles:
            self.title = env.titles[name].astext()
        if self.title is None:
            logger.warning(f"Unable to derive link label, document does not exist: {name}")

        # Create project node layout and root node.
        self.container = nodes.bullet_list(classes=self.classes)
        self.main = self.root.util.project(name=self.name, label=self.title, level=1)
        self.inner = nodes.bullet_list()
        self.container.append(self.main)
        self.main.append(self.inner)

    @property
    def classes(self) -> t.List[str]:
        """
        Compute CSS classes based on runtime / selection info.
        """
        if self.is_current_project():
            return ["current"]
        return []

    def is_current_project(self) -> bool:
        """
        Whether the component is rendering the current project (self).

        This information will get used to add `current` CSS classes, when the project has been selected.
        """
        return self.name == self.root.project_name

    def add(self, *items) -> "ProjectSection":
        """
        Add one or many elements or nodes to the project section.
        """
        self.inner.extend(items)
        return self

    def toctree(self, docname: t.Optional[str] = None, maxdepth: int = -1) -> "ProjectSection":
        """
        Generate a toctree node tree, and add it to the project section.
        """
        logger.info(f"Generating toctree for document: {docname}")
        if docname is None:
            docname = self.root.docname

        toctree = self.root.util.toctree(docname=docname, maxdepth=maxdepth)
        if toctree is not None:
            self.add(toctree)
        else:
            logger.warning("WARNING: toctree is empty")
        return self


class Api:
    """
    An API to the low-level node factory functions.
    """

    def __init__(self, root: LinkTree):
        self.root = root

    @staticmethod
    def wrap_ul(elem):
        ul = nodes.bullet_list()
        ul.append(elem)
        return ul

    def doc(self, name: str, label: t.Optional[str] = None, level: int = 2, **kwargs):
        return self.wrap_ul(self.root.util.doc(name, label, level, **kwargs))

    def link(self, uri: str, label: t.Optional[str] = None, level: int = 2, **kwargs):
        return self.wrap_ul(self.root.util.link(uri, label, level, **kwargs))

    def ref(self, target: str, label: t.Optional[str] = None, level: int = 2, **kwargs):
        return self.wrap_ul(self.root.util.ref(target, label, level, **kwargs))


class Util:
    """
    Low-level node factory functions.
    """

    def __init__(self, root: LinkTree):
        self.root = root

    @staticmethod
    def title(text: str) -> nodes.Element:
        return nodes.title(text=text)

    @staticmethod
    def item(**kwargs) -> nodes.Element:
        """
        Create node layout for all kinds of linked items.
        """

        # Compute CSS classes.
        level = 1
        if "level" in kwargs:
            level = int(kwargs["level"])
            del kwargs["level"]
        toctree_class = f"toctree-l{level}"
        classes = kwargs.get("classes", [])
        effective_classes = [toctree_class] + classes

        # Container node: <li>.
        container = nodes.list_item(classes=effective_classes)

        # Intermediary node.
        content = addnodes.compact_paragraph(classes=effective_classes)

        # Inner node: The reference.
        # An example call to `nodes.reference` looks like this.
        # `nodes.reference(refuri="foobar.html", label="Foobar", internal=True)`
        ref = nodes.reference(**kwargs)

        content.append(ref)
        container.append(content)
        return container

    def doc(self, name: str, label: t.Optional[str] = None, level: int = 2, **kwargs) -> nodes.Element:
        """
        Create node layout for a link to a Sphinx document.
        """
        if self.root.pathto is None:
            raise SphinxError("pathto is not defined")
        refuri = self.root.pathto(name)
        if label is None:
            titles = self.root.builder.app.env.titles
            if name in titles:
                label = self.root.builder.app.env.titles[name].astext()
            else:
                logger.warning(f"Unable to derive label from document: {name}")
        kwargs.setdefault("classes", [])
        if name == self.root.docname:
            kwargs["classes"] += ["current", "current-page"]
        return self.item(refuri=refuri, text=label, internal=True, level=level, **kwargs)

    def link(self, uri: str, label: t.Optional[str] = None, level: int = 2, **kwargs):
        """
        Create node layout for a basic URL-based link.
        """
        # FIXME: Fix visual appearance of `internal=False`, then start using it.
        if label is None:
            label = uri
        return self.item(refuri=uri, text=label, internal=True, level=level, **kwargs)

    def ref(self, target: str, label: t.Optional[str] = None, level: int = 2, **kwargs) -> t.Optional[nodes.Element]:
        """
        Create node layout for a link to a Sphinx intersphinx reference.
        """
        refnode_content = nodes.TextElement(reftarget=target, reftype="any")
        refnode_xref = addnodes.pending_xref(reftarget=target, reftype="any")
        ref = resolve_reference_detect_inventory(
            env=self.root.builder.app.env,
            node=refnode_xref,
            contnode=refnode_content,
        )
        # TODO: Add option to handle unresolved intersphinx references gracefully.
        if ref is None:
            raise SphinxError(f"Unable to resolve intersphinx reference: {target}")
        refuri = ref["refuri"]
        if label is None:
            txt = next(ref.findall(nodes.TextElement, include_self=False))
            label = txt.astext()
            if self.root.strip_from_label is not None:
                label = label.replace(self.root.strip_from_label, "").strip()
        return self.item(refuri=refuri, text=label, internal=True, level=level, **kwargs)

    def project(self, name: t.Optional[str], label: t.Optional[str], level: int = 1, **kwargs) -> nodes.Element:
        """
        Create project section node layout.
        """
        if self.root.pathto is None:
            raise SphinxError("pathto is not defined")
        refuri = self.root.pathto(self.root.root_doc)
        kwargs.setdefault("classes", [])
        if name == self.root.project_name:
            kwargs.setdefault("classes", [])
            kwargs["classes"] += ["current"]
        return self.item(refuri=refuri, text=label, internal=True, level=level, **kwargs)

    def toctree(self, docname: t.Optional[str], maxdepth: int = -1) -> t.Optional[nodes.Element]:
        """
        Create node layout of classic Sphinx toctree.
        """
        if docname is None:
            raise SphinxError("Unable to compute toctree without docname")
        return _get_local_toctree_unrendered(
            builder=self.root.builder,
            docname=docname,
            maxdepth=maxdepth,
        )


def _get_local_toctree_unrendered(
    builder, docname: str, collapse: bool = False, **kwargs: t.Any
) -> t.Optional[nodes.Element]:
    """
    Build a toctree for the given document and options, without rendering it to HTML yet.

    From `sphinx.builders.html._get_local_toctree`.

    TODO: Also look at implementations from Executable Books Theme.
    """
    """
    if 'includehidden' not in kwargs:
        kwargs['includehidden'] = False
    """
    if kwargs.get("maxdepth") == "":
        kwargs.pop("maxdepth")

    return TocTree(builder.app.env).get_toctree_for(docname, builder, collapse, **kwargs)
