from django.contrib import admin

# Register your models here.
from . import models


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'qtd_stock')


admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Product, ProductAdmin)
