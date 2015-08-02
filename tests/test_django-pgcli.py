#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import django_mycli  # noqa


class RuntimeTestCase(unittest.TestCase):

    def test_database_client_subclassed(self):
        from django.db.backends.mysql import base

        self.assertEqual(base.DatabaseClient, django_mycli.mycliDatabaseClient)

    def test_database_client_calls_mycli_executable(self):
        from django.db.backends.mysql import base
          
        self.assertEqual(base.DatabaseClient.executable_name, 'mycli')

    def test_old_database_client_set_on_base(self):
        from django.db.backends.mysql import base
        from django.db.backends.mysql.client import DatabaseClient
        
        self.assertEqual(getattr(base, '__old_database_client'), DatabaseClient)

if __name__ == '__main__':
    unittest.main()
