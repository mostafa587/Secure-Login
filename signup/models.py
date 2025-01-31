from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11, unique=True)