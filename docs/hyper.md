(hyper-role)=

# Hyper


## About

A component to render hyperlinks with a few bells and whistles,
implementing the Sphinx role `hyper`.


## Features

The `hyper` role aims to expand the features of the traditional
Sphinx `:ref:` / `{ref}` role everyone loves so much for its powerful
linking capabilities.

:Syntax Extension:
    The standard role expression syntax of `{ref}` is extended, by adding a
    third slot for conveying additional **options** to Sphinx roles, building
    upon fundamentals of Sphinx referencing and linking. A typical markup
    snippet using the `{hyper}` role in MyST syntax looks like this.
    :::{code}
    {hyper}`label <resource> {option1=value1,option2=value2}`
    :::
    The most basic variant is to just slap an arbitrary resource identifier
    into its value slot. That can be a Sphinx reference of any kind, or just
    an URL.
    :::{code}
    {hyper}`resource`
    :::

:Referencing and Linking:
    The role implementation `HyperRefRole` inherits all the niceties from
    `AnyXRefRole`. 
    Linking features are enhanced by providing rST / MyST cross-over
    compatibility, and a few other gimmicks like automatically deriving
    link labels from `<title>` elements of HTML pages on arbitrary URLs.

:Layout and Style:
    Other than rendering plain HTML hyperlink anchors, the `hyper` role
    provides an array of options to present hyperlinks differently.
    For example, hyperlinks can be represented through badges from
    [Shields.io], building upon the {ref}`shield <shield-directive>`
    directive, just by slapping a `{type=shield}` option on it.


## Synopsis

A hyperlink that navigates to a URL, rendered in different variants,
defined using the markup outlined below.

::::{card}

:Text-Only:
    {hyper}`https://community.panodata.org/t/technical-advancements-in-sphinx/278 {short-title=true}`

:Shield:
    {hyper}`https://community.panodata.org/t/technical-advancements-in-sphinx/278 {type=shield,label=Navigate to,short-title=true}`

::::



## Usage

::::{tab-set-code}
:::{literalinclude} ./snippets/myst/hyper.md
:language: markdown
:::
::::

:::{warning}
Currently only works with MyST.
reStructuredText is not supported yet, but support can be added.
:::

The `hyper` role provides a few configuration options, 
mimicking and expanding `{ref}`.

:::::::{sd-table}
:widths: 3 9
:row-class: col-compact

:::{rubric} Fundamentals
:::

::::::{sd-row}
:::::{sd-item} **Item**
:::::
:::::{sd-item} **Description and Syntax**
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org` \
{hyper}`mailto:test@example.org`
:::::
:::::{sd-item}
A basic hyper without any options, referencing an URL.
::::{code} markdown

{hyper}`https://example.org` \
{hyper}`mailto:test@example.org`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`Read More <https://example.org>`
:::::
:::::{sd-item}
Referencing a URL with a self-defined link label.
::::{code} markdown

{hyper}`Read More <https://example.org>`
::::
:::::
::::::


:::{rubric} Linking and Referencing
:::

::::::{sd-row}
:::::{sd-item}
{hyper}`infocard-directive` \
{hyper}`#infocard-directive`
:::::
:::::{sd-item}
Links to project-local references can be defined by using reference labels
in both reStructuredText and MyST syntax.
::::{code} markdown

{hyper}`infocard-directive` \
{hyper}`#infocard-directive`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`sd:sd-cards` \
{hyper}`Card Layouts <sd:sd-cards>`
:::::
:::::{sd-item}
Using a traditional intersphinx reference is the most compact way to
run links to other Sphinx projects.
::::{code} markdown

{hyper}`sd:sd-cards` \
{hyper}`Card Layouts <sd:sd-cards>`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`inv:sd:*:doc#index` \
{hyper}`inv:sd:*:label#sd-grids` \
{hyper}`inv:sd#sd-cards`
:::::
:::::{sd-item}
MyST reference syntax is also supported for intersphinx links.
::::{code} markdown

{hyper}`inv:sd:*:doc#index` \
{hyper}`inv:sd:*:label#sd-grids` \
{hyper}`inv:sd#sd-cards`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`Grid Table <[gridtable]>` \
{hyper}`Sphinx Design <[sphinx-design]>` \
{hyper}`Example Domain <[example-org]>`

[gridtable]: gridtable-directive
[sphinx-design]: inv:sd#index
[example-org]: https://example.org/
:::::
:::::{sd-item}
Indirect references are defined out-of-band from the link definition, for example
at the end of the page.

In MyST, indirect references are defined by, for example:
- `[label]: <reference>`
- `[label]: #<reference>`
- `[label]: inv:<project>#<reference>`
- `[label]: <url>`
:::{div} text-small
**Note:** This only works in MyST.
:::
::::{code} markdown

{hyper}`Grid Table <[gridtable]>` \
{hyper}`Sphinx Design <[sphinx-design]>` \
{hyper}`Example Domain <[example-org]>`

