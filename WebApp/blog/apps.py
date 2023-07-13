# We're telling Django that this is an App. So it will be correctly handled by the settings.py

from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
