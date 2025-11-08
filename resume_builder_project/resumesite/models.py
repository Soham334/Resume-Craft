# resumesite/models.py

from django.db import models
from django.conf import settings 

# Create your models here.

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    full_name = models.CharField(max_length=100)
    about = models.TextField()
    age = models.IntegerField(null=True, blank=True) # Added null/blank for flexibility
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    skills = models.TextField(help_text="Comma-separated skills")
    languages = models.TextField(help_text="Comma-separated languages")
    
    education1 = models.TextField()
    education2 = models.TextField(blank=True, null=True)
    education3 = models.TextField(blank=True, null=True)
    
    project1 = models.TextField()
    project2 = models.TextField(blank=True, null=True)
    
    experience1 = models.TextField()
    experience2 = models.TextField(blank=True, null=True)
    
    achievements = models.TextField(help_text="Comma-separated achievements")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
