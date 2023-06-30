"""
    Here we are setting up signal handlers to automatically create and save a Profile 
instance whenever a new User instance is created or saved.
 
    For this, we need Django's post_save signal, the User model, the receiver decorator 
and our Profile model
"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""
    The receiver decorator watches when a post_save signal is sent by a User object and
triggers the create_profile function. When (if) the user is created, a Profile must be
created and associated with the new user.
"""
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

"""
    This one updates the profile and it's user if is updated
"""
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
 