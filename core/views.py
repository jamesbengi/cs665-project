from django.shortcuts import render,redirect
from .import models
from .models import Customers, Menu, Orders, OrdersItem, Trucks
# Create your views here.
def index(request):
    return render(request, 'index.html')
# def menu(request):
#     return render(request, 'menu.html')
def menu(request):
    menu_items = Menu.objects.all()
    context = {
        'menu_item': menu_items
    }

    return render(request, 'menu.html', {'menu_items': menu_items})
def add_menu(request):
    menu = Trucks.objects.all()
    if request.method == 'POST':
        truck= request.POST.get('truck')
        name = request.POST.get('item_name')
        price = request.POST.get('price')
        des = request.POST.get('availability')
        

        menu_item = models.Menu.objects.create(
            item_name=name,
            availability=des,
            price=price,
            truck_id=truck,
            
        )
        menu_item.save()
        return redirect('menu')
    return render(request, 'add_menu.html',{'menu':menu})
def trucks(request):
    trucks = Trucks.objects.all()
    context = {
        'trucks': trucks
    }
    return render(request, 'trucks.html', {'trucks': trucks})
def add_truck(request):
    if request.method == 'POST':
        truck_name = request.POST.get('truck_name')
        truck_location = request.POST.get('location')
        owner = request.POST.get('owner')

        truck = models.Trucks.objects.create(
            name=truck_name,
            current_location=truck_location,
            owner=owner,
        )
        truck.save()
        return redirect('trucks')
    return render(request, 'add_truck.html')
      
def orders(request):
    order = Orders.objects.all()
    return render(request, 'orders.html',{'order': order})