from django.contrib import admin
from .models import EmployeeData, ProductData

# Register your models here.
admin.site.register(EmployeeData)
admin.site.register(ProductData)
