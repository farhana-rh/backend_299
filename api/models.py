from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Meeting(models.Model):  
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="meetings")
    title = models.CharField(max_length=200)  
    datetime = models.DateTimeField()  # Combine date + time  
    link = models.URLField()  # Meeting URL (Zoom/Google Meet)  
    google_drive_folder_id = models.CharField(max_length=500)  # Store folder ID/URL  
    email = models.EmailField(unique=True) 

    def __str__(self):
        return self.title