from django.contrib import admin

# Register your models here.
from ecommerce.models import User, Categoryproduct, Product, Producttype, Order, Orderdetail, Attributegroup, \
    Attribute


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    search_fields = ('username', 'email')

admin.site.register(User,UserAdmin)
admin.site.register(Categoryproduct)
admin.site.register(Producttype)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderdetail)
admin.site.register(Attribute)
admin.site.register(Attributegroup)
