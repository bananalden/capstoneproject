from django.db import models
from users.models import Student
import os

# Create your models here.
class PaymentPurpose(models.Model):
    payment_purpose = models.CharField()
    payment_price = models.DecimalField(max_digits=10,decimal_places=2)


class Transaction(models.Model):
    class RegistrarStatus(models.TextChoices):
        PENDING = "PENDING", 'Pending'
        PROCESSING = "PROCESSING", 'Processing'
        AVAILABLE = "AVAILABLE", 'Available'

    payment_purpose = models.ForeignKey(PaymentPurpose, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    registrar_status = models.CharField(max_length=255, choices=RegistrarStatus.choices, default=RegistrarStatus.PENDING)
    payment_proof = models.ImageField(upload_to='payments/')

    def save(self, *args, **kwargs):
        if self.image:
            ext = self.image.name.split('.')[-1]
            modified_filename = f"PAYMENT{self.student_id}.{ext}"
            new_path = os.path.join("payments/", modified_filename)

            self.image.name = new_path