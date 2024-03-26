import re
from typing import Any, Dict, List, Tuple, Union
from unittest.mock import patch
from urllib.parse import parse_qs

import yaml
from docutils import nodes
from docutils.nodes import Node, system_message, unescape
from docutils.parsers.rst.states import Inliner
from myst_parser.mocking import MockInliner
from sphinx.application import Sphinx
from sphinx.jinja2glue import _tobool
from sphinx.roles import AnyXRefRole
from sphinx.util.docutils import SphinxRole

from sphinx_design_elements.util.directive import SmartReference
from sphinx_design_elements.util.role import (
    get_html_page_title,
    label_from_reference_element,
    link_type,
    parse_block_myst,
    parse_block_rst,
    resolve_reference,
)


def setup_hyper(app: Sphinx):
    """
    Set up the `hyper` shortcut role.
    """
    p = patch("myst_parser.mocking.MockInliner.parse_block", parse_block_myst, create=True)
    p.start()
    p2 = patch("docutils.parsers.rst.states.Inliner.parse_block", parse_block_rst, create=True)
    p2.start()
    app.add_role("hyper", HyperRefRole(app=app))
    app.add_role("hyper-navigate", HyperNavigateRole(app=app))
    app.add_role("hyper-open", HyperOpenRole(app=app))
    app.add_role("hyper-tutorial", HyperTutorialRole(app=app))
    app.add_role("hyper-read-more", HyperReadMoreRole(app=app))
    app.add_role("hyper-readme-github", HyperReadmeGitHubRole(app=app))
    app.add_role("hyper-nb-colab", HyperNotebookColabRole(app=app))
    app.add_role("hyper-nb-binder", HyperNotebookBinderRole(app=app))
    app.add_role("hyper-nb-github", HyperNotebookGitHubRole(app=app))


class HyperRefRole(AnyXRefRole):
    """
    Craft hyperlinks with style.

    Synopsis:

    {hyper}`Navigate to Tutorial <fts-analyzer> {type=shield,color=darkcyan,logo=Markdown}`
    """

    special_types = [
        "button",
        "shield",
    ]

    options_re = re.compile(r"^(?P<target>.+?)\s*(?:{(?P<options>.+)})?$", re.DOTALL)
    title_and_options_re = re.compile(
        r"^(?P<title>.+?)\s*(?<!\x00)<(?P<target>.+?)>(?:\s*{(?P<options>.+)})?$", re.DOTALL
    )

    default_options: Dict[str, str] = {}

    def __init__(self, app: Sphinx, *args, **kwargs):
        # Any number of options for the reference role.
        self.ref_options: Dict[str, Any] = {}
        self.system_messages: List[nodes.system_message] = []
        self.app = app
        super().__init__(*args, **kwargs)

    def __call__(
        self,
        name: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Union[Inliner, MockInliner],
        options: Union[Dict, None] = None,
        content: Union[List[str], None] = None,
    ) -> Tuple[List[Node], List[system_message]]:

        self.rawtext = rawtext
        self.text = unescape(text)
        self.lineno = lineno
        self.inliner = inliner  # type: ignore[assignment]
        # self.options = options  # noqa: ERA001
        # self.content = content  # noqa: ERA001

        options = options or {}
        content = content or []

        # if the first character is a bang, don't cross-reference at all
        self.disabled = text.startswith("!")

        self.title = ""
        self.target = ""
        self.ref_options = {}
        if self.default_options:
            self.ref_options.update(self.default_options)

        matched = self.title_and_options_re.match(text)
        if matched:
            self.has_explicit_title = True
        else:
            self.has_explicit_title = False
            matched = self.options_re.match(text)

        if matched:
            data = matched.groupdict()
            for key, value in data.items():
                if value is not None:
                    data[key] = unescape(value)
            if data["options"]:
                self.ref_options.update(decode_hyper_options(data["options"]))
            title = data.get("title")
            target = data.get("target")

            if target:
                self.target = target
            if title:
                self.title = title

            self.srh = SmartReference(ref=self.target)

            # When no title is given, attempt to resolve it from the reference.
            if not self.title:
                try:
                    label = self.resolve_page_title()
                except ReferenceError:
                    label = None
                if label:
                    self.title = label

        else:
            error = ValueError("Unable to resolve reference")
            msg = inliner.reporter.warning(error)  # type: ignore[union-attr]
            prb = inliner.problematic(rawtext, rawtext, msg)  # type: ignore[union-attr]
            return [prb], [msg]

        return SphinxRole.__call__(self, name, rawtext, text, lineno, inliner, options, content)  # type: ignore[arg-type]

    def resolve_page_title(self) -> str:
        """
        Resolve page title from reference or URL.
        """
        ref: Union[nodes.Node, nodes.Element, None] = None
        if self.srh.is_url():
            try:
                return get_html_page_title(self.target)
            except Exception:
                return self.target
        elif self.srh.is_traditional_intersphinx_reference():
            document = self.inliner.document  # type: ignore[attr-defined]
            ref = resolve_reference(env=self.app.env, document=document, target=self.target)
        elif self.srh.is_myst_reference():
            link = f"[]({self.target})"
            ref = self.render_snippet(link)[0][0]
        if ref is not None:
            return label_from_reference_element(ref)
        return self.target

    def run(self) -> Tuple[List[nodes.Node], List[nodes.system_message]]:
        """Run the role."""

        if self.title and "short-title" in self.ref_options:
            del self.ref_options["short-title"]
            self.title = self.title.split(" - ", 1)[0]

        if not self.ref_options:
            title = self.target
            if self.title:
                title = self.title
            if self.srh.is_url() or self.srh.is_myst_reference():
                snippet = f"[{title}]({self.target})"
            elif self.srh.is_indirect_reference():
                title = title.strip("[]")
                snippet = f"[{title}]{self.target}"
            else:
                if self.title:
                    snippet = f"{{ref}}`{self.title}<{self.target}>`"
                else:
                    snippet = f"{{ref}}`{self.target}`"
            return self.render_snippet(snippet)

        type_ = self.ref_options.get("type")
        if type_ not in self.special_types:
            raise NotImplementedError(
                f"Hyperref type not implemented: {type_}." f"Viable choices: {self.special_types}"
            )
        del self.ref_options["type"]

        tpl = {
            "title": self.title,
            "target": self.target,
        }

        # Argument and content of directive.
        argument0 = ""
        content = ""

        if type_ == "button":
            self.ref_options.setdefault("color", "primary")
            no_text = _tobool(self.ref_options.pop("notext", False))

            argument0 = self.target
            if self.srh.is_url():
                type_ = "button-link"
            else:
                type_ = "button-ref"
            if self.title and not no_text:
                content = self.title

            if icon := self.ref_options.pop("icon", None):
                icon_type, icon_options = icon.split(":")
                icon_myst = f"{{{icon_type}}}`{icon_options}`"
                content = f"{icon_myst} {content}"

        elif type_ == "shield":
            self.ref_options.setdefault("message", self.title or self.target)

            if message := self.ref_options.get("message"):
                message = message % tpl
                self.ref_options["message"] = message
            if label := self.ref_options.get("label"):
                label = label % tpl
                self.ref_options["label"] = label

            self.ref_options.setdefault("link", self.target)
            self.ref_options.setdefault("link-type", link_type(self.ref_options.get("link")))
            self.ref_options.setdefault("link-title", self.ref_options["message"])

        else:
            raise NotImplementedError(f"Hyper type not implemented: {type_}")

        snippet = f":::{{{type_}}} {argument0}\n{self.directive_options}{content}\n:::"
        return self.render_snippet(snippet)

    def render_snippet(self, snippet: str) -> Tuple[List[nodes.Node], List[nodes.system_message]]:
        """
        Render a MyST snippet.
        """
        directive_nodes, _ = self.inliner.parse_block(  # type: ignore[attr-defined]
            text=snippet, lineno=self.lineno, memo=self, parent=self.inliner.parent  # type: ignore[attr-defined]
        )
        if not directive_nodes:
            return [], self.system_messages
        node = directive_nodes[0]
        self.set_source_info(node)
        return [node], self.system_messages

    @property
    def directive_options(self) -> str:
        """
        Format options in MyST directive format, using YAML.
        """
        items = self.ref_options.copy()
        for key, value in items.items():
            if not value or _tobool(value):
                items[key] = True
        return "---\n" + yaml.dump(items) + "---\n"


