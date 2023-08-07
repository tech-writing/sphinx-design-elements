# Dropdown Group


## About

This is an extension to [sphinx-design dropdowns], intending to implement a
similar behavior like [using CSS `toggle-group` to group exclusive toggles].

If you have multiple dropdown elements, you can group them together, in order
to make only one toggle from the group active at a time, effectively defining
exclusive dropdowns.

This is similar to how HTML radio buttons behave, where two buttons cannot be
checked at the same time.


## Usage

In order define a group of multiple dropdown elements that should exclusively
open when toggled, wrap them into a container element using the `dropdown-group`
class.

````{tab-set-code}
```{literalinclude} ./snippets/myst/dropdown-group.md
:language: markdown
```
```{literalinclude} ./snippets/rst/dropdown-group.rst
:language: rst
```
````


## Example

::::{div} dropdown-group

:::{dropdown} Dropdown A
Dropdown content A
:::

:::{dropdown} Dropdown B
Dropdown content B
:::

::::


[sphinx-design dropdowns]: https://sphinx-design.readthedocs.io/en/latest/dropdowns.html
[using CSS `toggle-group` to group exclusive toggles]: https://blog.logrocket.com/advanced-guide-css-toggle-pseudo-class/#using-toggle-group-exclusive-toggles
