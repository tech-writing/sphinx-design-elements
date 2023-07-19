(infocard-directive)=

# Info Card


## About

A composite info card container element, to be used as an item within
a [grid layout](inv:sd#grids). It provides the Sphinx directive `info-card`.


## Details

The info card is a composite element offering a title, description text, and
both verbose and short tags. It is suitable for authoring pages enumerating
items with dense information, without the maintenance nightmares of tables.

For a compact notation of the short tag elements, it uses the corresponding
[](#tag-role) for efficiently rendering [](inv:sd#badges), which is also
provided by this package.


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


## Usage
````{tab-set-code}
```{literalinclude} ./snippets/myst/infocard.md
:language: markdown
```
```{literalinclude} ./snippets/rst/infocard.rst
:language: rst
```
````


_This page is written in Markedly Structured Text (MyST Markdown)._
