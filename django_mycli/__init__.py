# -*- coding: utf-8 -*-

__author__ = 'Ash Christopher'
__email__ = 'ash.christopher@gmail.com'
__version__ = '0.0.1'

import subprocess

from django.db.backends.mysql import base
from django.db.backends.mysql.client import DatabaseClient
from django.db import connections


class mycliDatabaseClient(DatabaseClient):
    executable_name = 'mycli'

    def runshell(self):
        args = self.settings_to_cmd_args(self.connection.settings_dict)
        subprocess.check_call(args)


base.DatabaseClient = mycliDatabaseClient
base.client_class = mycliDatabaseClient

for conn in connections.all():
    if isinstance(conn.client, DatabaseClient):
        conn.client = mycliDatabaseClient(conn)
