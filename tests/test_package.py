from verlib2 import Version

import sphinx_design_elements


def test_version():
    assert Version(sphinx_design_elements.__version__) > Version("0.4.0")
