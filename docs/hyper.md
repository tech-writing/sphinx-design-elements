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
    provides an array of options to present hyperlinks differently. Hyper
    currently supports:

    :::{rubric} Button
    :::
    The {ref}`hyper-button` Hyper renders hyperlinks using the
    {ref}`button <sd:buttons>` directive from [](inv:sd#index).

    :::{rubric} Shield
    :::
    A {ref}`hyper-shield`-typed Hyper renders hyperlinks using
    badges from [Shields.io], building upon the {ref}`shield
    <shield-directive>` directive from {ref}`index`.


## Synopsis

A hyperlink that navigates to a URL, rendered in different variants,
defined using the markup outlined below.

::::{card}

:Text:
    {hyper}`https://community.panodata.org/t/technical-advancements-in-sphinx/278 {short-title=true}`

:Button:
    {hyper}`https://community.panodata.org/t/technical-advancements-in-sphinx/278 {type=button,outline=true,short-title=true}`

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
:row-class: col-compact bottom-margin-generous

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
- `[label]: reference`
- `[label]: #reference`
- `[label]: inv:project#reference`
- `[label]: url`
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


(hyper-button)=
### Button

Adding the option `{type=button}` renders the hyperlink using a badge based
on the sphinx-design [`button`](inv:sd#buttons) directive implementation, it
accepts the same options, and the additional `icon` option.

ref-type (`button-ref` only)
: Type of reference to use; `any` (default), `ref`, `doc`, or `myst`

color
: Set the color of the button (background and font).
  One of the semantic color names: `primary`, `secondary`, `success`, `danger`,
  `warning`, `info`, `light`, `dark`, `muted`.
  The default value is `primary`.

outline
: Display button in outlined color style variant. Use `outline=true`
  to toggle that option.

align
: Align the button on the page; `left`, `right`, `center` or `justify`

expand
: Expand to fit parent width. Use `expand=true` to toggle that option.

click-parent
: Make parent container also clickable. Use `click-parent=true` to
  toggle that option.

tooltip
: Add tooltip text, displayed when hovering over the link.

icon
: All [icon features](inv:sd#icons) of sphinx-design can be used. The icon,
  when given, will be placed on the left hand side of the text. The micro syntax
  to describe it is not much different from the original role notation, just note
  the colon `:` separates icon family from icon name.
  ```markdown
  {octicon}`report;1em;sd-text-info`  # Original MyST
  octicon:report;1em;sd-text-info     # Hyper inline variant
  ```

shadow
: Add shadow CSS.

class
: Additional CSS classes.


:::::::{sd-table}
:widths: 3 9
:row-class: col-compact bottom-margin-generous

::::::{sd-row}
:::::{sd-item} **Item**
:::::
:::::{sd-item} **Description and Syntax**
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org {type=button}` \
{hyper}`Read More <https://example.org> {type=button}`
:::::
:::::{sd-item}
A basic button hyperlink for URLs, without any options.
::::{code} markdown

{hyper}`https://example.org {type=button}` \
{hyper}`Read More <https://example.org> {type=button}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`shield-directive {type=button}` \
{hyper}`Shield badges <shield-directive> {type=button}`
:::::
:::::{sd-item}
Use project-local references.
::::{code} markdown

{hyper}`shield-directive {type=button}` \
{hyper}`Shield badges <shield-directive> {type=button}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`sd:sd-cards {type=button}` \
{hyper}`Card Layouts <sd:sd-cards> {type=button}`
:::::
:::::{sd-item}
Use intersphinx references.
::::{code} markdown

{hyper}`sd:sd-cards {type=button}` \
{hyper}`Card Layouts <sd:sd-cards> {type=button}`
::::
:::::
::::::


:::{rubric} Layout
:::

::::::{sd-row}
:::::{sd-item}
`expand` option.
:::::
:::::{sd-item}
Use the `expand` option to fit the element to the width of its parent.
{hyper}`https://example.org {type=button,expand=true}`
::::{code} markdown

{hyper}`https://example.org {type=button,expand=true}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
`align` option.
:::::
:::::{sd-item}
Use the `align` option.

{hyper}`https://example.org {type=button,align=center}`
::::{code} markdown

{hyper}`https://example.org {type=button,align=center}`
::::
:::{todo}
:class: no-margin
Apparently, the `align` option does not work?
:::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org {type=button,icon=octicon:rocket,notext=true}`
{hyper}`https://example.org {type=button,icon=octicon:rocket,notext=true}`
{hyper}`https://example.org {type=button,icon=octicon:rocket,notext=true}`
:::::
:::::{sd-item}
Because `hyper` roles render as inline elements, multiple instances can
be placed side by side, even when written down spanning multiple lines.
Regular button directives are block level elements, which would cause
line breaks.
::::{code} markdown

{hyper}`https://example.org {type=button,icon=octicon:rocket,notext=true}`
{hyper}`https://example.org {type=button,icon=octicon:rocket,notext=true}`
{hyper}`https://example.org {type=button,icon=octicon:rocket,notext=true}`
::::
:::::
::::::


:::{rubric} Style
:::

::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org {type=button,outline=true}` \
{hyper}`https://example.org {type=button,color=info}` \
{hyper}`https://example.org {type=button,shadow=true}`
:::::
:::::{sd-item}
Use `outline`, `color`, and `shadow` options.
::::{code} markdown

{hyper}`https://example.org {type=button,outline=true}` \
{hyper}`https://example.org {type=button,color=info}` \
{hyper}`https://example.org {type=button,shadow=true}`
::::
:::{todo}
:class: no-margin
Apparently, the `shadow` option does not work?
:::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`https://example.org {type=button,class=text-small}` \
{hyper}`https://example.org {type=button,tooltip=Tooltip Message}`
:::::
:::::{sd-item}
Use `class` and `tooltip` options.
::::{code} markdown

{hyper}`https://example.org {type=button,class=text-small}` \
{hyper}`https://example.org {type=button,tooltip=Tooltip Message}`
::::
:::::
::::::


::::::{sd-row}
:::::{sd-item}
{hyper}`Read More <https://example.org> {type=button,icon=octicon:report}` \
{hyper}`Read More <https://example.org> {type=button,color=info,outline=true,icon=material-outlined:emoji_objects;3em;sd-text-primary}`
:::::
:::::{sd-item}
The value of the `icon` option translates to the syntax of an {ref}`inline icon
<sd:icons>` from [](inv:sd#index), inheriting all its features.
::::{code} markdown

{hyper}`Read More <https://example.org> {type=button,icon=octicon:report}` \
{hyper}`Read More <https://example.org> {type=button,color=info,outline=true,icon=material-outlined:emoji_objects;3em;sd-text-primary}`
::::
:::::
::::::


:::::::


(hyper-shield)=
### Shield

Adding the option `{type=shield}` renders the hyperlink using a badge based
on the [`shield`](#shield-directive) directive implementation.

:::::::{sd-table}
:widths: 3 9
:row-class: col-compact bottom-margin-generous

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


:::{rubric} Layout
:::

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
Because `hyper` roles render as inline elements, multiple instances can
be placed side by side, even when written down spanning multiple lines.
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


:::{rubric} Style
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

::::{dropdown} Shield Shortcuts
:animate: fade-in-slide-down
:open:

Shield shortcut roles help saving a few keystrokes. Examples:
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

:::{code} markdown

{hyper-navigate}`https://example.org`
{hyper-open}`https://example.org`

{hyper-tutorial}`https://example.org`
{hyper-read-more}`https://example.org`
{hyper-readme-github}`https://example.org`

{hyper-nb-colab}`https://example.org`
{hyper-nb-binder}`https://example.org`
{hyper-nb-github}`https://example.org`
:::
::::


::::{dropdown} Buttons Everywhere
:animate: fade-in-slide-down
:open:

Buttons in multiple colors, optionally outlined. \
Colors: primary, secondary, success, danger, warning, info, light, dark, muted

{hyper}`primary <https://example.org> {type=button,color=primary}`
{hyper}`secondary <https://example.org> {type=button,color=secondary}`
{hyper}`success <https://example.org> {type=button,color=success}`
{hyper}`danger <https://example.org> {type=button,color=danger}`
{hyper}`warning <https://example.org> {type=button,color=warning}`
{hyper}`info <https://example.org> {type=button,color=info}`
{hyper}`light <https://example.org> {type=button,color=light}`
{hyper}`dark <https://example.org> {type=button,color=dark}`
{hyper}`muted <https://example.org> {type=button,color=muted}`

{hyper}`primary <https://example.org> {type=button,color=primary,outline=true}`
{hyper}`secondary <https://example.org> {type=button,color=secondary,outline=true}`
{hyper}`success <https://example.org> {type=button,color=success,outline=true}`
{hyper}`danger <https://example.org> {type=button,color=danger,outline=true}`
{hyper}`warning <https://example.org> {type=button,color=warning,outline=true}`
{hyper}`info <https://example.org> {type=button,color=info,outline=true}`
{hyper}`light <https://example.org> {type=button,color=light,outline=true}`
{hyper}`dark <https://example.org> {type=button,color=dark,outline=true}`
{hyper}`muted <https://example.org> {type=button,color=muted,outline=true}`

:::{code} markdown

{hyper}`primary <https://example.org> {type=button,color=primary}`
{hyper}`secondary <https://example.org> {type=button,color=secondary}`
{hyper}`success <https://example.org> {type=button,color=success}`
{hyper}`danger <https://example.org> {type=button,color=danger}`
{hyper}`warning <https://example.org> {type=button,color=warning}`
{hyper}`info <https://example.org> {type=button,color=info}`
{hyper}`light <https://example.org> {type=button,color=light}`
{hyper}`dark <https://example.org> {type=button,color=dark}`
{hyper}`muted <https://example.org> {type=button,color=muted}`

{hyper}`primary <https://example.org> {type=button,color=primary,outline=true}`
{hyper}`secondary <https://example.org> {type=button,color=secondary,outline=true}`
{hyper}`success <https://example.org> {type=button,color=success,outline=true}`
{hyper}`danger <https://example.org> {type=button,color=danger,outline=true}`
{hyper}`warning <https://example.org> {type=button,color=warning,outline=true}`
{hyper}`info <https://example.org> {type=button,color=info,outline=true}`
{hyper}`light <https://example.org> {type=button,color=light,outline=true}`
{hyper}`dark <https://example.org> {type=button,color=dark,outline=true}`
{hyper}`muted <https://example.org> {type=button,color=muted,outline=true}`
:::

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
`doc:badges_buttons` can't be resolved well. See "Intersphinx across
the board".
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
