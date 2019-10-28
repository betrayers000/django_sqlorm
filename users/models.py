from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    balance = models.IntegerField()
