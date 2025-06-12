from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Meeting(models.Model):  
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to logged-in user  
    title = models.CharField(max_length=200)  
    datetime = models.DateTimeField()  # Combine date + time  
    link = models.URLField()  # Meeting URL (Zoom/Google Meet)  
    google_drive_folder_id = models.CharField(max_length=500)  # Store folder ID/URL  

    def __str__(self):
        return self.title