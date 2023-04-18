from django.db import models
# Create your models here.
from django.contrib import admin
class waitlist(models.Model):
    email = models.EmailField(max_length=55)
    social = models.CharField(max_length=60)

admin.site.register(waitlist)