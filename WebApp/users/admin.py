# Here, we are importing the admin module from django's library and our Profile model.
# We want to be able to manage the profiles of our web app in the administrator interface

from django.contrib import admin
from .models import Profile

# Here we are registring the profiles on the admin interface
admin.site.register(Profile)
