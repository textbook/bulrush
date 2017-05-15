from setuptools import setup

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
    install_requires=['webassets'],
    license='ISC',
    name='bulrush',
    package_data={
        'bulrush': [
            'templates/*.html',
            'static/css/*.css',
            'static/css/*.less',
        ]
    },
    packages=['bulrush'],
    test_suite='tests',
    url='https://github.com/textbook/bulrush',
    version='0.0.5',
)
