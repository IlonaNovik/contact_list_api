from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """Contact model"""
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    is_professional = models.BooleanField(default=False)

    def __str__(self):
        return self.name
