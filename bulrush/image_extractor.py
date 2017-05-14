from html.parser import HTMLParser


class ImageExtractor(HTMLParser):
    """Class to extract image sources from article content."""

    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            self._extract_source_attr(attrs)

    def _extract_source_attr(self, attrs):
        self.images.append(next(val for attr, val in attrs if attr == 'src'))


def extract_images(article_content):
    """Extract the sources of all images in the article."""
    extractor = ImageExtractor()
    extractor.feed(article_content)
    return extractor.images
