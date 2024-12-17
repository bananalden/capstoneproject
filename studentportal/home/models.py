from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have email address")
        
        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
    
class CustomUser(AbstractUser):
    
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        STUDENT = "STUDENT", 'Student'
        REGISTRAR = "REGISTRAR", 'Registrar'
        CASHIER = "CASHIER", 'Cashier'
        FACULTY = "FACULTY", 'Faculty'


    role = models.CharField(max_length=50 ,choices=Role.choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    


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

@receiver(post_save, sender = Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role =="STUDENT":
        StudentProfile.objects.create(studentID=instance)


class StudentProfile(models.Model):
    studentID = models.OneToOneField(CustomUser, on_delete=models.CASCADE)



class FacultyManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.FACULTY) 

class Faculty(CustomUser):
    base_role = CustomUser.Role.FACULTY

    faculty = FacultyManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Faculty"
    
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

class RegistrarManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.REGISTRAR) 

class Registrar(CustomUser):
    base_role = CustomUser.Role.REGISTRAR

    cashier = RegistrarManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Registrar"
    
