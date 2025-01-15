from django.db.models.signals import post_save
from .models import Student, Teacher, StudentProfile, TeacherProfile
from django.dispatch import receiver


@receiver(post_save, sender=Student)
def create_student_profile (sender, instance, created, **kwargs):
    if created and instance.role =="STUDENT":
        profile_data = getattr(instance, 'profile_data',{})
        StudentProfile.objects.get_or_create(student=instance,
                                             course=profile_data.get('course'),
                                             teacher=profile_data.get('teacher')
                                             )

@receiver(post_save, sender=Teacher)
def create_teacher_profile (sender, instance, created, **kwargs):
    if created and instance.role =="TEACHER":
        profile_data = getattr(instance, 'profile_data', {})
        TeacherProfile.objects.get_or_create(teacher=instance,
                                            course=profile_data.get('course'))