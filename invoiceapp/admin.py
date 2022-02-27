from django.contrib import admin
from .models import Invoice,Product

# Register your models here.

# class Productadmin(admin.StackedInline):
#     model = Product

# class Productlist(admin.ModelAdmin):
#     list_display = ('product_name','quantity')
#     inlines = [Productadmin]

# admin.site.register(Invoice,Productlist)


class Invoiceadmin(admin.StackedInline):
    model = Product

class Invoicelist(admin.ModelAdmin):
    list_display = ('client_name','notes','Payment_method','Shipping_charge')
    inlines = [Invoiceadmin]

admin.site.register(Invoice,Invoicelist)


