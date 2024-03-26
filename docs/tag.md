(tag-role)=

# Tag


## About

The `tag` and `tags` roles are shortcuts to the `bdg` badge roles of
[sphinx{design}](inv:sd#index), see [](inv:sd#badges).


## Details

The idea is to reduce markup code for defining "tag"-like badges within the
[](#infocard-directive) element. All of them will use the `outline` option flag
by default, to give them a corresponding visual appearance like demonstrated below.

There are two roles: `{tag}` and `{tags}`. A `{tag}` will render its text content
1:1 into a single badge element, while `{tags}` will split the text by comma (`,`),
and renders the outcome using multiple badge elements.


## Synopsis

::::{sd-table}
:widths: 3 3 3 3
:row-class: top-border

:::{sd-row}
```{sd-item} **Description**
```
```{sd-item} **Appearance**
```
```{sd-item} **MyST syntax**
```
```{sd-item} **rST syntax**
```
:::

:::{sd-row}
```{sd-item} Single tag
```
```{sd-item}
{tag}`foo, bar`
```
```{sd-item}
```markdown
{tag}`foo, bar`
```
```{sd-item}
```restructuredtext
:tag:`foo, bar`
```
:::

:::{sd-row}
```{sd-item} Multiple tags
```
```{sd-item}
{tags}`foo, bar`
```
```{sd-item}
```markdown
{tags}`foo, bar`
```
```{sd-item}
```restructuredtext
:tags:`foo, bar`
```
:::

::::


## Color variants

All colors of badges are supported, by appending a color label from the list of
[semantic colors] as a suffix to the role name, like presented below.

::::{sd-table}
:widths: 3 3 6
:row-class: top-border

:::{sd-row}
```{sd-item} **Description**
```
```{sd-item} **Appearance**
```
```{sd-item} **MyST syntax**
```
:::

:::{sd-row}
```{sd-item} Primary and secondary
```
```{sd-item}
{tags-primary}`foo, bar` \
{tags-secondary}`foo, bar`
```
```{sd-item}
```markdown
{tags-primary}`foo, bar` \
{tags-secondary}`foo, bar`
```
:::

:::{sd-row}
```{sd-item} Admonitions
```
```{sd-item}
{tags-success}`foo, bar` \
{tags-info}`foo, bar` \
{tags-warning}`foo, bar` \
{tags-danger}`foo, bar`
```
```{sd-item}
```markdown
{tags-success}`foo, bar` \
{tags-info}`foo, bar` \
{tags-warning}`foo, bar` \
{tags-danger}`foo, bar`
```
:::

:::{sd-row}
```{sd-item}
Light to dark
```
```{sd-item}
{tags-white}`foo, bar` \
{tags-light}`foo, bar` \
{tags-muted}`foo, bar` \
{tags-dark}`foo, bar` \
{tags-black}`foo, bar`
```
```{sd-item}
```markdown
{tags-white}`foo, bar` \
{tags-light}`foo, bar` \
{tags-muted}`foo, bar` \
{tags-dark}`foo, bar` \
{tags-black}`foo, bar`
```
:::

::::

````{note}
While the table above only presents Markdown syntax, reStructuredText syntax is
also supported.

```{eval-rst}
:tag-warning:`REVIEW!`
:tags-primary:`foo, bar`
```

```restructuredtext
:tag-warning:`REVIEW!`
:tags-primary:`foo, bar`
```
````


---

_This page is written in Markedly Structured Text (MyST Markdown)._


[semantic colors]: https://sphinx-design.readthedocs.io/en/latest/css_classes.html#colors
