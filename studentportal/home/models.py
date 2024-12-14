from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", 'Student'
        FACULTY = "FACULTY", 'Faculty'
        REGISTRAR = "REGISTRAR", 'Registrar'
        CASHIER = "CASHIER", 'Cashier'
        ADMIN = "ADMIN", 'Admin'

    base_role = Role.ADMIN

    USN = models.CharField()
