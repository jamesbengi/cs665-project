from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Customers'


class Menu(models.Model):
    item_id = models.AutoField(primary_key=True, blank=True, null=False)
    truck = models.ForeignKey('Trucks', models.DO_NOTHING, blank=True, null=True)
    item_name = models.CharField(blank=True, null=True, max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    availability = models.TextField()

    class Meta:
        managed = False
        db_table = 'Menu'
    def __str__(self):
        return self.item_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True, blank=True, null=False)
    truck = models.ForeignKey('Trucks', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    status = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Orders'


class OrdersItem(models.Model):
    orders_item_id = models.AutoField(primary_key=True, blank=True, null=False)
    order = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Menu, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField()
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Orders_item'


class Trucks(models.Model):
    truck_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    current_location = models.CharField(blank=True, null=True,max_length=255)

    class Meta:
        managed = False
        db_table = 'Trucks'