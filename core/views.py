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
def add_order(request):
    trucks = Trucks.objects.all()
    customers= Customers.objects.all()
    if request.method == 'POST':
        truck= request.POST.get('truck')
        customer= request.POST.get('customer')
        status = request.POST.get('status')
        price= request.POST.get('price')

        order = Orders.objects.create(
            customer_id=customer,
            truck_id=truck,
            status=status,
            total_price=price,
        )
        order.save()


        return redirect('orders')
    return render(request, 'add_order.html', {'trucks': trucks, 'customers': customers})
def customers(request):
    customers = Customers.objects.all()
    return render(request, 'customers.html',{'customers': customers})
def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('customer_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')

        customer = models.Customers.objects.create(
            name=name,
            email=email,
            phone_no=phone_number,
        )
        customer.save()
        return redirect('customers')
    return render(request, 'add_customer.html')
def delete_customer(request,customer_id):
    customer = Customers.objects.get(customer_id=customer_id)
    print(customer_id)
    customer.delete()
    return redirect('customers')
def delete_menu(request, menu_id):
    menu = Menu.objects.get(item_id=menu_id)
    menu.delete()
    return redirect('menu')
def delete_truck(request, truck_id):
    truck = Trucks.objects.get(truck_id=truck_id)
    truck.delete()
    return redirect('trucks')
def delete_order(request, order_id):
    order = Orders.objects.get(order_id=order_id)
    order.delete()
    return redirect('orders')
def update_customer(request, customer_id):
    customer = Customers.objects.get(customer_id=customer_id)
    if request.method == 'POST':
        customer.name = request.POST.get('customer_name')
        customer.email = request.POST.get('email')
        customer.phone_no = request.POST.get('phone')
        customer.save()
        return redirect('customers')
    return render(request, 'update_customer.html', {'customer': customer})
def update_menu(request, menu_id):
    menu = Menu.objects.get(item_id=menu_id)
    truck=Trucks.objects.all()
    if request.method == 'POST':
        menu.truck = request.POST.get('truck')
        menu.item_name = request.POST.get('item_name')
        menu.price = request.POST.get('price')
        menu.availability = request.POST.get('availability')
        menu.save()
        return redirect('menu')
    return render(request, 'update_menu.html', {'menu': menu, 'truck': truck})
def update_truck(request, truck_id):
    truck = Trucks.objects.get(truck_id=truck_id)
    if request.method == 'POST':
        truck.name = request.POST.get('truck_name')
        truck.current_location = request.POST.get('location')
        truck.owner = request.POST.get('owner')
        truck.save()
        return redirect('trucks')
    return render(request, 'update_truck.html', {'truck': truck})