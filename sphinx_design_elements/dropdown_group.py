from sphinx.application import Sphinx


def setup_dropdown_group(app: Sphinx):
    """
    Add JavaScript for defining exclusive dropdown elements using the `dropdown-group` class.
    """
    dropdown_js = """
    """
    app.add_js_file(None, body=dropdown_js)
