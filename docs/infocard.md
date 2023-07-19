(infocard-directive)=

# Info Card


## About

A composite info card container element, to be used as an item within
a [grid layout](inv:sd#grids). It implements the Sphinx directive `info-card`.


## Details

The info card is a composite element based on nested grid and card components
from [](inv:sd#index). It is suitable to be used as an alternative to tables,
for example when authoring pages enumerating items with dense information,
without the maintenance nightmares of tables.

## Synopsis

::::{info-card}

:::{grid-item}
:columns: 8
[example.org/beagles](https://example.org/beagles)

A module for collecting votes from beagles, \
and for consolidating them.

**Author:** C. Schultz, Universal Features Syndicate \
**Contact:** Los Angeles, CA; <cschultz@peanuts.example.org>
:::

:::{grid-item}
:columns: 4

{tags-primary}`foo, bar`

{tags-success}`baz`

{tags-secondary}`qux`

{tags-info}`anything else`
:::

::::

:::{note}
This example provides a title with link, a formatted description text, and both
verbose and short tags, represented using badges.

For a compact markup to represent the short tag elements, it uses a shortcut notation
based on the corresponding [](#tag-role), for efficiently rendering [sphinx{design}
badges](inv:sd#badges) with a special appearance.
:::


## Usage
````{tab-set-code}
```{literalinclude} ./snippets/myst/infocard.md
:language: markdown
```
```{literalinclude} ./snippets/rst/infocard.rst
:language: rst
```
````


---

_This page is written in Markedly Structured Text (MyST Markdown)._
