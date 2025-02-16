from django.db import models
from users.models import CustomUser
from django.utils import formats

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="teacher_announcement")

    def __str__(self):
        return self.title
    
    def formatted_date(self):
        return formats.date_format(self.created_on, "Y-d-m")
    
    def data_date(self):
        return self.strftime('%Y-%m-%d')