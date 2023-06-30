"""
Here, we're creating the forms to register the user and update it's profile.
The profile-only attribute that a user can change is the profile picture.
The other infos are directly related to the user, not the profile
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# From django's default UserRegisterForm, we want also an email field
class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField() # empty is required = true.

    class Meta: # we need to explain django which Models and attributes will be affected
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

# Here, the "update profile" forms. But the attributes "username" and "email" belongs to User (not "Profile")
# These two forms will be implemented in a way that the user will see only 1 thing
class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField() 
     class Meta: 
        model = User 
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']