from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)

class Semester(models.Model):
    class SemNumber(models.TextChoices):
        SEM_1 = "SEM1",'1st Semester'
        SEM_2 = "SEM2", '2nd Semester'
    semester = models.CharField(choices=SemNumber.choices)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.CharField(max_length=25, null=False,blank=False)

class Subject(models.Model):
    name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)

class Grades(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    grade = models.FloatField(max_length=25)