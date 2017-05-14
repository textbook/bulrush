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

 - [x] **Printable layouts** - the navigation is hidden when printed, avoiding
wasted space.

 - [x] **Custom styling** - additional CSS files can be included to customise
the default styling.

 - [x] **Service integrations** - including Disqus, GitHub, Google Analytics
and MailChimp.

 - [x] **PyPI package available** - so it can be `pip install`-ed.

Installation
------------

Bulrush is available via the [Python Package Index][22], so you can install it
with:

```bash
pip install bulrush
```

The main exports from the module are:

 - `PATH`: the path to the theme;
 - `FILTERS`: the additional Jinja filters used by the theme; and
 - `ENVIRONMENT`: the Jinja environment required by the theme.

You can use them in your `pelicanconf.py` as follows:

```python
import bulrush

THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS
```

### Other Requirements

The main stylesheet is provided in [Less][16] format, so you will need the Less
compiler (`lessc`). An easy way to install this is:

```bash
npm install -g less
```

You also need to make the appropriate Pelican plugin, [`assets`][15], available.
One way of achieving this is to make the `pelican-plugin` repository a submodule
of your site, then you can add to your `pelicanconf.py`:

```python
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']
```

### Alternative

If you don't want to install the theme from PyPI you can simply give Pelican a
relative path to the inner `bulrush/` directory. For example, add `bulrush` as
a submodule and set:

```python
THEME = 'bulrush/bulrush'
```

In this case you will need to configure the environment and filters yourself
and ensure that `webassets` *is* installed from PyPI.

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
| `MAILCHIMP` | Configure to activate a [MailChimp][20] sign-up form; see details below. |
| `MENUITEMS` | A list of tuples `('Title', 'URL')` for items to appear in the tabbed navigation. |
| `SITESUBTITLE` | A subtitle to appear in the header. |
| `SOCIAL` | A list of tuples `('Title', 'URL')` to appear in the "social" section of the sidebar. |
| `TWITTER_USERNAME` | Enables Twitter meta-tags in the article and page headers. |

If `DISPLAY_CATEGORIES_ON_MENU` is omitted or set explicitly to `True`, the
categories are shown in the tabbed navigation with any `MENUITEMS`. If
`DISPLAY_PAGES_ON_MENU` is omitted or set explicitly to `True`, they are listed
in the sidebar with any `SOCIAL` or other `LINKS`.

### Social Links

Appropriate icons are provided in the sidebar for a range of sites in the
`SOCIAL` link list. Have a look in [`social.html`][17] to see which titles this
applies to.

### MailChimp Configuration

If you're using [MailChimp][20] to handle a mailing list for your blog, you
can configure a subscription form in the sidebar. You need to set three values
to enable this, which you can get from [the signup form creator][21]. Simply
look for the form action:

```html
<form action="//user.region.list-manage.com/subscribe/post?u=abc123&amp;id=def456" ...
```

and extract the relevant sections:

```python
MAILCHIMP = dict(
    domain='user.region.list-manage.com',
    user_id='abc123',
    list_id='def456',
    validation=True,  # enable jQuery validation
)
```

If you set `validation=False` (or leave it out entirely) you will reduce the
page load (as it won't need 140KB of JavaScript) but won't get inline form
submission or email validation.

You can also add `rewards_url`, providing your unique [MonkeyRewards][19] URL,
to enable a *"Powered by MailChimp"* link.

Custom Styling
--------------

If any of the entries in `EXTRA_PATH_METADATA` have `'path'`s ending with
`'.css'` they will be included in the base template, allowing the site style
to be overridden as required. For example, in your `pelicanconf.py`:

```python
# Static files
STATIC_PATHS = [
    'extra',
    ...
]
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    ...
}
```

In use
------

Here are few current users of Bulrush (or modified versions of it):

 - [textbook](http://blog.jonrshar.pe/)
 - [Simon Says](https://simonsays.neocities.org/)
 - [CodeRobot](http://coderobot.downley.net/)
 - [chair6.net](http://chair6.net/)
 - [Just Numbers and Things](http://justnumbersandthings.com/)
 - [بلاگ باهم](https://baaham.net/blog/) (in Persian!)

If you'd like to be featured here (or are and would prefer not to be), feel
free to submit a [pull request][18].

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
  [15]: https://github.com/getpelican/pelican-plugins/tree/master/assets
  [16]: http://lesscss.org/
  [17]: https://github.com/textbook/bulrush/blob/master/templates/social.html
  [18]: https://help.github.com/articles/about-pull-requests/
  [19]: http://kb.mailchimp.com/accounts/billing/add-or-remove-monkeyrewards
  [20]: http://eepurl.com/cNv6Rb
  [21]: http://kb.mailchimp.com/lists/signup-forms/add-a-signup-form-to-your-website
  [22]: https://pypi.python.org/pypi/bulrush
