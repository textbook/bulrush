from pathlib import Path
from unittest import TestCase

import bulrush


class ExportTest(TestCase):

    def test_environment(self):
        extensions = bulrush.ENVIRONMENT.get('extensions', [])
        self.assertIn('webassets.ext.jinja2.AssetsExtension', extensions)
        self.assertIn('jinja2.ext.with_', extensions)

    def test_filters(self):
        self.assertIn('images', bulrush.FILTERS)
        images = bulrush.FILTERS['images']('<img src="foo.bar.baz">')
        self.assertEqual(images, ['foo.bar.baz'])

    def test_path(self):
        expected = Path(__file__).parent.parent.joinpath('bulrush')
        self.assertEqual(bulrush.PATH, expected.as_posix())
