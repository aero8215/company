from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^customers$', views.customers, name='customers'),
    url(r'^orders', views.orders, name='orders'),
    url(r'^employees', views.employees, name='employees'),
]