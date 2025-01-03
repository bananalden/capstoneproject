from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUser(AbstractUser):
    
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        REGISTRAR = "REGISTRAR", 'Registrar'
        CASHIER = "CASHIER", 'Cashier'
        TEACHER = "TEACHER", 'Teacher'
        STUDENT = "STUDENT", 'Student'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50 ,choices=Role.choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class RegistrarManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.REGISTRAR) 


class Registrar(CustomUser):
    base_role = CustomUser.Role.REGISTRAR
    registrar = RegistrarManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Registrar"
    
class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.TEACHER) 


class Teacher(CustomUser):
    base_role = CustomUser.Role.TEACHER
    registrar = RegistrarManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Teacher"
    

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.STUDENT) 


class Student(CustomUser):
    base_role = CustomUser.Role.STUDENT
    student = StudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Students"
    
    
class CashierManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.CASHIER) 

class Cashier(CustomUser):
    base_role = CustomUser.Role.CASHIER

    cashier = CashierManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Cashier"