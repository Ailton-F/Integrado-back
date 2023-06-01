from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    img = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    add_dthr = models.DateTimeField(auto_now=False, auto_now_add=True)
