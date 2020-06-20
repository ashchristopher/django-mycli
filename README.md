===============================
django-mycli
===============================

.. image:: https://img.shields.io/travis/ashchristopher/django-mycli.svg
        :target: https://travis-ci.org/ashchristopher/django-mycli

.. image:: https://img.shields.io/pypi/v/django-mycli.svg
        :target: https://pypi.python.org/pypi/django-mycli


Alternate database runtime for Django that replaces mysql with mycli when
calling the Django `dbshell` management command.

* Free software: BSD license

Installation
------------

Installation is as simple as::

    $ pip install django-mycli

Add ``django_mycli`` to your ``INSTALLED_APPS`` setting.

    INSTALLED_APPS = [
        ...,
        'django_mycli',
    ]


Usage
-----
Call the `dbshell` command.

    ./manage.py dbshell
