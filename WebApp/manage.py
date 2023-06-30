#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""
The function "execute_from_command_line( )" gets arguments passed from the 
  command line (sys.argv) and, from this, starts Django's command line manager.

This allows the execution of administrative tasks from command line, like start 
  the server (python manage.py runserver), make migrations (... makemigrations; 
  .... migrate) and others.

The snippet "if __name__ == '__main__':" is a Python convention with the purpose 
  of identifying if the project is being executed directly (it is the case) or if 
  it's being imported by other project as a module.  "__name__" is a special variable 
  witch indicates the name of the module on which the code is being executed. 
  So, if we go to the therminal an use: python manage.py runserver, we are executing it 
  directly and "__name__" will be "__main__".

If it's being imported by other module/project, the manage.py will not execute "main( )" 
(instead, this will be executed by the main module that imported our WebApp project).

"""


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebApp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

