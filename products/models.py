from django.db import models

# Create your models here.
class Nevin(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    stock=models.IntegerField()
    desc=models.CharField(max_length=5000)
    image=models.CharField(max_length=10000)