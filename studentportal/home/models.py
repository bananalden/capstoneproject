from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


# USER MODELS HERE
class User(AbstractBaseUser):
    
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        FACULTY = "FACULTY", "Faculty"
        CASHIER = "CASHIER", "Cashier"
        REGISTRAR = "REGISTRAR", "Registrar"

    role = models.CharField(_('Role'), max_length=255, choices=Roles.choices, default=Roles.ADMIN)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255, blank=False)

    USERNAME_FIELD = 'username'

    def get_absolute_url(self):
        return reverse("users:detail",kwargs={"username": self.username})
    
class StudentTable(User):
    class Meta:
        proxy = True

class CashierTable(User):
    class Meta:
        proxy = True

class FacultyTable(User):
    class Meta:
        proxy = True

class RegistrarTable(User):
    class Meta:
        proxy = True

