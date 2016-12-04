Bulrush
=======

A [Bulma][1]-based [Pelican][2] blog theme; clean, flexible and responsive.

The icons are from [Font Awesome][3] by Dave Gandy. The pure HTML/CSS "Fork me
on GitHub" ribbon is based on [`github-fork-ribbon-css`][4] by Simon Whitaker; I
modified it to be flatter.

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

Features
--------

 - [x] **Responsive design** - four column layout on desktop (≥980px), three column
on tablet (≥769px), single column on mobile. Tabbed navigation bar collapses
into drop-down "burger menu" on mobile.

 - [x] **Meta tagging functionality** - support for [Open Graph][5] and [Twitter
Cards][6] meta tags, giving enhanced display when sharing articles on social
media sites (**note**: *currently only available for [articles and pages][7]*).

Screenshots
-----------

 - 980 x 480px:

     ![Screenshot - Bulrush at 980px][10]

 - 480 x 480px

     ![Screenshot - Bulrush at 480px][11]

 - 840 x 480px

     ![Screenshot - Bulrush at 840px][12]

 - 1,440 x 480px

     ![Screenshot - Bulrush at 1440px][13]

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