def decode_hyper_options(text: str) -> Dict[str, str]:
    """
    Decode options in {} from `{hyper}` roles.

    {hyper}`Navigate to Tutorial <fts-analyzer> {type=shield,color=darkcyan,logo=Markdown}`
    """
    indata = parse_qs(text, separator=",")
    outdata = {}
    for key, value in indata.items():
        outdata[key] = value[0]
    return outdata


class HyperNavigateRole(HyperRefRole):
    default_options = decode_hyper_options(
        "type=shield,label=Navigate to,message=%(title)s,short-title=true,color=darkcyan"
    )


class HyperOpenRole(HyperRefRole):
    default_options = decode_hyper_options("type=shield,label=Open,message=%(title)s,short-title=true,color=darkblue")


class HyperTutorialRole(HyperRefRole):
    default_options = decode_hyper_options(
        "type=shield,label=Navigate to,message=Tutorial,color=darkcyan,logo=Markdown"
    )


class HyperReadMoreRole(HyperRefRole):
    default_options = decode_hyper_options("type=shield,label=Read More,color=yellow,logo=Markdown")


class HyperReadmeGitHubRole(HyperRefRole):
    default_options = decode_hyper_options("type=shield,message=Open README,color=darkblue,logo=GitHub")


class HyperNotebookColabRole(HyperRefRole):
    default_options = decode_hyper_options(
        "type=shield,label=Open,message=Notebook on Colab,color=blue,logo=Google Colab"
    )


class HyperNotebookBinderRole(HyperRefRole):
    default_options = decode_hyper_options(
        "type=shield,label=Open,message=Notebook on Binder,color=lightblue,logo=binder"
    )


class HyperNotebookGitHubRole(HyperRefRole):
    default_options = decode_hyper_options(
        "type=shield,label=Open,message=Notebook on GitHub,color=darkgreen,logo=GitHub"
    )
