# Just telling django that "Users" is to be treated as a proper app. 

from django.apps import AppConfig

# In this case, we nead to set the signals our app we'll need (see signals.py)
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals