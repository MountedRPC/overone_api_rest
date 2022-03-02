from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Products(models.Model):
    image = models.ImageField(upload_to='image_products', blank=False)
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False)
    price = models.CharField(max_length=30, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
