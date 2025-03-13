from django.db import models

# Create your models here.

class Grades(models.Model):
    student_usn = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
