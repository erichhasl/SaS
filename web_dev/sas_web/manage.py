#!/usr/bin/env python3
import os
import sys
import import platform


if __name__ == "__main__":
    operating_system = platform.platform
    if operating_system.startswith( "Darwin" ):
        import pymysql
        pymysql.install_as_MySQLdb()
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sas_web.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
