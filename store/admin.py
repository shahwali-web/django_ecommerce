from django.contrib import admin
from . models import Customer, Category, Product, Order
# Register your models here.

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)