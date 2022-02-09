from django.db import models
from django.db.models.deletion import CASCADE

class Product(models.Model):
    code = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    units = [
        ('U', 'unidad'),
        ('Kg', 'kilogramo'),
        ('Lb', 'libra'),
        ('Oz', 'onza'),
        ('m', 'metro'),
        ('cm', 'centimetro'),
        ('mm', 'milimetro'),
        ('L', 'litro'),
        ('mL', 'mililitro')
    ]
    measure_unit = models.CharField(max_length=5, null=False, blank=False, default='U', choices=units)
    price_per_unit = models.FloatField(null=False, blank=False)    
    quantity = models.FloatField()

class Reception_voucher(models.Model):
    voucher_number = models.PositiveSmallIntegerField(primary_key=True)
    date_stamp = models.DateField(null=False, blank=False)
    bill = models.CharField(max_length=15, null=False, blank=False)
    product_code = models.ForeignKey(Product, null=False, blank=False, on_delete=CASCADE)

class Delivery_voucher(models.Model):
    voucher_number = models.PositiveSmallIntegerField(primary_key=True)
    date_stamp = models.DateField(null=False, blank=False)
    product_code = models.ForeignKey(Product, null=False, blank=False, on_delete=CASCADE)

class Return_voucher(models.Model):
    voucher_number = models.PositiveSmallIntegerField(primary_key=True)
    date_stamp = models.DateField(null=False, blank=False)
    product_code = models.ForeignKey(Product, null=False, blank=False, on_delete=CASCADE)

class Provider(models.Model):
    code = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)    
    reception_voucher = models.ForeignKey(Reception_voucher, null=False, blank=False, on_delete=CASCADE)

class Client(models.Model):
    code = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    delivery_voucher = models.ForeignKey(Delivery_voucher, on_delete=CASCADE)
    return_voucher = models.ForeignKey(Return_voucher, on_delete=CASCADE)

class Warehouse(models.Model):
    code = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    delivery_voucher = models.ForeignKey(Delivery_voucher, on_delete=CASCADE)
    return_voucher = models.ForeignKey(Return_voucher, on_delete=CASCADE)
    reception_voucher = models.ForeignKey(Reception_voucher, on_delete=CASCADE)
