from django.db import models
from users.models import Student

# Create your models here.
class Transaction(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", 'Pending'
        PROCESSING = "PROCESSING", 'Processing'
        AVAILABLE = "AVAILABLE", 'Available'

    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_approved = models.BooleanField()
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.PENDING)
    amount = models.FloatField(max_length=100)