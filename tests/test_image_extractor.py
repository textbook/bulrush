from unittest import TestCase

from bulrush import extract_images


class ImageExtractorTest(TestCase):

    def test_no_image(self):
        result = extract_images('<h1>No images here</h1>')
        self.assertEqual(result, [])

    def test_only_image(self):
        result = extract_images('<img src="hello.world">')
        self.assertEqual(result, ['hello.world'])

    def test_complex_with_images(self):
        result = extract_images('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>Title</title>
        </head>
        <body>
          <div>
            <article>
              <img src="hello.world" alt="First dummy image">
              <p>This is just some text in the article.</p>
              <img src="foo.bar.baz" alt="Second dummy image">
            </article>
          </div>
        </body>
        </html>
        ''')
        self.assertEqual(result, ['hello.world', 'foo.bar.baz'])
