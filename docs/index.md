---
sd_hide_title: true
---

# sphinx-design

::::::{div} landing-title
:style: "padding: 0.6rem 0.1rem 0.1rem 0; background-image: linear-gradient(315deg, #992d3b 0%, #303545 84%); clip-path: polygon(0px 0px, 100% 0%, 100% calc(100% - 1.5rem), 0% 100%); -webkit-clip-path: polygon(0px 0px, 100% 0%, 100% calc(100% - 1.5rem), 0% 100%);"

::::{grid}
:reverse:
:gutter: 2 3 3 3
:margin: 4 4 1 2

:::{grid-item}
:columns: 12 4 4 4
:::

:::{grid-item}
:columns: 12 8 8 8
:child-align: justify
:class: sd-text-white sd-fs-3

A collection of composite web elements based on [![img][sphinx-design-logo]{w=200px}][sphinx-design].


```{button-ref} get_started
:ref-type: doc
:outline:
:color: white
:class: sd-px-4 sd-fs-5

Get Started
```

:::
::::

::::::

Building upon sphinx-design
: [sphinx-design] is a Sphinx extension for designing beautiful, screen-size
  responsive web-components. It is inspired by the [Bootstrap], [Material Design],
  and [Material-UI] design frameworks, and is the foundation for all composite
  elements in this collection.

Works with reStructuredText (rST) and Markedly Structured Text (MyST)
: Either write documentation using the venerable [reStructuredText], or use the
  new extended [Markdown]/[CommonMark] syntax [Markedly Structured Text]. Both
  are supported equally well.

Less markup
: You can do everything what [sphinx-design] can do, but with less markup code,
  so you can better focus on content instead of design and style details.

Sandbox and incubator
: [sphinx-design-elements] intends to provide a sandbox and incubation environment
  for all details currently beyond the scope of [sphinx-design], and is very open
  to receive further contributions in the same area.

```{toctree}
:hidden:

README <readme>
get_started
```

```{toctree}
:caption: Development
:hidden:

project
changes
sandbox
```


::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`table` Placeholder
:::

::::

-----------

Kudos to [Chris Sewell] and all contributors for conceiving and maintaining
[MyST Parser] and [sphinx-design]. 


[Bootstrap]: https://getbootstrap.com/
[Chris Sewell]: https://github.com/chrisjsewell
[CommonMark]: https://spec.commonmark.org/
[Markdown]: https://daringfireball.net/projects/markdown/syntax
[Markedly Structured Text]: https://myst-parser.readthedocs.io/
[Material Design]: https://material.io
[Material-UI]: https://material-ui.com/
[MyST Parser]: https://myst-parser.readthedocs.io/
[reStructuredText]: https://docutils.sourceforge.io/rst.html
[sphinx-design]: https://sphinx-design.readthedocs.io/
[sphinx-design-logo]: https://sphinx-design.readthedocs.io/en/latest/_static/logo_wide.svg
[sphinx-design-elements]: https://sphinx-design-elements.readthedocs.io/
