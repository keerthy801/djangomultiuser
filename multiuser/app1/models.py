from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    place=models.TextField(default=' ')
    phone=models.IntegerField(default=0)
    is_admin=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    def __str__(self):
        return self.username
