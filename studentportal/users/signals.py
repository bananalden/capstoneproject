from django.db.models.signals import post_save
from .models import Student, Teacher, StudentProfile
from django.dispatch import receiver


@receiver(post_save, sender=Student)
def create_student_profile (sender, instance, created, **kwargs):
    if created and instance.role =="STUDENT" and isinstance(instance, Student):
        profile_data = getattr(instance, 'profile_data',{})
        StudentProfile.objects.get_or_create(student=instance,
                                             defaults={
                                                 'course': profile_data.get('course'),
                                                 'date_of_birth': profile_data.get('date_of_birth'),
                                                 'gender': profile_data.get('gender'),
                                                 'address': profile_data.get('address'),
                                                 'date_of_birth': profile_data.get('date_of_birth'),
                                             })

