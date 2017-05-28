from json import dumps

from markupsafe import Markup

from .image_extractor import extract_images

_DEFAULT_SCHEMA = {'@context': 'http://schema.org', '@type': 'BlogPosting'}


def generate_jsonld_schema(article, site_url):
    schema = _create_basic_schema(article, site_url)
    schema.update(_DEFAULT_SCHEMA)
    if hasattr(article, 'modified'):
        schema['dateModified'] = article.modified.isoformat()
    if hasattr(article, 'summary'):
        schema['description'] = Markup(article.summary).striptags()
    images = extract_images(article.content)
    if images:
        schema['image'] = _create_image(images[0])
    return dumps(schema)


def _create_basic_schema(article, site_url):
    return {
        'articleSection': article.category.name,
        'author': _create_person(article.author),
        'datePublished': article.date.isoformat(),
        'headline': article.title,
        'mainEntityOfPage': _create_entity(article, site_url),
    }


def _create_image(image_url):
    return {'@type': 'ImageObject', 'url': image_url}


def _create_entity(article, site_url):
    return {'@type': 'WebPage', '@id': '{}/{}'.format(site_url, article.url)}


def _create_person(person):
    return {'@type': 'Person', 'name': person.name}
