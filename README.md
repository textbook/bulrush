Bulrush
=======

A [Bulma][1]-based [Pelican][2] blog theme; clean, flexible and responsive.

 ![Screenshot - Bulrush at 1440px][13]

The icons are from [Font Awesome][3] by Dave Gandy. The pure HTML/CSS "Fork me
on GitHub" ribbon is based on [`github-fork-ribbon-css`][4] by Simon Whitaker; I
modified it to be flatter.

Features
--------

 - [x] **Responsive design** - four column layout on desktop (≥980px), three column
on tablet (≥769px), single column on mobile. Tabbed navigation bar collapses
into drop-down "burger menu" on mobile.

 - [x] **Meta tagging functionality** - support for [Open Graph][5] and [Twitter
Cards][6] meta tags, giving enhanced display when sharing articles on social
media sites (**note**: *currently only available for [articles and pages][7]*).

Additional Screenshots
----------------------

 - 480 x 480px (mobile):

     ![Screenshot - Bulrush at 480px][11]

 - 840 x 480px (tablet):

     ![Screenshot - Bulrush at 840px][12]

 - 980 x 480px (desktop):

     ![Screenshot - Bulrush at 980px][10]

Settings
--------

As well as the [basic settings][14], Bulrush supports the following options in
your `pelicanconf.py`:

| Setting name | What does it do? |
| --- | --- |
| `DISQUS_SITENAME` | Enables Disqus comments. Note that you should set up the full Comment Count Link, as no additional text is applied. |
| `GITHUB_URL` | Enables the "Fork me on GitHub" ribbon. |
| `GOOGLE_ANALYTICS` | Set to `‘UA-XXXX-YYYY’` to activate Google Analytics. |
| `LINKS` | A list of tuples `('Title', 'URL')` for links to appear in the "blogroll" section of the sidebar. |
| `MENUITEMS` | A list of tuples `('Title', 'URL')` for items to appear in the tabbed navigation. |
| `SITESUBTITLE` | A subtitle to appear in the header. |
| `SOCIAL` | A list of tuples `('Title', 'URL')` to appear in the “social” section of the sidebar. |
| `TWITTER_USERNAME` | Enables Twitter meta-tags in the article and page headers. |

If `DISPLAY_CATEGORIES_ON_MENU` is omitted or set explicitly to `True`, the
categories are shown in the tabbed navigation with any `MENUITEMS`. If
`DISPLAY_PAGES_ON_MENU` is omitted or set explicitly to `True`, they are listed
in the sidebar with any `SOCIAL` or other `LINKS`.

If the following titles are used in `SOCIAL`, an appropriate icon is added in
the sidebar:

 - Bitbucket
 - GitHub
 - Stack Overflow
 - Twitter

Requirements
------------

This theme requires an additional Python dependency, [`webassets`][9], which can
be added to your project with:

```bash
pip install webassets
```

It also requires two Jinja plugins, `webassets` and [the `with` statement][8].
To implement this, I have the following in my `pelicanconf.py`:

```python
JINJA_EXTENSIONS = ['webassets.ext.jinja2.AssetsExtension', 'jinja2.ext.with_']
```

  [1]: http://bulma.io/
  [2]: http://docs.getpelican.com/en/stable/
  [3]: http://fontawesome.io/
  [4]: https://github.com/simonwhitaker/github-fork-ribbon-css
  [5]: http://ogp.me/
  [6]: https://dev.twitter.com/cards/overview
  [7]: http://docs.getpelican.com/en/3.6.3/content.html#articles-and-pages
  [8]: http://jinja.pocoo.org/docs/dev/extensions/#with-statement
  [9]: https://github.com/miracle2k/webassets/
  [10]: ./screenshot-980px.png
  [11]: ./screenshot-480px.png
  [12]: ./screenshot-840px.png
  [13]: ./screenshot-1440px.png
  [14]: http://docs.getpelican.com/en/3.6.3/settings.html#basic-settings
