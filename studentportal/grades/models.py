from django.db import models

# Create your models here.

class Grades(models.Model):
    student_usn = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    grade_value = models.DecimalField(max_digits=5,decimal_places=2)

    @property
    def sort_year(self):
        try:
            return int(self.year.split('-')[0])
        except (ValueError, AttributeError):
            return 0
    @property 
    def sort_semester(self):
        try:
            return int(''.join(filter(str.isdigit, self.semester)))
        except (ValueError, TypeError):
            return 0

    class Meta:
        unique_together = ('student_usn','subject_code','subject_name','semester','year')
