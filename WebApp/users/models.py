from django.db import models
from django.contrib.auth.models import User
from PIL import Image

"""
Creating our Profile model. Each Profile instance has it's respective User instance and an image.

Other Profile's data are in fact User's data

Also, we need a save() function, so the profile can be created and updated
"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile.pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)