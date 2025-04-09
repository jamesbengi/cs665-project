from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('add_menu/', views.add_menu, name='add_menu'),
    path('trucks/', views.trucks, name='trucks'),
    path('add_truck/', views.add_truck, name='add_truck'),
    path('orders/', views.orders, name='orders'),
    path('add_order/', views.add_order, name='add_order'),
    path('customers/', views.customers, name='customers'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('delete_menu/<int:menu_id>/', views.delete_menu, name='delete_menu'),
    path('delete_truck/<int:truck_id>/', views.delete_truck, name='delete_truck'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),  
    path('update_customer/<int:customer_id>/', views.update_customer, name='update_customer'),
    path('update_menu/<int:menu_id>/', views.update_menu, name='update_menu'),
    path('update_truck/<int:truck_id>/', views.update_truck, name='update_truck'),
    path('run_raw_sql/', views.run_raw_sql, name='run_raw_sql'),

]