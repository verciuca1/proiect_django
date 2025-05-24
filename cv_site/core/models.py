from django.db import models

# Create your models here.
from django.db import models

class StudentProfile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    photo = models.ImageField(upload_to='profile/')
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    linkedin_url = models.URLField()

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
