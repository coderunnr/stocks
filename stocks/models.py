from django.db import models

# Create your models here.

class MainCategory(models.Model):
    name = models.CharField(max_length=100)

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    maincat = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    quantity = models.IntegerField()
    subcat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)        
