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


## More examples

:::::{info-card}

::::{grid-item}
:columns: 8
:class: sd-align-major-spaced
#### Curated picture of the day

A mountain goat with long horns standing on a grassy hill.

:::{div} text-small
**Author:** Jaromír Kalina, [@jkalinaofficial](https://unsplash.com/@jkalinaofficial) \
**Contact:** Czech Republic, <https://jkalina.carrd.co/> \
**Exposé:** https://unsplash.com/photos/spdQ1dVuIHw \
**Source:** [Unsplash -- The internet’s source for visuals](https://unsplash.com/)
:::
::::

::::{grid-item}
:columns: 4

[![](https://unsplash.com/photos/spdQ1dVuIHw/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjg5Nzg4MTEzfA&force=true&w=640)](https://unsplash.com/photos/spdQ1dVuIHw)
::::

:::::

:::{note}
Did you ever ask yourself how to [align items in a flex container], and how to control
all those details within Sphinx documentation markup? The documentation about
[using sphinx{design} CSS classes to align flexbox items] has all the answers.
In this case, the items within the left content column are aligned "spaced", to fill the
full major axis, using the `sd-align-major-spaced` CSS class.
:::


---

_This page is written in Markedly Structured Text (MyST Markdown)._


[align items in a flex container]: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Aligning_items_in_a_flex_container
[using sphinx{design} CSS classes to align flexbox items]: https://sphinx-design.readthedocs.io/en/latest/css_classes.html#display
