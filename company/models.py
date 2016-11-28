# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Customers(models.Model):
    customerid = models.IntegerField(db_column='CustomerID', primary_key=True, blank=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    contacttitle = models.CharField(db_column='ContactTitle', max_length=60, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=60, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.companyname


class Employees(models.Model):
    employeeid = models.IntegerField(db_column='EmployeeID', primary_key=True, blank=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=60, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=40, blank=True, null=True)  # Field name made lowercase.
    hiredate = models.CharField(db_column='HireDate', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'
        verbose_name_plural = "Employees"

    def __str__(self):
        return ' '.join([self.firstname, self.lastname])


class Orderdetails(models.Model):
    orderdetailid = models.IntegerField(db_column='OrderDetailID', primary_key=True, blank=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderDetails'
        verbose_name_plural = "OrderDetails"

    def __str__(self):
        return ' - '.join(map(str,[self.orderid, self.orderdetailid]))

class Orders(models.Model):
    orderid = models.IntegerField(db_column='OrderID', primary_key=True, blank=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.IntegerField(db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.CharField(db_column='OrderDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    requireddate = models.CharField(db_column='RequiredDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    shippeddate = models.CharField(db_column='ShippedDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    shipvia = models.IntegerField(db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    freightcharge = models.FloatField(db_column='FreightCharge', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.orderid)

class Shippers(models.Model):
    shipperid = models.IntegerField(db_column='ShipperID', primary_key=True, blank=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shippers'
        verbose_name_plural = "Shippers"

    def __str__(self):
        return self.companyname

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
