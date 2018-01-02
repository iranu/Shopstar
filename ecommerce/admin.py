from django.contrib import admin

# Register your models here.
from .models import User, Categoryproduct, Product, Producttype, Order, Orderdetail, Attributegroup, Attribute
admin.site.register(User)
admin.site.register(Categoryproduct)
admin.site.register(Producttype)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderdetail)
admin.site.register(Attribute)
admin.site.register(Attributegroup)
