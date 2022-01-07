from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Users(User, models.Model):
    """ class to define users """
    is_author = models.BooleanField(default=False)