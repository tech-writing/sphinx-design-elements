import typing as t
from typing import List

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx_design.grids import item_columns_option
from sphinx_design.shared import create_component, margin_option, padding_option


def setup_gridtable(app: Sphinx):
    """
    Set up the `TableDirective`, `RowDirective`, and `ItemDirective`.
    """
    app.add_directive("sd-table", TableDirective)
    app.add_directive("sd-row", RowDirective)
    app.add_directive("sd-item", ItemDirective)


margin_padding_classes = [margin_option("0")[0], padding_option("0")[0]]


def widths_option(
    argument: t.Optional[str],
) -> List[str]:
    """
    Column widths. Each column width is an integer value between 1 and 12.

    TODO: Validate the value range and the number of columns.
    """
    if argument is None:
        return []
    values = argument.strip().split()
    return values


class TableDirective(SphinxDirective):
    """
    A composite element offering a title, description text, and both verbose and short tags.
    It is suitable for authoring pages enumerating items with dense information, without
    the maintenance nightmares of tables.
    """

    has_content = True
    required_arguments = 0
    optional_arguments = 1
    option_spec = {
        "item-outline": directives.flag,
        "outline": directives.flag,
        "row-class": directives.class_option,
        "row-outline": directives.flag,
        "widths": widths_option,
    }

    def run(self) -> List[nodes.Node]:
        self.state_machine.document.attributes["widths"] = self.options.get("widths", [])
        self.state_machine.document.attributes["row-class"] = self.options.get("row-class", [])
        if "row-outline" in self.options:
            self.state_machine.document.attributes["row-outline"] = None
        if "item-outline" in self.options:
            self.state_machine.document.attributes["item-outline"] = None

        grid_classes = ["sd-container-fluid", "sd-sphinx-override"]
        grid_container = create_component(
            "grid-container",
            grid_classes
            + margin_padding_classes
            + (["sd-border-1"] if "outline" in self.options else [])
            + self.options.get("class-container", []),
        )
        self.set_source_info(grid_container)
        self.state.nested_parse(self.content, self.content_offset, grid_container)
        return [grid_container]


class RowDirective(SphinxDirective):
    """
    The "row" element of the `TableDirective`.
    """

    has_content = True
    option_spec = {
        "outline": directives.flag,
    }

    def run(self) -> List[nodes.Node]:
        if "row-outline" in self.state_machine.document.attributes:
            self.options["outline"] = None

        grid_row = create_component(
            "grid-row",
            ["sd-row"]
            + margin_padding_classes
            + self.options.get("gutter", [])
            + (["sd-flex-row-reverse"] if "reverse" in self.options else [])
            + (["sd-border-1"] if "outline" in self.options else [])
            + self.state_machine.document.attributes["row-class"]
            + self.options.get("row-class", []),
        )
        self.state_machine.document.attributes["row"] = grid_row
        grid_row.parent = self.state_machine.node
        self.set_source_info(grid_row)
        self.state.nested_parse(self.content, self.content_offset, grid_row)

        # Apply widths.
        widths = t.cast("t.Iterable[str]", self.state_machine.document.attributes.get("widths"))
        for column, width in zip(grid_row.children, widths):
            element = t.cast("nodes.Element", column)
            element.update_basic_atts({"classes": item_columns_option(width)})

        return [grid_row]


class ItemDirective(SphinxDirective):
    """
    The "item" (cell) element of the `TableDirective`.

    It is intended to be used nested within a `RowDirective`.
    """

    has_content = True
    option_spec = {
        "child-align": directives.unchanged,
        "child-direction": directives.unchanged,
        "class": directives.class_option,
        "columns": directives.unchanged,
        "margin": directives.unchanged,
        "outline": directives.flag,
        "padding": directives.unchanged,
    }

    def run(self) -> List[nodes.Node]:
        if "item-outline" in self.state_machine.document.attributes:
            self.options["outline"] = None

        column = create_component(
            "grid-item",
            [
                "sd-col",
                f"sd-d-flex-{self.options.get('child-direction', 'column')}",
            ]
            + self.options.get("columns", [])
            + self.options.get("margin", [])
            + self.options.get("padding", [])
            + ([f'sd-align-major-{self.options["child-align"]}'] if "child-align" in self.options else [])
            + (["sd-border-1"] if "outline" in self.options else [])
            + self.options.get("class", []),
        )
        column.parent = self.state_machine.node
        self.set_source_info(column)
        self.state.nested_parse(self.content, self.content_offset, column)
        return [column]
