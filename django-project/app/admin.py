from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Client)
admin.site.register(models.Product)
