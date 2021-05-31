from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'


def validate(username, password):
    if username is None or password is None:
        raise Exception('no data provided')
    User.objects.get(username=username,password=password)
