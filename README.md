# sphinx-design-elements

» [Documentation]
| [Changelog]
| [PyPI]
| [Issues]
| [Source code]
| [License]

[![CI][gha-badge]][gha-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![PyPI][pypi-badge]][pypi-link]


## About

A collection of composite web elements based on components from [sphinx-design].


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

## Comparison to sphinx-design

This package uses low-level components of [sphinx-design], in order to build more
high-level elements on top.


## Development



[Changelog]: https://github.com/panodata/sphinx-design-elements/blob/main/CHANGES.md
[Documentation]: https://sphinx-design-elements.readthedocs.io/
[Issues]: https://github.com/panodata/sphinx-design-elements/issues
[License]: https://github.com/panodata/sphinx-design-elements/blob/main/LICENSE
[PyPI]: https://pypi.org/project/sphinx-design-elements/
[Source code]: https://github.com/panodata/sphinx-design-elements
[sphinx-design]: https://sphinx-design.readthedocs.io/

[gha-badge]: https://github.com/panodata/sphinx-design-elements/actions/workflows/main.yml/badge.svg
[gha-link]: https://github.com/panodata/sphinx-design-elements/actions/workflows/main.yml
[codecov-badge]: https://codecov.io/gh/panodata/sphinx-design-elements/branch/main/graph/badge.svg
[codecov-link]: https://codecov.io/gh/panodata/sphinx-design-elements
[pypi-badge]: https://img.shields.io/pypi/v/sphinx-design-elements.svg
[pypi-link]: https://pypi.org/project/sphinx-design-elements
