# -*- coding: utf-8 -*-

__author__ = 'Ash Christopher'
__email__ = 'ash.christopher@gmail.com'
__version__ = '0.0.1'


from django.db.backends.mysql import base
from django.db.backends.mysql.client import DatabaseClient


class mycliDatabaseClient(DatabaseClient):
    executable_name = 'mycli'

base.__old_database_client = base.DatabaseClient
base.DatabaseClient = mycliDatabaseClient
