from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=30)
    address = models.CharField(max_length=3000)
    city = models.CharField(max_length=2500)
    postal_code = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.username
