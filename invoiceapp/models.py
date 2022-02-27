from unicodedata import name
from django.db import models

# class Product(models.Model):
#     product_name = models.TextField()
#     date =models.DateField(auto_now=True)
#     quantity = models.IntegerField()
#     price = models.IntegerField()

class Invoice(models.Model):
    client_name = models.CharField(max_length=255)
    product_name = models.TextField()
    date =models.DateField(auto_now=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    sub_total = models.IntegerField()
    Payment_method = models.TextField(null=True,blank=True)
    Shipping_charge = models.IntegerField()
    total = models.IntegerField()
    notes =models.TextField(null=True,blank=True)

