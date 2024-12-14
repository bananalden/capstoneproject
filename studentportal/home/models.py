from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=255)
    role = models.CharField(max_length=255)