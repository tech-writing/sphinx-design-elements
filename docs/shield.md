(shield-directive)=

# Shield


## About

A component to render badges through [Shields.io], with or without links,
and optional parameterization. It implements the Sphinx directive `shield`.


## Details

The `shield` directive supports the options provided by [Shields.io Static Badges].

(shield-message)=
:message:
    The text on the right hand side of the shield. When no label is defined,
    the shield will only include the message text.

(shield-label)=
:label:
    The optional text on the left hand side of the shield.

(shield-logo)=
:logo:
    One of the named logos (bitcoin, dependabot, gitlab, npm, paypal,
    serverfault, stackexchange, superuser, telegram, travis), or one
    of [Simple Icons]. All simple icons are referenced using [icon slugs].
    For general documentation, see also [Shields.io Logos].

(shield-style)=
:::{rubric} Style
:::
:style:
    The style of the shield, `flat` by default. Possible values: `flat`,
    `flat-square`, `plastic`, `for-the-badge`, `social`.

(shield-color)=
:::{rubric} Colors
:::

For the colors, hex, rgb, rgba, hsl, hsla and css named colors supported.
**Formats:** `rgb(r,g,b)` / `rgba(r,g,b,a)` and `hsl(h,s,l)` /
`hsla(h,s,l,a)`.

:message-color:
    Background color of the right part. When no label is defined,
    the shield will be single-colored. When not defining a color,
    the default is `blue`.

:label-color:
    Background color of the left part.

:logo-color:
    The background color of the logo. Supported for named logos and Shields
    logos, but not for custom logos.

:color:
    An alias for `message-color`.    

:::{seealso}
- https://github.com/badges/shields/tree/master/badge-maker#colors
- https://github.com/badges/shields/discussions/7128
:::


(shield-linking)=
:::{rubric} Linking
:::
Optionally, for using a shield to navigate to a reference (local, indirect,
intersphinx, page), or URL, the component will also accept those options.

:link:
    Either a Sphinx reference, supporting different formats, or an URL.

:link-type:
    The link type: `doc`, `ref` (local and intersphinx), or `url`.

:link-title:
    Slightly supported option to adjust the link title, mostly displayed
    as a tooltip.


## Synopsis

A static shield badge linking to a URL, defined using the markup outlined below.

::::{card}

:::{shield}
:label: Example
:message: Shield
:color: darkcyan
:logo: Markdown
:link: https://example.org/
:link-type: url
:link-title: An example using the shield directive
:::

::::


## Usage
::::{tab-set-code}
:::{literalinclude} ./snippets/myst/shield.md
:language: markdown
:::
:::{literalinclude} ./snippets/rst/shield.rst
:language: rst
:::
::::


## Variants

A few more variants how to change the visual appearance.

The following examples just enumerate variants in MyST syntax. Modulo some
specific features, it should work roughly the same way when using rST.

:::::::{sd-table}
:widths: 2 6 4
:row-class: col-compact

:::{rubric} Basics
:::

Fundamental features of the `shield` directive, about basic text
and layout options, and configuration styles.

::::::{sd-row}
:::::{sd-item} **Item**
:::::
:::::{sd-item} **Description**
:::::
:::::{sd-item} **Syntax**
:::::
::::::

