from django.db import models


# Create your models here.
class User(AbstractBaseUser):
    
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        FACULTY = "FACULTY", "Faculty"
        CASHIER = "CASHIER", "Cashier"
        REGISTRAR = "REGISTRAR", "Registrar"

    type = models.CharField(_('Type'), max_length=255, choices=Types.choices, default=Types.ADMIN)
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

