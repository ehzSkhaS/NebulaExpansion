from itertools import product
from django.db import models
from django.core.exceptions import ValidationError


class Inventory(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    
    class Meta:
        abstract = True


class Product(models.Model):
    code = models.IntegerField(primary_key=True)
    account = models.IntegerField(null=False)
    account_sub = models.IntegerField(null=False)
    description = models.CharField(null=False, max_length=50)
    unit = models.CharField(null=False, max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'api_product'
        verbose_name = "Product"
        verbose_name_plural = "Products"        

    def __str__(self):
        return str(self.code)
    

# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------

class Provider(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    
    class Meta:
        db_table = 'api_provider'
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self):
        return str(self.code)
    
# Enterprise End --------------------------------------------------------------------------------------------------------------------------------------------


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------

class Warehouse(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    products = models.ManyToManyField(Product, through='WarehouseInventory')
    
    class Meta:
        db_table = 'api_warehouse'
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"

    def __str__(self):
        return str(self.code)


class WarehouseInventory(Inventory):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'api_warehouse_inventory'
        verbose_name = "Warehouse Inventory"
        verbose_name_plural = "Warehouse Inventories"
        unique_together = (('warehouse', 'product'),)

    def __str__(self):
        return str(self.pk)
        
# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

class Unit(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(null=False, max_length=50)
    
    class Meta:
        db_table = 'api_unit'
        verbose_name = "Unit"
        verbose_name_plural = "Units"

    def __str__(self):
        return self.code
    
    
class CostCenter(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CostCenterInventory')

    class Meta:
        db_table = 'api_cost_center'
        verbose_name = "Cost Center"
        verbose_name_plural = "Cost Centers"

    def __str__(self):
        return str(self.code)
    

class CostCenterInventory(Inventory):
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_cost_center_inventory'
        verbose_name = "Cost Center Inventory"
        verbose_name_plural = "Cost Center Inventories"
        unique_together = (('cost_center', 'product'),)

    def __str__(self):
        return str(self.pk)

# Client End ------------------------------------------------------------------------------------------------------------------------------------------------


# Operations ------------------------------------------------------------------------------------------------------------------------------------------------

class Order(models.Model):    
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    existence = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class DeliverySC208(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    request_voucher_1 = models.IntegerField(null=False)
    request_voucher_2 = models.IntegerField(null=False)
    request_plan = models.IntegerField(null=False)    
    date_stamp = models.DateField(auto_now=True, editable=False)
    warehouse_dispatcher = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    cost_center_receiver = models.DecimalField(max_digits=11, decimal_places=0, null=False)    
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)   
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_delivery_sc_2_08'
        verbose_name = "Delivery SC-2-08"
        verbose_name_plural = "Deliveries SC-2-08"

    def __str__(self):
        return str(self.voucher)
    
    
class DeliveryListSC208(Order):
    delivery = models.ForeignKey(DeliverySC208, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'api_delivery_list_sc_2_08'
        verbose_name = "Delivery List SC-2-08"
        verbose_name_plural = "Delivery Lists SC-2-08"
        unique_together = (('delivery', 'product'),)
        
    def __str__(self):
        return str(self.pk)
        
    def clean(self):
        warehouse = DeliverySC208.objects.get(
            voucher = self.delivery.voucher
        ).warehouse
        cost_center = DeliverySC208.objects.get(
            voucher = self.delivery.voucher
        ).cost_center
        
        def validate_quantity():
            quantity_w = WarehouseInventory.objects.get(
                product = self.product,
                warehouse = warehouse
            ).quantity            
            
            if quantity_w >= self.quantity :
                self.existence = quantity_w
            
                WarehouseInventory.objects.update(
                    product = self.product,
                    warehouse = warehouse,
                    quantity = quantity_w - self.quantity
                )
                
                exists = CostCenterInventory.objects.filter(
                    product=self.product,
                    cost_center=cost_center
                ).exists()
                
                if exists:
                    quantity_cc = CostCenterInventory.objects.get(
                        product = self.product,
                        cost_center = cost_center
                    ).quantity
                    
                    CostCenterInventory.objects.update(
                        product = self.product,
                        cost_center = cost_center,
                        quantity = quantity_cc + self.quantity
                    )
                else:
                    CostCenterInventory.objects.create(
                        product=self.product,
                        cost_center=cost_center,
                        quantity=self.quantity
                    )
            else :
                raise ValidationError({'quantity': 'delivery quantity must be less or equal to stored quantity'})
        
        validate_quantity()
     
    
class DevolutionSC208(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    warehouse_receiver = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    cost_center_dispatcher = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_devolution_sc_2_08'
        verbose_name = "Devolution SC-2-08"
        verbose_name_plural = "Devolutions SC-2-08"

    def __str__(self):
        return str(self.voucher)


class DevolutionListSC208(Order):
    devolution = models.ForeignKey(DevolutionSC208, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_devolution_list_sc_2_08'
        verbose_name = "Devolution List SC-2-08"
        verbose_name_plural = "Devolution Lists SC-2-08"
        unique_together = (('devolution', 'product'),)
        
    def __str__(self):
        return str(self.pk)
    
    def clean(self):
        warehouse = DevolutionSC208.objects.get(
            voucher = self.devolution.voucher
        ).warehouse
        cost_center = DevolutionSC208.objects.get(
            voucher = self.devolution.voucher
        ).cost_center
        
        def validate_quantity():
            quantity_w = WarehouseInventory.objects.get(
                product = self.product,
                warehouse = warehouse
            ).quantity            
            quantity_cc = CostCenterInventory.objects.get(
                product = self.product,
                cost_center = cost_center
            ).quantity
            
            if quantity_cc >= self.quantity :
                self.existence = quantity_w
            
                WarehouseInventory.objects.update(
                    product = self.product,
                    warehouse = warehouse,
                    quantity = quantity_w + self.quantity
                )
                
                CostCenterInventory.objects.update(
                    product = self.product,
                    cost_center = cost_center,
                    quantity = quantity_cc - self.quantity
                )
            else :
                raise ValidationError({'quantity': 'devolution quantity must be less or equal to stored quantity'})
        
        validate_quantity()
    
    
class AdjustSC216(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    concept = models.CharField(null=False, max_length=255)
    store_manager = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    inventory_manager = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'api_adjust_sc_2_16'
        verbose_name = "Adjust SC-2-16"
        verbose_name_plural = "Adjusts SC-2-16"

    def __str__(self):
        return str(self.voucher)
    

class AdjustListSC216(Order):
    adjust = models.ForeignKey(AdjustSC216, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_adjust_list_sc_2_16'
        verbose_name = "Adjust List SC-2-16"
        verbose_name_plural = "Adjust Lists SC-2-16"
        unique_together = (('adjust', 'product'),)
        
    def __str__(self):
        return str(self.pk)
    
    def clean(self):
        warehouse = AdjustSC216.objects.get(
            voucher = self.adjust.voucher
        ).warehouse
        
        def validate_quantity():
            quantity = WarehouseInventory.objects.get(
                product = self.product,
                warehouse = warehouse
            ).quantity
            
            if quantity >= self.quantity or self.quantity < 0:
                self.existence = quantity
            
                WarehouseInventory.objects.update(
                    product = self.product,
                    warehouse = warehouse,
                    quantity = self.existence - self.quantity
                )
            else :
                raise ValidationError({'quantity': 'adjust quantity must be less or equal to stored quantity'})
        
        validate_quantity()

class ReceptionSC204(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    bill_number = models.CharField(null=False, max_length=255)
    warehouse_receiver = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    store_manager = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    driver = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_reception_sc_2_04'
        verbose_name = "Reception SC-2-04"
        verbose_name_plural = "Receptions SC-2-04"

    def __str__(self):
        return str(self.voucher)
    

class ReceptionListSC204(Order):
    reception = models.ForeignKey(ReceptionSC204, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_reception_list_sc_2_04'
        verbose_name = "Reception List SC-2-04"
        verbose_name_plural = "Recepton Lists SC-2-04"
        unique_together = (('reception', 'product'),)
        
    def __str__(self):
        return str(self.pk)
    
    def clean(self):
        warehouse = ReceptionSC204.objects.get(
            voucher = self.reception.voucher
        ).warehouse
        
        def validate_quantity():
            exists = WarehouseInventory.objects.filter(
                product=self.product,
                warehouse=warehouse
            ).exists()
        
            if exists :
                self.existence = WarehouseInventory.objects.get(
                    product = self.product,
                    warehouse = warehouse
                ).quantity
                
                WarehouseInventory.objects.update(
                    product = self.product,
                    warehouse = warehouse,
                    quantity = self.quantity + self.existence
                )        
            else :
                WarehouseInventory.objects.create(
                    product=self.product,
                    warehouse=warehouse,
                    quantity=self.quantity
                )
        
        validate_quantity()
        
# Operations End --------------------------------------------------------------------------------------------------------------------------------------------