from django.contrib.auth.models import User
from django.db import models

class BlogUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    github = models.CharField(max_length=300, blank=True, null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user)