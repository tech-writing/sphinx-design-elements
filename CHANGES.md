# Change Log

## Unreleased
- Dependencies: Added compatibility with docutils 0.19 - 0.22
- Dependencies: Added compatibility with sphinx 7 - 9
- Add "link tree" element, using directive `linktree`

## v0.4.0 - 2024-06-27
- Dependencies: Update to sphinx-design 0.6.0
  See also [sphinx-design change log].
- Remove support for Python 3.7 and 3.8, following `sphinx-design`.

## v0.3.2 - 2024-05-28
- Dependencies: Use sphinx-design 0.5
  sphinx-design 0.6 introduced CSS changes downstream projects might not
  be prepared for.

## v0.3.1 - 2024-04-10
- Fix compatibility issue with Python 3.8

## v0.3.0 - 2024-04-06
- Accept more options on grid table's `sd-item` directive
- Add `shield` directive, to render badges through Shields.io
- Add `hyper` role, to render different kinds of hyperlinks

## v0.2.1 - 2023-08-08

- Improve JS/CSS asset loading
- Fix JavaScript for dropdown group elements

## v0.2.0 - 2023-08-08

- For dropdown elements that should exclusively open when toggled,
  add a `dropdown-group` CSS class. Thanks, @kojinkai and @msbt.

## v0.1.0 - 2023-07-19

- Add "grid table" element, using directives `sd-table`, `sd-row`, `sd-item`
- Add "info card" element, using directive `info-card`
- Add "tag(s)" shortcuts, using roles `tag` and `tags`


[sphinx-design change log]: https://sphinx-design.readthedocs.io/en/furo-theme/changelog.html#v0-6-0-2024-05-23
