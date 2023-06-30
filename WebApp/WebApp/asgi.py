"""
ASGI config for WebApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# This will serve the project with the ASGI protocol. It works as an interface 
# for asynchronous conections. 

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebApp.settings')

application = get_asgi_application()
