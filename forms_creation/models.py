from django.db import models

# Create your models here.

class StoreData(models.Model):
    name=models.CharField(max_length=200)
    roll=models.CharField(max_length=14)
    branch=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
