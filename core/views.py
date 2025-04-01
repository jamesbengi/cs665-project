from django.shortcuts import render
from .import models
# Create your views here.
def index(request):
    return render(request, 'index.html')
# def menu(request):
#     return render(request, 'menu.html')
def menu(request):
    menu_items = models.Menu.objects.all()
    context = {
        'menu_item': menu_items
    }

    return render(request, 'menu.html', {'menu_items': menu_items})