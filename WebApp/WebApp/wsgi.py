"""
WSGI config for WebApp1Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
# This basically serves the project with the WSGI protocol. It works as an
# interface between the app and the web server.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebApp.settings')

application = get_wsgi_application()
