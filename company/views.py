from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers, Orders, Employees

# Create your views here.
def customers(request):
    customers = Customers.objects.all()
    context = {'customers': customers}
    return render(request,"company/customers.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def orders(request):
    orders = Orders.objects.all()
    context = {'orders': orders}
    return render(request,"company/orders.html", context)

def employees(request):
    employees = Employees.objects.all()
    context = {'employees': employees}
    return render(request,"company/employees.html", context)