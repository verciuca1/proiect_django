
from django.contrib import admin

# Register your models here.
from .models import StudentProfile, ContactMessage
from django.contrib import admin

admin.site.register(StudentProfile)
admin.site.register(ContactMessage)