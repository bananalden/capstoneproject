from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        STUDENT = "STUDENT", 'Student'
        REGISTRAR = "REGISTRAR", 'Registrar'
        CASHIER = "CASHIER", 'Cashier'
        FACULTY = "FACULTY", 'Faculty'
    
    base_role = Role.ADMIN

    role = models.CharField(max_length=50 ,choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT) 

class Student(User):
    base_role = User.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Students"

@receiver(post_save, sender = Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role =="STUDENT":
        StudentProfile.objects.create(studentID=instance)


class StudentProfile(models.Model):
    studentID = models.OneToOneField(User, on_delete=models.CASCADE)



class FacultyManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.FACULTY) 

class Faculty(User):
    base_role = User.Role.FACULTY

    faculty = FacultyManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Faculty"
    
class CashierManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CASHIER) 

class Cashier(User):
    base_role = User.Role.CASHIER

    cashier = CashierManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Cashier"

class RegistrarManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.REGISTRAR) 

class Registrar(User):
    base_role = User.Role.REGISTRAR

    cashier = RegistrarManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Registrar"
    
