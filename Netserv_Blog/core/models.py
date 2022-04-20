from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="static/profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
 