from django.db import models

# Create your models here.
class EmployeeData(models.Model):

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ProductData(models.Model):

    product_name = models.CharField(max_length=200)
    product_id = models.CharField(max_length=200)
    slug_id = models.SlugField(null = True, blank=True)
    manufacture_date = models.DateField(auto_now=True)
