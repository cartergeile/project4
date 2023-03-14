from django.contrib import admin
from . models import Cart, Product, Customer

# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)