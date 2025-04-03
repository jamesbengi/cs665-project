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

      
   