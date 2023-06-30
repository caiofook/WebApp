from django.apps import AppConfig

# We're telling Django that this is an App. So it will be correctly handled by the settings.py

class WebAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WebApp'
