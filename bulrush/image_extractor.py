from html.parser import HTMLParser


class ImageExtractor(HTMLParser):
    """Class to extract image sources from article content."""

    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self._images = []

    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        for attr, val in attrs:
            if attr == 'src':
                self._images.append(val)
                break

    def feed(self, data):
        super().feed(data)
        return self

    @classmethod
    def images(cls, article_content):
        extractor = cls()
        extractor.feed(article_content)
        return extractor._images
