from unicodedata import name
from django.db import models

class Invoice(models.Model):
    name=models.CharField(max_length=100)
    date =models.DateField(auto_now=True)
    quantity
    product_name 
    price =
    total_price =
    sub_total =
    Payment_method =
    Shipping_charge =
    total =
    notes =models.TextField(null=True,blank=True)


