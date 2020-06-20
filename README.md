
# django-mycli

[![Build Status](https://travis-ci.org/ashchristopher/django-mycli.svg?branch=master)](https://travis-ci.org/ashchristopher/django-mycli) [![PyPI version](https://badge.fury.io/py/django-mycli.svg)](https://badge.fury.io/py/django-mycli) ![PyPI - License](https://img.shields.io/pypi/l/django-mycli)

Replaces your existing *mysql* cli for MySQL, MariaDB, and Percona with *mycli* which provides enhancements such as auto-completion and syntax highlighting. Visit the [MyCLI website](https://www.mycli.net/) to learn more about the MyCLI client.

## Installation

To install the package:

`$ pip install django-mycli`

Add `django_mycli` to your `INSTALLED_APPS` setting in your settings.py file.

    INSTALLED_APPS = [
        ...,
        'django_mycli',
    ]

## Usage

To use the `mycli` command with your project, call the `dbshell` command.

    ./manage.py dbshell
