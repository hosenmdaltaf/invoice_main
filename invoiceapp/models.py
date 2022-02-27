from unicodedata import name
from django.db import models

class Invoice (models.Model):
    client_name = models.CharField(max_length=255,null=True,blank=True)
    total_price = models.IntegerField(null=True,blank=True)
    sub_total = models.IntegerField(null=True,blank=True)
    Payment_method = models.TextField(null=True,blank=True)
    Shipping_charge = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    notes =models.TextField(null=True,blank=True) 
    

class Product(models.Model):
    product_name = models.TextField(null=True,blank=True)
    # date =models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    
    products = models.ForeignKey(Invoice,on_delete=models.CASCADE,null=True,blank=True)
 

