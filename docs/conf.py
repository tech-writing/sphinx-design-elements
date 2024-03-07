"""Configuration file for the Sphinx documentation builder."""

import os

project = "Sphinx Design Elements"
copyright = "2023, Panodata Developers"  # noqa: A001
author = "Panodata Developers"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_design_elements",
    "sphinx.ext.intersphinx",
]

html_theme = os.environ.get("SPHINX_THEME", "furo")
html_title = "sphinx-design-elements"
# html_title = f"Sphinx Design Elements ({html_theme.replace('_', '-')})"

html_static_path = ["_static"]
# html_logo = "_static/logo_wide.svg"
# html_favicon = "_static/logo_square.svg"

# if html_theme not in ("sphinx_book_theme", "pydata_sphinx_theme"):
#    html_css_files = [
#        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
#    ]
if False and html_theme == "furo":
    html_css_files = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/fontawesome.min.css"]
    html_theme_options = {
        "sidebar_hide_name": False,
    }

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
myst_enable_extensions = [
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_substitutions = {}

# Configure Sphinx-copybutton
copybutton_remove_prompts = True
copybutton_line_continuation_character = "\\"
copybutton_prompt_text = r">>> |\.\.\. |\$ |sh\$ |PS> |cr> |mysql> |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# Configure Intersphinx
intersphinx_mapping = {
    "sd": ("https://sphinx-design.readthedocs.io/en/latest/", None),
    "myst": ("https://myst-parser.readthedocs.io/en/latest/", None),
}
