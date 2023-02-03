from django.db import models

# Create your models here.

class Product(models.Model):
    OrderDate = models.DateField()
    Region    = models.CharField(max_length=50)
    City      = models.CharField(max_length=100)
    Category  = models.CharField(max_length=50)
    Product   = models.CharField(max_length=50)
    Quantity  = models.IntegerField()
    UnitPrice = models.FloatField()

    def __str__(self):
        return self.Product