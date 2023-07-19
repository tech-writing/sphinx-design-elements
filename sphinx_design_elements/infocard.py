from typing import Dict, List, Tuple

from docutils import nodes
from docutils.statemachine import StringList
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx_design.cards import CardDirective
from sphinx_design.shared import create_component, margin_option, padding_option


def setup_infocard(app: Sphinx):
    """
    Set up the `InfoCardDirective` composite web element.
    """
    app.add_directive("info-card", InfoCardDirective)


class GridBuilderDirective(SphinxDirective):
    """
    Helper functions for the `InfoCardDirective` to create grids and cards.
    """

    def create_grid(self) -> Tuple[nodes.container, nodes.container]:
        """
        Create a "grid layout" using sphinx-design components.

        Return its outer and inner `docutils.container` instances.
        """
        margin_padding_classes = [margin_option("0")[0], padding_option("0")[0]]

        grid_classes = ["sd-container-fluid", "sd-sphinx-override"]
        grid_container = create_component(
            "grid-container",
            grid_classes
            + margin_padding_classes
            + (["sd-border-1"] if "outline" in self.options else [])
            + self.options.get("class-container", []),
        )
        self.set_source_info(grid_container)
        grid_row = create_component(
            "grid-row",
            ["sd-row"]
            + margin_padding_classes
            + self.options.get("gutter", [])
            + (["sd-flex-row-reverse"] if "reverse" in self.options else [])
            + self.options.get("class-row", []),
        )
        self.set_source_info(grid_row)
        grid_container += grid_row
        return grid_container, grid_row

    def create_card(self) -> Tuple[nodes.container, nodes.container]:
        """
        Create a sphinx-design "card" component.

        Return its outer and inner `docutils.container` instances.
        """
        card = CardDirective(
            # FIXME: Need to assign random name?
            name="sdroot",
            arguments=self.arguments,
            options=self.options,
            content=StringList(None),
            lineno=self.lineno,
            content_offset=self.content_offset,
            block_text=self.block_text,
            state=self.state,
            state_machine=self.state_machine,
        )

        # TODO: Can process this differently?
        card_node = card.run()[0]
        self.set_source_info(card_node)

        card_body = card_node.children[0]
        self.set_source_info(card_body)
        return card_node, card_body


class InfoCardDirective(GridBuilderDirective):
    """
    A composite info card container element, offering a title, description text, and both
    verbose and short tags.

    It is suitable for authoring pages enumerating items with dense information, without
    the maintenance nightmares of tables.
    """

    has_content = True
    required_arguments = 0
    optional_arguments = 1
    option_spec: Dict[str, str] = {}

    def run(self) -> List[nodes.Node]:
        # Create a canvas grid.
        root, canvas = self.create_grid()

        # Create a card, and add it to the canvas.
        card, card_body = self.create_card()
        canvas += card

        # Create a content grid, and add it to the card.
        content_outer, content_inner = self.create_grid()
        self.set_source_info(content_outer)
        card_body += content_outer

        # Parse the node content, assuming grid items, and add them to the content grid.
        self.state.nested_parse(self.content, self.content_offset, content_inner)
        self.set_source_info(content_inner)

        # Return a reference to the root node.
        return [root]