::::::{sd-row}
:::::{sd-item}
::::{shield} Read More
::::
:::::
:::::{sd-item}
A basic shield without any options.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield} Read More
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: Read More
:::
:::::
:::::{sd-item}
The message can also be defined using the [`message`](#shield-message) option.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: Read More
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:label: Read
:message: More
:::
:::::
:::::{sd-item}
Left vs. right texts can be defined by using the [`label`](#shield-label)
vs. [`message`](#shield-message) options.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:label: Read
:message: More
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
---
message: "Read More"
:::
:::::
:::::{sd-item}
When using MyST, options can also be defined in YAML syntax,
which also allows to use multi-line values.
:::::
:::::{sd-item}
YAML
::::{code} markdown

:::{shield}
---
message: "Read More"
:::
::::
Multi-line
::::{code} markdown

:::{shield}
---
message: |
    Read
    More
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: 🌻 Read More 🍀
:::
:::::
:::::{sd-item}
Text input also accepts Unicode glyphs.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: 🌻 Read More 🍀
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
::::{div} inline

:::{shield} S 1
:::
:::{shield} S 2
:::
::::
:::::
:::::{sd-item}
By default, `shield` directives render as block-level elements.
To place multiple items side by side, in order to display them
inline, wrap them into a `::::{div} inline` colon fence. 
:::::
:::::{sd-item}
````{code} markdown

::::{div} inline

:::{shield} S 1
:::

:::{shield} S 2
:::

::::
````
:::::
::::::



:::{rubric} Styling
:::

About defining colors, an icon, and the style/shape of the shield.

::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: Read More
:color: darkgreen
:::
:::::
:::::{sd-item}
The `color` option determines the background color.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: Read More
:color: darkgreen
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:label: Read
:message: More
:label-color: darkgreen
:message-color: orange
:::
:::{shield}
:label: Read
:message: More
:label-color: hsl(270,60%,70%)
:message-color: rgb(255,0,153)
:::
:::{shield} Read More
:color: "#123456"
:::
:::::
:::::{sd-item}
Left vs. right background colors can be defined by using the `label-color`
vs. `message-color` options, see [](#shield-color). For single-colored shields,
the `color` option can be used as an alias for `message-color`.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:label: Read
:message: More
:label-color: darkgreen
:message-color: orange
:::

:::{shield}
:label: Read
:message: More
:label-color: hsl(270,60%,70%)
:message-color: rgb(255,0,153)
:::

:::{shield} Read More
:color: #123456
:::

::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: CrateDB
:logo: CrateDB
:color: gray
:::
:::::
:::::{sd-item}
Select an image from a collection of brand depictions, using the
[`logo`](#shield-logo) option.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: CrateDB
:logo: CrateDB
:color: gray
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: PS Controller
:logo: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEiIHdpZHRoPSI2MDAiIGhlaWdodD0iNjAwIj48cGF0aCBkPSJNMTI5IDExMWMtNTUgNC05MyA2Ni05MyA3OEwwIDM5OGMtMiA3MCAzNiA5MiA2OSA5MWgxYzc5IDAgODctNTcgMTMwLTEyOGgyMDFjNDMgNzEgNTAgMTI4IDEyOSAxMjhoMWMzMyAxIDcxLTIxIDY5LTkxbC0zNi0yMDljMC0xMi00MC03OC05OC03OGgtMTBjLTYzIDAtOTIgMzUtOTIgNDJIMjM2YzAtNy0yOS00Mi05Mi00MmgtMTV6IiBmaWxsPSIjZmZmIi8+PC9zdmc+
:::
:::::
:::::{sd-item}
Use a custom [`logo`](#shield-logo) image by base64 encoding it.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: Play Station
:logo: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEiIHdpZHRoPSI2MDAiIGhlaWdodD0iNjAwIj48cGF0aCBkPSJNMTI5IDExMWMtNTUgNC05MyA2Ni05MyA3OEwwIDM5OGMtMiA3MCAzNiA5MiA2OSA5MWgxYzc5IDAgODctNTcgMTMwLTEyOGgyMDFjNDMgNzEgNTAgMTI4IDEyOSAxMjhoMWMzMyAxIDcxLTIxIDY5LTkxbC0zNi0yMDljMC0xMi00MC03OC05OC03OGgtMTBjLTYzIDAtOTIgMzUtOTIgNDJIMjM2YzAtNy0yOS00Mi05Mi00MmgtMTV6IiBmaWxsPSIjZmZmIi8+PC9zdmc+
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: Read More
:style: flat
:::
:::{shield}
:message: Read More
:style: flat-square
:::
:::{shield}
:message: Read More
:style: plastic
:::
:::{shield}
:message: Read More
:style: for-the-badge
:::
:::{shield}
:message: Read More
:style: social
:::
:::::
:::::{sd-item}
The [`style`](#shield-style) option determines the style / shape of the shield.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: Read More
:style: flat
:::

:::{shield}
:message: Read More
:style: flat-square
:::

:::{shield}
:message: Read More
:style: plastic
:::

:::{shield}
:message: Read More
:style: for-the-badge
:::

:::{shield}
:message: Read More
:style: social
:::

::::
:::::
::::::


:::{rubric} Linking
:::

How to use the shield as a hypertext reference to link to other resources.
See also complete [linking options](#shield-linking).

::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: Sandbox
:link: sandbox
:link-type: doc
:::
:::::
:::::{sd-item}
Link to a Sphinx document using the `link-type=doc` option.
In this case, `link` refers to a document name.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: Sandbox
:link: sandbox
:link-type: doc
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: Linking
:link: shield-linking
:link-type: ref
:::
:::::
:::::{sd-item}
Link to a Sphinx reference using the `link-type=ref` option.
In this case, `link` refers to any local Sphinx reference.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: Linking
:link: shield-linking
:link-type: ref
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: sphinx{design}
:link: sd:index
:link-type: ref
:::
:::::
:::::{sd-item}
Link to another project using the `link-type=ref` option.
In this case, `link` refers to an intersphinx reference.
:::{div} text-small
**Note:** This only works in MyST.
:::
```python
intersphinx_mapping = {
  "sd": ("https://sphinx-design.readthedocs.io/en/latest/", None),
}
```
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: sphinx{design}
:link: sd:index
:link-type: ref
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: example.org
:link: https://example.org/
:link-type: url
:::
:::{shield}
:message: test@example.org
:link: mailto:test@example.org
:link-type: url
:::
:::::
:::::{sd-item}
Link to any URL using `url` for the `link-type` option.
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: example.org
:link: https://example.org/
:link-type: url
:::
::::
::::{code} markdown

:::{shield}
:message: test@example.org
:link: mailto:test@example.org
:link-type: url
:::
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
:::{shield}
:message: Indirect Reference
:link: "inv:sd#index"
:link-type: ref
:::
:::{shield}
:message: Indirect URL
:link: "[example-org]"
:link-type: url
:::
[example-org]: https://example.org/
:::::
:::::{sd-item}
Indirect references are defined out-of-band from the link definition, for example
at the end of the page.

In MyST, indirect references are defined by, for example:
- `[label]: inv:<project>#<label>`
- `[label]: <url>`
:::{div} text-small
**Note:** This only works in MyST.
:::
:::::
:::::{sd-item}
::::{code} markdown

:::{shield}
:message: Indirect Reference
:link: "inv:sd#index"
:link-type: ref
:::

:::{shield}
:message: Indirect URL
:link: "[example-org]"
:link-type: url
:::

[example-org]: https://example.org/

::::
:::::
::::::


:::::::


[icon slugs]: https://github.com/simple-icons/simple-icons/blob/master/slugs.md
[Shields.io]: https://shields.io/
[Shields.io Logos]: https://shields.io/docs/logos
[Shields.io Static Badges]: https://shields.io/badges/static-badge
[Simple Icons]: https://simpleicons.org/
