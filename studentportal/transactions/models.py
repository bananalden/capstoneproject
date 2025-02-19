from django.db import models
from users.models import CustomUser
import os

# Create your models here.
class PaymentPurpose(models.Model):
    payment_purpose = models.CharField()
    payment_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.payment_purpose


class Transaction(models.Model):
    class RegistrarStatus(models.TextChoices):
        PENDING = "PENDING", 'Pending'
        PROCESSING = "PROCESSING", 'Processing'
        AVAILABLE = "AVAILABLE", 'Available'

    payment_purpose = models.ForeignKey(PaymentPurpose, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    registrar_status = models.CharField(max_length=255, choices=RegistrarStatus.choices, default=RegistrarStatus.PENDING)
    payment_proof = models.ImageField(upload_to='media/payments/')

    