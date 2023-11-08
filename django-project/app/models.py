from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField('Name of Product', max_length=200)
    price = models.DecimalField('Price', decimal_places=2, max_digits=10)
    qtd_stock = models.IntegerField('Quantity in Stock')