[gridtable]: gridtable-directive
[sphinx-design]: inv:sd#index
[example-org]: https://example.org/
::::
:::::
::::::

:::::::


## Variants

The `hyper` role provides a few rendering variants.

:::::::{sd-table}
:widths: 3 9
:row-class: col-compact

:::{rubric} Shield
:::

Adding the option `{type=shield}` renders the hyperlink using a badge based
on the [`shield`](#shield-directive) directive implementation.

::::::{sd-row}
:::::{sd-item} **Item**
:::::
:::::{sd-item} **Description and Syntax**
:::::
::::::

::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org {type=shield}` \
{hyper}`mailto:test@example.org {type=shield}`
:::::
:::::{sd-item}
A basic shield hyperlink.
::::{code} markdown

{hyper}`https://example.org {type=shield}` \
{hyper}`mailto:test@example.org {type=shield}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`Read More <https://example.org> {type=shield}`
:::::
:::::{sd-item}
Using a self-defined linked label works the same way with `{type=shield}`.
::::{code} markdown

{hyper}`Read More <https://example.org> {type=shield}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`Info Card <infocard-directive> {type=shield}` \
{hyper}`Info Card <#infocard-directive> {type=shield}`
:::::
:::::{sd-item}
Link to project-local references, with link labels.
::::{code} markdown

{hyper}`Info Card <infocard-directive> {type=shield}` \
{hyper}`Info Card <#infocard-directive> {type=shield}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`sd:sd-cards {type=shield}` \
{hyper}`Card Layouts <sd:sd-cards> {type=shield}`
:::::
:::::{sd-item}
Using a traditional intersphinx reference is the most compact way to
run links to other Sphinx projects.
::::{code} markdown

{hyper}`sd:sd-cards {type=shield}` \
{hyper}`Card Layouts <sd:sd-cards> {type=shield}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`inv:sd:*:doc#index {type=shield}` \
{hyper}`inv:sd:*:label#sd-grids {type=shield}` \
{hyper}`inv:sd#sd-cards {type=shield}`
:::::
:::::{sd-item}
MyST reference syntax is also supported for intersphinx links.
::::{code} markdown

{hyper}`inv:sd:*:doc#index {type=shield}` \
{hyper}`inv:sd:*:label#sd-grids {type=shield}` \
{hyper}`inv:sd#sd-cards {type=shield}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org {type=shield,label=Read}`
:::::
:::::{sd-item}
A shield with an additional label, rendered on the left-hand side.
::::{code} markdown

{hyper}`https://example.org {type=shield,label=Read}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`More <https://example.org> {type=shield,label=Read}` \
{hyper}`https://example.org {type=shield,label=Read,message=More}`
:::::
:::::{sd-item}
When using an additional shield `label` on the left-hand side, the
text on the right-hand side can be defined through the link label,
or the `message` option. 
::::{code} markdown

{hyper}`More <https://example.org> {type=shield,label=Read}` \
{hyper}`https://example.org {type=shield,label=Read,message=More}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org {type=shield,label=🌻 Read,message=More 🍀}`
:::::
:::::{sd-item}
Text input also accepts Unicode glyphs.
::::{code} markdown

{hyper}`https://example.org {type=shield,label=🌻 Read,message=More 🍀}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`H1 <https://example.org> {type=shield}`
{hyper}`H2 <https://example.org> {type=shield}`
:::::
:::::{sd-item}
By default, `hyper` roles render as inline elements, so multiple ones are
placed side by side, even when authored using line breaks.
::::{code} markdown

{hyper}`H1 <https://example.org> {type=shield}`
{hyper}`H2 <https://example.org> {type=shield}`
::::
:::{tip}
For purposely applying line breaks, use the backslash `\` as line
continuation character.
:::
:::::
::::::


:::{rubric} Styling
:::

About defining colors, an icon, and the style/shape of the shield.
The corresponding options accept the same values like the
[`shield`](#shield-directive) directive.


::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org {type=shield,color=darkgreen}`
:::::
:::::{sd-item}
Use the [`color`](#shield-color) option to adjust the background color.
::::{code} markdown

{hyper}`https://example.org {type=shield,color=darkgreen,logo=Markdown}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org {type=shield,label=Read,message=More,label-color=darkgreen,message-color=orange}` \
{hyper}`https://example.org {type=shield,label=Read,message=More,label-color=hsl(270,60%,70%),message-color=rgb(255,0,153)}` \
{hyper}`https://example.org {type=shield,message=Read More,color=#123456}`
:::::
:::::{sd-item}
Left vs. right background colors can be defined by using the `label-color`
vs. `message-color` options, see [](#shield-color). For single-colored shields,
the `color` option can be used as an alias for `message-color`.
::::{code} markdown

{hyper}`https://example.org {type=shield,label=Read,message=More,label-color=darkgreen,message-color=orange}` \
{hyper}`https://example.org {type=shield,label=Read,message=More,label-color=hsl(270,60%,70%),message-color=rgb(255,0,153)}` \
{hyper}`https://example.org {type=shield,message=Read More,color=#123456}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`CrateDB <https://cratedb.com> {type=shield,color=gray,logo=CrateDB}`
:::::
:::::{sd-item}
Select an image from a collection of brand depictions, using the
[`logo`](#shield-logo) option.
::::{code} markdown

{hyper}`CrateDB <https://cratedb.com> {type=shield,color=gray,logo=CrateDB}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org {type=shield,style=flat}` \
{hyper}`https://example.org {type=shield,style=flat-square}` \
{hyper}`https://example.org {type=shield,style=plastic}` \
{hyper}`https://example.org {type=shield,style=for-the-badge}` \
{hyper}`https://example.org {type=shield,style=social}`
:::::
:::::{sd-item}
The [`style`](#shield-style) option determines the style / shape of the shield.
::::{code} markdown

{hyper}`https://example.org {type=shield,style=flat}` \
{hyper}`https://example.org {type=shield,style=flat-square}` \
{hyper}`https://example.org {type=shield,style=plastic}` \
{hyper}`https://example.org {type=shield,style=for-the-badge}` \
{hyper}`https://example.org {type=shield,style=social}`
::::
:::::
::::::


:::::::


## Gallery

A few more examples, about shortcuts and intersphinx linking.

::::{dropdown} Shortcuts
:animate: fade-in-slide-down
:open:

Shortcut roles help saving keystrokes. Examples:
`hyper-navigate`, `hyper-open`, `hyper-tutorial`, `hyper-read-more`,
`hyper-readme-github`, `hyper-nb-colab`, `hyper-nb-binder`, `hyper-nb-github`. 

---

{hyper-navigate}`https://example.org`
{hyper-open}`https://example.org`

{hyper-tutorial}`https://example.org`
{hyper-read-more}`https://example.org`
{hyper-readme-github}`https://example.org`

{hyper-nb-colab}`https://example.org`
{hyper-nb-binder}`https://example.org`
{hyper-nb-github}`https://example.org`

::::{code} markdown

{hyper-navigate}`https://example.org`
{hyper-open}`https://example.org`

{hyper-tutorial}`https://example.org`
{hyper-read-more}`https://example.org`
{hyper-readme-github}`https://example.org`

{hyper-nb-colab}`https://example.org`
{hyper-nb-binder}`https://example.org`
{hyper-nb-github}`https://example.org`
::::

::::{dropdown} Intersphinx across the board
:animate: fade-in-slide-down

There are some flaws here yet, see backlog below.

:::{rubric} Intersphinx Text-Only
:::

- {hyper }`sd:index` provides
{hyper}`sd:sd-grids`
{hyper}`sd:sd-cards`
{hyper}`sd:sd-dropdowns`
{hyper}`sd:sd-tabs`
{hyper }`sd:badges_buttons`
{hyper }`doc:badges_buttons`
{hyper}`sd:special`.


:::{rubric} Intersphinx Shields
:::

- {hyper}`sd:index {type=shield}` provides
{hyper}`sd:sd-grids {type=shield}`
{hyper}`sd:sd-cards {type=shield}`
{hyper}`sd:sd-dropdowns {type=shield}`
{hyper}`sd:sd-tabs {type=shield}`
{hyper}`sd:badges_buttons {type=shield}`
{hyper}`sd:special {type=shield}`.

- {hyper}`myst:index {type=shield}` provides
{hyper}`myst:syntax/core {type=shield}`
{hyper}`myst:syntax/colon_fence {type=shield}`
{ hyper}`myst:syntax/admonitions {type=shield}`
{hyper}`myst:syntax/images_and_figures {type=shield}`
{hyper}`myst:syntax/roles-and-directives {type=shield}`
{hyper}`myst:syntax/reference {type=shield}`
{hyper}`myst:syntax/cross-referencing {type=shield}`
{hyper}`myst:syntax/code_and_apis {type=shield}`
{ hyper}`myst:syntax/math {type=shield}`
{hyper}`myst:syntax/extensions {type=shield}`.

::::


## Backlog

:::{todo}
There are a few errors in here: `sd:index`, `sd:badges_buttons`, and
`doc:badges_buttons` can't be resolved well.
:::
:::{todo}
Link label resolution does not work yet with project-local links, e.g.
{hyper}`infocard-directive`, {hyper}`#infocard-directive`.
:::
:::{todo}
rgb() / hsl() colors do not work, yet. They contain values separated by
commas, which confuses the naive role option parser.
:::
:::{todo}
Resolving `myst:syntax/admonitions` and `myst:syntax/math` does not work yet,
due to ambiguity errors.

-- [More than one target found for 'myst' cross-reference [myst.xref_ambiguous]](https://github.com/executablebooks/MyST-Parser/issues/892)
:::
:::{todo}
Maybe use a different way of having shortcuts, not by using dedicated roles,
but integrated into the options instead. Also, leverage shield-level style
presets, as outlined in their backlog.
:::


[Shields.io]: https://shields.io/
