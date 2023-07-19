(css-classes)=

# CSS Classes

Additionally to [sphinx{design}](inv:sd#index)'s [](inv:sd#css_classes),
this package provides a few more CSS classes, mostly serving as convenience
shortcuts.
See [`compiled/style.css`] for inspecting the whole CSS rule file.


## Font sizes

The `.text-{small,smaller,medium,larger,large}` CSS classes exclusively adjust the
`font-size` CSS attribute. They can be used anywhere.

:::{card}
```{div} text-small
Small text.
```
```{div} text-smaller
Smaller text.
```
```{div} text-medium
Medium text.
```
```{div} text-large
Large text.
```
```{div} text-larger
Larger text.
```
:::


## Table styling

The `.{top,bottom}-border` CSS classes adjust the `border-{top,bottom}-{width,style,color}`
CSS attributes. They are meant to be applied to rows in a [](gridtable-directive) by using
its `:row-class:` directive option.

:::::{card}
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
:::::

[`compiled/style.css`]: https://github.com/panodata/sphinx-design-elements/blob/main/sphinx_design_elements/compiled/style.css
