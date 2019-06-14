from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))
with open('{}/README.md'.format(here)) as readme:
    long_description = readme.read()

setup(
    author='Jonathan Sharpe',
    author_email='mail@jonrshar.pe',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pelican :: Themes',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3 :: Only',
    ],
    description='Bulrush theme for Pelican',
    install_requires=['markupsafe', 'webassets'],
    license='ISC',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='bulrush',
    package_data={
        'bulrush': [
            'templates/*.html',
            'static/css/*.css',
        ]
    },
    packages=['bulrush'],
    test_suite='tests',
    tests_require=['pelican'],
    url='https://github.com/textbook/bulrush',
    version='0.3.2',
)
