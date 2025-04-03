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

]