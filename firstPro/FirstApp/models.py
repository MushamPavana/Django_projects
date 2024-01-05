from django.db import models

# Create your models here.
class employee(models.Model):
    username = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)

