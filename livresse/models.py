from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    name = models.CharField(max_length=30)
    idName = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    admin = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

class Category(models.Model):
    nome = models.CharField(max_length=256)

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    # img1 = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    # img2 = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    # img3 = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    # img4 = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    add_dthr = models.DateTimeField(auto_now=False, auto_now_add=True)

class Buy(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    dt_hr = models.DateTimeField(auto_now=False, auto_now_add=True)

class Desire(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)

class PutBook(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    dt_hr = models.DateTimeField(auto_now=False, auto_now_add=True)
    
class CatBook(models.Model):
    id_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
