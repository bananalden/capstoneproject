from django.db.models.signals import post_save
from .models import Student, Teacher, StudentProfile, TeacherProfile
from django.dispatch import receiver


@receiver(post_save, sender=Student)
def create_student_profile (sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create()