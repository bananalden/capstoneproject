from django.db import models

# Create your models here.
class Grades(models.Model):
    student_usn = models.CharField(max=255)
    subject_code = models.CharField(max=255)
    final_grade = models.FloatField()
    semester = models.CharField(max=255)
    year = models.IntegerField()