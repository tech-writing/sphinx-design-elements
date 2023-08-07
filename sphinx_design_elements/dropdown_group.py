from sphinx.application import Sphinx


def setup_dropdown_group(app: Sphinx):
    """
    Add JavaScript for defining exclusive dropdown elements using the `dropdown-group` class.
    """
    dropdown_js = """

    // Select all relevant detail elements nested within container elements using the `dropdown-group` class.
    const dropdown_details = document.querySelectorAll(".dropdown-group details");

    // Add event listener for special toggling.
    dropdown_details.forEach((details) => {
      details.addEventListener("toggle", toggleOpenGroup);
    });

    // When toggling elements, exclusively open one element, and close all others.
    function toggleOpenGroup(e) {
      if (this.open) {
        dropdown_details.forEach((details) => {
          if (details != this && details.open) {
            details.open = false;
          }
        });
      }
    }
    """
    app.add_js_file(None, body=dropdown_js)
