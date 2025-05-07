from django.db import models
from users.models import CustomUser
import os

# Create your models here.

class Transaction(models.Model):
    class RegistrarStatus(models.TextChoices):
        PENDING = "PENDING", 'Pending'
        PROCESSING = "PROCESSING", 'Processing'
        AVAILABLE = "AVAILABLE", 'Available'
        COMPLETE = "COMPLETE", 'Complete'

    class PaymentPurposeChoice(models.TextChoices):
        TUITION_FEE = "TUITION FEE", "Tuition Fee"
        CERT_GRADES = "CERTIFICATE OF GRADES", "Certificate of Grades"
        CERT_MORALE = "CERTIFICATE OF GOOD MORALE", "Certificate of Good Morale"
        CERT_ENROL = "CERTIFICATE OF ENROLLMENT", "Certificate of Enrollment"
        OTHER = "OTHER", "Other"

    payment_purpose = models.CharField(max_length=255, choices=PaymentPurposeChoice.choices,  null=True)
    payment_purpose_other = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    registrar_status = models.CharField(max_length=255, choices=RegistrarStatus.choices, default=RegistrarStatus.PENDING)
    payment_proof = models.ImageField(upload_to='payments/', null=True, blank=True)

    