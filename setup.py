#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'mycli',
    'Django>=1.4',
]

test_requirements = [
    'mycli',
    'Django>=1.4',
]

setup(
    name='django-mycli',
    version='0.0.1',
    description="Database runtime for Django that replaces mysql with mycli.",
    long_description=readme + '\n\n' + history,
    author="Ash Christopher",
    author_email='ash.christopher@gmail.com',
    url='https://github.com/ashchristopher/django-mycli',
    packages=[
        'django_mycli',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='django mycli mysql database',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)