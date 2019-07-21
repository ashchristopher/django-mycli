#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import django_mycli  # noqa


class RuntimeTestCase(unittest.TestCase):

    def test_database_client_subclassed(self):
        from django.db.backends.mysql import base

        self.assertEqual(base.DatabaseWrapper.client_class, django_mycli.MyCLIDatabaseClient)

    def test_database_client_calls_mycli_executable(self):
        from django.db.backends.mysql import base

        self.assertEqual(base.DatabaseWrapper.client_class.executable_name, 'mycli')


if __name__ == '__main__':
    unittest.main()
