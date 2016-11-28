from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customers)
admin.site.register(Employees)
admin.site.register(Shippers)
admin.site.register(Orders)
admin.site.register(Orderdetails)
