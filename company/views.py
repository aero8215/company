from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers, Orders, Employees, Shippers


# Create your views here.
def customers(request):
    customers = Customers.objects.all()
    context = {'customers': customers}
    return render(request,"company/customers.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")


def orders(request):
    orders = Orders.objects.all()
    for order in orders:
        order.companyname = Customers.objects.get(pk=order.customerid).companyname
        order.employeename = Employees.objects.get(pk=order.employeeid).fullname
        order.shipcompany = Shippers.objects.get(pk=order.shipvia).companyname
    context = {'orders': orders}
    return render(request,"company/orders.html", context)


def employees(request):
    employees = Employees.objects.all()
    context = {'employees': employees}
    return render(request,"company/employees.html", context)


def employee_detail(request, pk):
    employee = Employees.objects.filter(pk=pk)
    employee_rec = employee[0] if len(employee) else None
    return render(request, 'company/employee_detail.html', {'employee': employee_rec})