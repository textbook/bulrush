from datetime import datetime, timezone
from json import loads
from unittest import TestCase

from pelican.contents import Article
from pelican.settings import DEFAULT_CONFIG
from pelican.urlwrappers import Category, Author

from bulrush import generate_jsonld_schema

ARTICLE_URL = 'article-name.html'
AUTHOR = 'Hans Muster'
CATEGORY = 'Article Category'
DATE = datetime.now(timezone.utc)
HEADLINE = 'Headless Body In Topless Bar'
SITE_URL = 'http://example.org'


def _build_article(content='', **metadata):
    defaults = dict(
        author=Author(AUTHOR, DEFAULT_CONFIG),
        category=Category(CATEGORY, DEFAULT_CONFIG),
        date=DATE,
        title=HEADLINE,
        url=ARTICLE_URL,
    )
    defaults.update(metadata)
    return Article(content=content, settings=DEFAULT_CONFIG, metadata=defaults)


class ArticleSchemaGeneratorTest(TestCase):

    ARTICLE = _build_article('This is a nice article')

    @staticmethod
    def _generate_schema(article=None):
        return loads(generate_jsonld_schema(article or _build_article(), SITE_URL))

    def assertSchemaContains(self, schema, key, value):
        self.assertIn(key, schema)
        self.assertEqual(value, schema[key])

    def assertSchemaContainsLax(self, schema, key, value):
        self.assertIn(key, schema)
        self.assertIn(value, schema[key])

    def test_context(self):
        schema = self._generate_schema()
        self.assertSchemaContains(schema, '@context', 'http://schema.org')

    def test_main_entity(self):
        expected = {
            '@type': 'WebPage',
            '@id': '{}/{}'.format(SITE_URL, ARTICLE_URL),
        }
        schema = self._generate_schema()
        self.assertSchemaContains(schema, 'mainEntityOfPage', expected)

    def test_type(self):
        schema = self._generate_schema()
        self.assertSchemaContains(schema, '@type', 'BlogPosting')

    def test_article_section(self):
        schema = self._generate_schema()
        self.assertSchemaContains(schema, 'articleSection', CATEGORY)

    def test_headline(self):
        schema = self._generate_schema()
        self.assertSchemaContains(schema, 'headline', HEADLINE)

    def test_date_published(self):
        schema = self._generate_schema()
        formatted = DATE.strftime('%Y-%m-%dT%H:%M:%S')
        self.assertSchemaContainsLax(schema, 'datePublished', formatted)

    def test_date_modified_missing(self):
        schema = self._generate_schema()
        self.assertNotIn('dateModified', schema)

    def test_date_modified_supplied(self):
        modified = datetime(2011, 12, 13, 14, 15, 16)
        formatted = modified.strftime('%Y-%m-%dT%H:%M:%S')

        schema = self._generate_schema(_build_article(modified=modified))

        self.assertSchemaContainsLax(schema, 'dateModified', formatted)

    def test_author(self):
        expected = {'@type': 'Person', 'name': AUTHOR}
        schema = self._generate_schema()
        self.assertSchemaContains(schema, 'author', expected)

    def test_image(self):
        src = 'https://www.fillmurray.com/g/200/300'
        content = '<img src="{}">'.format(src)
        expected = {'@type': 'ImageObject', 'url': src}

        schema = self._generate_schema(_build_article(content))

        self.assertSchemaContains(schema, 'image', expected)

    def test_description(self):
        summary = 'Just a short intro to the article'
        markup = '<p>{}</p>'.format(summary)

        schema = self._generate_schema(_build_article(summary=markup))

        self.assertSchemaContains(schema, 'description', summary)
