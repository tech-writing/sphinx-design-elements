(gridtable-directive)=

# Grid Table


## About

_sd-table -- Tables with sphinx{design}_.

A generic, beautiful, yet efficient table element based on a [grid layout](inv:sd#grids),
with top-down configuration capabilities.

It provides the Sphinx directives `sd-table`, `sd-row`, and `sd-item`,
and a few convenience directive options and flags on them.


## Details

The idea of this element is to implement a table based on a grid layout, which can
be parameterized using directives on the table level, so that styling details will
not clutter the leaf nodes (row and item) too much.

To goal is to provide a table element as an alternative to the `list-table` and
`csv-table` directives, which explores a few needs of authors not offered by
other Sphinx directives.


## Synopsis

Basic table, two columns, no formatting.

::::{sd-table}
:widths: 3 9

:::{sd-row}
```{sd-item} **What**
```
```{sd-item} **Description**
```
:::

:::{sd-row}
```{sd-item} Fox
```
```{sd-item}
The quick brown fox jumps
over the lazy dog.
```
:::
:::{sd-row}
```{sd-item} Franz
```
```{sd-item}
Franz jagt im komplett verwahrlosten
Taxi quer durch Bayern.
```
:::

::::


## Usage

sphinx{design} uses a classic 12-column grid layout, so, in order to use
it optimally, make sure that your table item/column widths sum up to 12.

The example table defines two columns, using individual widths of `3` and `9`.

````{tab-set-code}
```{literalinclude} ./snippets/myst/gridtable.md
:language: markdown
```
```{literalinclude} ./snippets/rst/gridtable.rst
:language: rst
```
````


## Variants

A few more variants how to change the visual appearance.

### Visual line separators

Using `:row-class:` to assign row-level styles on the table-level component.

::::{sd-table}
:widths: 3 9
:row-class: top-border

:::{sd-row}
```{sd-item} **What**
```
```{sd-item} **Description**
```
:::

:::{sd-row}
```{sd-item} Fox
```
```{sd-item}
The quick brown fox jumps
over the lazy dog.
```
:::
:::{sd-row}
```{sd-item} Franz
```
```{sd-item}
Franz jagt im komplett verwahrlosten
Taxi quer durch Bayern.
```
:::

::::


### Outlines

This section demonstrates different kinds of outlines, on different component levels.

#### Table outline

Using the `:outline:` directive flag will draw a single border around the whole **table**.

```markdown
::::{sd-table}
:outline:
```

::::{sd-table}
:widths: 3 9
:outline:

:::{sd-row}
```{sd-item} **What**
```
```{sd-item} **Description**
```
:::

:::{sd-row}
```{sd-item} Fox
```
```{sd-item}
The quick brown fox jumps
over the lazy dog.
```
:::
:::{sd-row}
```{sd-item} Franz
```
```{sd-item}
Franz jagt im komplett verwahrlosten
Taxi quer durch Bayern.
```
:::

::::


#### Row outline

Using the `:row-outline:` directive flag will draw borders around each **row** component.

```markdown
::::{sd-table}
:row-outline:
```

::::{sd-table}
:widths: 3 9
:row-outline:

:::{sd-row}
```{sd-item} **What**
```
```{sd-item} **Description**
```
:::

:::{sd-row}
```{sd-item} Fox
```
```{sd-item}
The quick brown fox jumps
over the lazy dog.
```
:::
:::{sd-row}
```{sd-item} Franz
```
```{sd-item}
Franz jagt im komplett verwahrlosten
Taxi quer durch Bayern.
```
:::

::::


#### Item outline

Using the `:item-outline:` directive flag will draw borders around each **item** component.

```markdown
::::{sd-table}
:item-outline:
```

::::{sd-table}
:widths: 3 9
:item-outline:

:::{sd-row}
```{sd-item} **What**
```
```{sd-item} **Description**
```
:::

:::{sd-row}
```{sd-item} Fox
```
```{sd-item}
The quick brown fox jumps
over the lazy dog.
```
:::
:::{sd-row}
```{sd-item} Franz
```
```{sd-item}
Franz jagt im komplett verwahrlosten
Taxi quer durch Bayern.
```
:::

::::


---

_This page is written in Markedly Structured Text (MyST Markdown)._
