from pathlib import Path

from .image_extractor import extract_images


ENVIRONMENT = {
    'extensions': ['webassets.ext.jinja2.AssetsExtension', 'jinja2.ext.with_'],
}
"""The required Jinja environment for the Bulrush theme."""


FILTERS = dict(images=extract_images)
"""The filters defined by the Bulrush theme."""


# https://github.com/getpelican/pelican/issues/1564#issuecomment-282136049
PATH = str(Path(__file__).parent)
"""The path to the Bulrush theme directory."""
