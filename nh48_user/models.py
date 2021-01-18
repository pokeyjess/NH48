from django.contrib.auth.models import AbstractUser
from django.db import models

class NHUser(AbstractUser):
    bio = models.TextField(null=True, blank=True, verbose_name="About Me")
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    joined_date = models.DateField(auto_now_add=True)
    
    # follows = models.ManyToManyField("self", symmetrical=False)
