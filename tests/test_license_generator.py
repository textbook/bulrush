from unittest import TestCase

from bulrush import generate_license


class LicenseNameGeneratorTest(TestCase):

    @property
    def url(self):
        return '#'

    def _create_license(self):
        return generate_license('')

    def test_format(self):
        html = self._create_license()
        self.assertIn('<ul class="menu-list">', html)
        self.assertIn('<li>', html)
        self.assertIn('<span class="icon is-small">', html)

    def test_icon(self):
        html = self._create_license()
        self.assertIn('<i class="fa fa-file-text-o fa-fw">', html)

    def test_url(self):
        html = self._create_license()
        self.assertIn('<a rel="license" href="{}">'.format(self.url), html)

    def test_name(self):
        name = 'License Name'
        html = generate_license(name)
        self.assertIn('<span>{}</span>'.format(name), html)


class CreativeCommonsTest(LicenseNameGeneratorTest):

    CC_NAME = 'CC-BY-SA-4.0'
    CC_URL = 'http://creativecommons.org/licenses/by-sa/4.0/'

    @property
    def url(self):
        return self.CC_URL

    def _create_license(self):
        return generate_license(self.CC_NAME)

    def test_name(self):
        html = self._create_license()
        self.assertIn('<span>CC BY-SA 4.0</span>', html)

    def test_icon(self):
        html = self._create_license()
        self.assertIn('<i class="fa fa-creative-commons fa-fw">', html)


class LicenseDictGeneratorTest(TestCase):

    def test_format(self):
        html = generate_license(dict(name='', url=''))
        self.assertIn('<ul class="menu-list">', html)
        self.assertIn('<li>', html)
        self.assertIn('<span class="icon is-small">', html)

    def test_name(self):
        name = 'My Cool License'
        html = generate_license(dict(name=name, url=''))
        self.assertIn('<span>{}</span>'.format(name), html)

    def test_url(self):
        url = 'http://example.org'
        html = generate_license(dict(name='', url=url))
        self.assertIn('<a rel="license" href="{}">'.format(url), html)

    def test_default_icon(self):
        html = generate_license(dict(name='', url=''))
        self.assertIn('<i class="fa fa-file-text-o fa-fw">', html)

    def test_custom_icon(self):
        html = generate_license(dict(name='', url='', icon='lock'))
        self.assertIn('<i class="fa fa-lock fa-fw">', html)

    def test_invalid_spec(self):
        html = generate_license({})
        self.assertEqual('', html)
