(linktree-directive)=

# Link Tree


## About

Similar but different from a Toc Tree.

```{attention}
This component is a work in progress. Breaking changes should be expected until a
1.0 release, so version pinning is recommended.
```

### Problem

So much work went into the toctree mechanics, it is sad that it is not a reusable
component for building any kinds of navigation structures, and to be able to define
its contents more freely.

### Solution

This component implements a programmable toc tree component, the link tree.


## Details

The link tree component builds upon the Sphinx [toc] and [toctree] subsystem. It provides
both a rendered primary navigation within the `sde_linktree_primary` context variable
for use from HTML templates, and a Sphinx directive, `linktree`, for rendering
navigation trees into pages, similar but different from the [toctree directive]. The
user interface mechanics and styles are based on [Furo]'s primary sidebar component.


## Customizing

Link trees can be customized by creating them programmatically, similar to how
the `sde_linktree_primary` context variable is populated with the default Sphinx
toc tree.

The section hidden behind the dropdown outlines how the "custom linktree" is
defined, which is displayed at the bottom of the page in a rendered variant.
:::{dropdown} Custom linktree example code

```python
import typing as t

from sphinx.application import Sphinx
from sphinx_design_elements.lib.linktree import LinkTree


def demo_tree(app: Sphinx, context: t.Dict[str, t.Any], docname: str = None) -> LinkTree:
    """
    The demo link tree showcases some features what can be done.

    It uses regular page links to documents in the current project, a few
    intersphinx references, and a few plain, regular, URL-based links.
    """
    linktree = LinkTree.from_context(app=app, context=context)
    doc = linktree.api.doc
    ref = linktree.api.ref
    link = linktree.api.link

    linktree \
        .title("Project-local page links") \
        .add(
            doc(name="gridtable"),
            doc(name="infocard"),
        )

    linktree \
        .title("Intersphinx links") \
        .add(
            ref("sd:index"),
            ref("sd:badges", label="sphinx{design} badges"),
            ref("myst:syntax/images_and_figures", "MyST » Images and figures"),
            ref("myst:syntax/referencing", "MyST » Cross references"),
        )

    linktree \
        .title("URL links") \
        .add(
            link(uri="https://example.com"),
            link(uri="https://example.com", label="A link to example.com, using a custom label ⚽."),
    )

    return linktree
```
:::

```{todo}
- Use the `linktree` directive to define custom link trees.
- Link to other examples of custom link trees.
- Maybe use `:link:` and `:link-type:` directive options of `grid-item-card` directive.
```


## Directive examples

### Example 1

The link tree of the `index` page, using a defined maximum depth, and a custom title.
```{linktree}
:docname: index
:maxdepth: 1
:title: Custom title
```


## Appendix

Here, at the bottom of the page, different global template variables are presented,
which contain representations of navigation trees, rendered to HTML.

- `sde_linktree_primary`: The classic toctree, like it will usually be rendered
  into the primary sidebar.
- `demo_synthetic_linktree`: A customized link tree composed of links to project-local
  pages, intersphinx links, and URLs, for demonstration purposes.

```{hint}
The corresponding template, `linktree-demo.html` will exclusively be rendered
here, and not on other pages.
```

[Furo]: https://pradyunsg.me/furo/
[toctree directive]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree
[toc]: https://www.sphinx-doc.org/en/master/development/templating.html#toc
[toctree]: https://www.sphinx-doc.org/en/master/development/templating.html#toctree
