(getting-started)=

# Getting Started

```{article-info}
:author: "[The Tech Writing Developers](https://github.com/tech-writing)"
:date: "{sub-ref}`today`"
:read-time: "1 min read"
```


## Setup

The basic installation supports documentation authoring using the [reStructuredText] (rST)
syntax. You can optionally support an extended [Markdown] syntax by installing and enabling
the [Markedly Structured Text] (MyST) extension.

### Use reStructuredText

Install the package.
```shell
pip install sphinx-design-elements
```

Then, add the extension item `sphinx_design_elements` to the list of
`extensions` within your [Sphinx] configuration file `conf.py`.

```python
extensions = [
    "sphinx_design",
    "sphinx_design_elements",
]
```


### Use Markedly Structured Text

Install the packages.
```shell
pip install myst-parser sphinx-design-elements
```

Then, add the extension items `myst_parser` and `sphinx_design_elements` to the list
of `extensions` within your [Sphinx] configuration file `conf.py`.
When using `sphinx-design-elements` with MyST, it is also recommended to enable the
`colon_fence` syntax extension.

```python
extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_design_elements",
]
myst_enable_extensions = [
    "colon_fence",
]
```


## Usage

Head over to the "directives" and "roles" sections to learn about the web elements
provided by this collection, and how to use them in your documentation markup.

- [](#gridtable-directive)
- [](#infocard-directive)
- [](#linktree-directive)
- [](#tag-role)

Both [reStructuredText] and [Markedly Structured Text] syntax are supported equally well.

## Outlook

Feedback and feature requests about the provided elements are always welcome.
If you see ways to improve them, or want to add a few of your own elements you
would like to share with others, do not hesitate to submit patches, in order to
add them to the collection.


[Markdown]: https://daringfireball.net/projects/markdown/syntax
[Markedly Structured Text]: https://myst-parser.readthedocs.io/
[reStructuredText]: https://docutils.sourceforge.io/rst.html
[Sphinx]: https://www.sphinx-doc.org/
