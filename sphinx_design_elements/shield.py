import urllib

from docutils import nodes
from docutils.parsers.rst import directives
from myst_parser.mocking import MockState
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective

from sphinx_design_elements.util.directive import MarkdownWrapper, link_to_markdown

mw = MarkdownWrapper()


def setup_shield(app: Sphinx):
    """
    Set up the `ShieldsDirective` element.
    """
    app.add_directive("shield", ShieldsDirective)


class ShieldsDirective(SphinxDirective):
    """
    Directive to render a badge from https://shields.io.

    <a class="reference internal" href="options.html#fts-options">
        <span class="std std-ref">
            <img alt="Read More" src="https://img.shields.io/badge/Read-More-darkyellow?logo=Markdown">
        </span>
    </a>
    """

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    option_spec = {
        "message": directives.unchanged,
        "message-color": directives.unchanged,
        "label": directives.unchanged,
        "label-color": directives.unchanged,
        "color": directives.unchanged,
        "logo": directives.unchanged,
        "logo-color": directives.unchanged,
        "style": directives.unchanged,
        "link": directives.unchanged,
        "link-type": directives.unchanged,
        "link-title": directives.unchanged,
        "link-alt": directives.unchanged,
    }

    def run(self):
        """Run the directive."""

        quote = urllib.parse.quote

        message = self.options.get("message") or (self.arguments and self.arguments[0])
        message_color = self.options.get("message-color", self.options.get("color")) or "blue"
        label = self.options.get("label")
        label_color = self.options.get("label-color")
        style = self.options.get("style")
        logo = self.options.get("logo")
        logo_color = self.options.get("logo-color")
        link = self.options.get("link")
        link_title = self.options.get("link-title") or message  # TODO: Optionally add label?
        link_alt = self.options.get("link-alt") or link_title

        # Sanity checks.
        if not message:
            raise self.error("Shield must have a message")

        text = encode_shield_text(message)
        if label:
            text = encode_shield_text(label) + "-" + text

        if not text:
            raise self.error("Shield text is empty")

        badge_url = f"https://img.shields.io/badge/{text}-{quote(message_color)}"
        badge_args = {}
        if style:
            badge_args["style"] = style
        if label_color:
            badge_args["labelColor"] = label_color
        if logo:
            badge_args["logo"] = logo
        if logo_color:
            badge_args["logoColor"] = logo_color

        if badge_args:
            badge_url += "?" + urllib.parse.urlencode(badge_args)
        content = f"![{link_alt}]({badge_url})"

        if link:
            content = link_to_markdown(link, content, link_title)

        # When working with rST, parse reference out-of-band using MyST.
        if not isinstance(self.state, MockState):
            return mw.render(content)

        # Native MyST rendering.
        return self.parse_nested(content)

    def parse_nested(self, content: str):
        """
        When using MyST, parse reference within the same parsing context.
        """
        node_ = nodes.Element()
        self.state.nested_parse(content.splitlines(), self.content_offset, node_)
        return node_.children


def encode_shield_text(text: str):
    """
    Encode text fragments for static badge according to its encoding rules.

    https://shields.io/badges/static-badge

    URL input	            Badge output
    ------------------------------------
    Underscore _ or %20	    Space
    Double underscore __	Underscore _
    Double dash --	        Dash -
    """
    return urllib.parse.quote(text).replace("_", "__").replace("-", "--")
