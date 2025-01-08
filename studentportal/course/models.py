from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Semester(models.Model):
    class SemNumber(models.TextChoices):
        SEM_1 = "SEM1",'1st Semester'
        SEM_2 = "SEM2", '2nd Semester'
    semester_code = models.CharField(max_length=100, null=True)
    semester = models.CharField(choices=SemNumber.choices)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.CharField(max_length=25, null=False,blank=False)
    def __str__(self):
        return self.semester_code

class Subject(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Grades(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    grade = models.FloatField(max_length=25)