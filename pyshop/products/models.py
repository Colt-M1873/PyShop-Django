from operator import mod
from pyexpat import model
from unicodedata import name
from django.db import models


# Create your models here.
class Product(models.Model): # models.Model is a class for common interactives with databases
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083) # standard length of url



class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
