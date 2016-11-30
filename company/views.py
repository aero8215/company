from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers, Orders, Employees, Shippers, Orderdetails
from pathlib import Path

# Create your views here.
def customers(request):
    customers = Customers.objects.all()
    context = {'customers': customers}
    context['title'] = Path(request.path).parts[-1].title()
    return render(request,"company/customers.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")


def orders(request):
    orders = Orders.objects.all()
    for order in orders:
        order.companyname = Customers.objects.get(pk=order.customerid).companyname
        order.employeename = Employees.objects.get(pk=order.employeeid).fullname
        order.shipcompany = Shippers.objects.get(pk=order.shipvia).companyname
    context = {'orders': orders}
    context['title']= Path(request.path).parts[-1].title()
    return render(request,"company/orders.html", context)


def employees(request):
    employees = Employees.objects.all()
    context = {'employees': employees}
    context['title'] = Path(request.path).parts[-1].title()
    return render(request,"company/employees.html", context)


def employee_detail(request, pk):
    employee = Employees.objects.filter(pk=pk)
    employee_rec = employee[0] if len(employee) else None
    context = {'employee': employee_rec}
    context['title'] = "employee details".title()
    return render(request, 'company/employee_detail.html', context)

def order_detail(request, pk):
    orders = Orderdetails.objects.filter(orderid=pk)
    context = {'orders': orders}
    context['title'] = "order details".title()
    return render(request, 'company/order_detail.html', context)