from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from course.models import Course

# Create your models here.
class CustomUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.ADMIN) 

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
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='+')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_id.first_name} Profile'

class TeacherProfile(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.teacher_id.first_name} Profile'
