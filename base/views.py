from django.http import HttpResponse
from django.shortcuts import render
from .models import EmployeeData, ProductData

# Create your views here.

def home(request):

    employee_info = EmployeeData.objects.order_by('-employee_id')
    output = ' , '.join([e.first_name for e in employee_info])
    return HttpResponse(output)
 