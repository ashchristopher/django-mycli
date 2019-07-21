# -*- coding: utf-8 -*-

__author__ = 'Ash Christopher'
__email__ = 'ash.christopher@gmail.com'
__version__ = '0.2.0'

import subprocess

from django.db.backends.mysql.base import DatabaseWrapper
from django.db.backends.mysql.client import DatabaseClient


class MyCLIDatabaseClient(DatabaseClient):
    executable_name = 'mycli'

    def runshell(self):
        args = self.__class__.settings_to_cmd_args(self.connection.settings_dict)
        subprocess.check_call(args)

DatabaseWrapper.client_class = MyCLIDatabaseClient
