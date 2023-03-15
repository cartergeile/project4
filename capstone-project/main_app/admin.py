from django.contrib import admin
from . models import Cart, Product, Customer, Payment, OrderPlaced, Wishlist

# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(OrderPlaced)