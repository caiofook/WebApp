from django.db import models
from django.contrib.auth.models import User


class UserHabits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracker_data = models.TextField()
    
    def __str__(self):
        return f'{self.user.username} - Tracker Data'