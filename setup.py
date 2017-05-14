from setuptools import setup

setup(
    author='Jonathan Sharpe',
    author_email='mail@jonrshar.pe',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pelican :: Themes',
        'Programming Language :: Python :: 3 :: Only',
    ],
    description='Bulrush theme for Pelican',
    install_requires=['webassets'],
    license='License :: OSI Approved :: ISC License (ISCL)',
    name='bulrush',
    package_data={
        'bulrush': [
            'templates/*.html',
            'static/css/*.css',
            'static/css/*.less',
        ]
    },
    packages=['bulrush'],
    url='https://github.com/textbook/bulrush',
    version='0.0.2',
)
