from django.db.models.signals import post_save
from .models import Student, Teacher, StudentProfile, TeacherProfile
from django.dispatch import receiver


@receiver(post_save, sender=Student)
def create_student_profile (sender, instance, created, **kwargs):
    if created and instance.role =="STUDENT":
        StudentProfile.objects.create(user= instance)

@receiver(post_save, sender=Student)
def save_student_profile (sender, instance, created, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Teacher)
def create_teacher_profile (sender, instance, created, **kwargs):
    if created and instance.role =="TEACHER":
        TeacherProfile.objects.create(user=instance)