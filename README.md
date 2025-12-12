# sphinx-design-elements

» [Documentation]
| [Changelog]
| [PyPI]
| [Issues]
| [Source code]
| [License]

[![CI][badge-tests]][project-tests]
[![Coverage Status][badge-coverage]][project-codecov]
[![License][badge-license]][project-license]
[![Downloads per month][badge-downloads-per-month]][project-downloads]

[![Supported Python versions][badge-python-versions]][project-pypi]
[![Supported Sphinx versions][badge-sphinx-versions]][project-sphinx]
[![Status][badge-status]][project-pypi]
[![Package version][badge-package-version]][project-pypi]


## About

A collection of composite and convenience web elements based on components
from [sphinx-design].


## Setup

Install the package using `pip install sphinx-design-elements`, and add the
extension to the list of `extensions` within your Sphinx configuration file
`conf.py`.

```python
extensions = [
    "sphinx_design",
    "sphinx_design_elements",
]
```

## Development

In order to learn how to set up a development sandbox, please visit the
[development documentation].


## Comparison to sphinx-design

[sphinx-design-elements] uses low-level components of [sphinx-design],
in order to build more high-level elements on top.


## Acknowledgements

Kudos to [Chris Sewell], [Chris Holdgraf], and all contributors for conceiving
and maintaining [MyST Parser] and [sphinx-design].



[Changelog]: https://github.com/tech-writing/sphinx-design-elements/blob/main/CHANGES.md
[Chris Holdgraf]: https://github.com/choldgraf
[Chris Sewell]: https://github.com/chrisjsewell
[development documentation]: https://sphinx-design-elements.readthedocs.io/en/latest/sandbox.html
[Documentation]: https://sphinx-design-elements.readthedocs.io/
[Issues]: https://github.com/tech-writing/sphinx-design-elements/issues
[License]: https://github.com/tech-writing/sphinx-design-elements/blob/main/LICENSE
[MyST Parser]: https://myst-parser.readthedocs.io/
[PyPI]: https://pypi.org/project/sphinx-design-elements/
[Source code]: https://github.com/tech-writing/sphinx-design-elements
[sphinx-design]: https://sphinx-design.readthedocs.io/
[sphinx-design-elements]: https://sphinx-design-elements.readthedocs.io/

[badge-coverage]: https://codecov.io/gh/tech-writing/sphinx-design-elements/branch/main/graph/badge.svg
[badge-downloads-per-month]: https://pepy.tech/badge/sphinx-design-elements/month
[badge-license]: https://img.shields.io/github/license/tech-writing/sphinx-design-elements.svg
[badge-package-version]: https://img.shields.io/pypi/v/sphinx-design-elements.svg
[badge-python-versions]: https://img.shields.io/pypi/pyversions/sphinx-design-elements.svg
[badge-sphinx-versions]: https://img.shields.io/badge/sphinx-5.1%20--%208.*-blue.svg
[badge-status]: https://img.shields.io/pypi/status/sphinx-design-elements.svg
[badge-tests]: https://github.com/tech-writing/sphinx-design-elements/actions/workflows/main.yml/badge.svg
[project-codecov]: https://codecov.io/gh/tech-writing/sphinx-design-elements
[project-downloads]: https://pepy.tech/project/sphinx-design-elements/
[project-license]: https://github.com/tech-writing/sphinx-design-elements/blob/main/LICENSE
[project-pypi]: https://pypi.org/project/sphinx-design-elements
[project-sphinx]: https://www.sphinx-doc.org/
[project-tests]: https://github.com/tech-writing/sphinx-design-elements/actions/workflows/main.yml
