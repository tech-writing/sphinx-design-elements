import typing as t

from docutils import nodes
from sphinx.application import Sphinx
from sphinx_design.badges_buttons import BadgeRole, create_bdg_classes
from sphinx_design.shared import SEMANTIC_COLORS


def setup_tags(app: Sphinx) -> None:
    """
    Set up the tag(s) shortcut roles.

    Tag shortcut roles are rendering sphinx-design "badge" components
    using a specific visual appearance.
    """
    app.add_role("tag", BadgeRole("primary", outline=True))
    app.add_role("tags", MultipleBadgeRole("primary", outline=True))
    for color in SEMANTIC_COLORS:
        app.add_role(
            "-".join(("tag", color)),
            BadgeRole(color, outline=True),
        )
        app.add_role(
            "-".join(("tags", color)),
            MultipleBadgeRole(color, outline=True),
        )


class MultipleBadgeRole(BadgeRole):
    """
    A Sphinx role displaying multiple sphinx-design "badge" components.

    Synopsis MyST:

        {tags-primary}`foo, bar`

    Synopsis rST:

        :tags-primary:`foo, bar`
    """

    def decode_input_text(self) -> t.List[str]:
        """
        Decode input text, splitting by comma.
        """
        return list(map(str.strip, self.text.split(",")))

    def run(self) -> t.Tuple[t.List[nodes.Node], t.List[nodes.system_message]]:
        """
        Run the role, rendering multiple "badge" nodes.
        """
        elements: t.List[nodes.Node] = []

        # Enumerate multiple items.
        for text in self.decode_input_text():
            # Add one node per item.
            node = nodes.inline(
                self.rawtext,
                text,
                classes=create_bdg_classes(self.color, self.outline),
            )
            self.set_source_info(node)
            elements.append(node)

            # Add spacer node.
            spacer = nodes.inline(" ", " ")
            elements.append(spacer)

        # Remove last spacer again.
        if elements:
            elements.remove(elements[-1])
        return elements, []
