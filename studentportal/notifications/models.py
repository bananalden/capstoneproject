from django.db import models
from users.models import Student


# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']