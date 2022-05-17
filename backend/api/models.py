from django.db import models
from django.core.exceptions import ValidationError

class Inventory(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    
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


class ProviderInventory(Inventory):
    code_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, on_delete=models.CASCADE)    

    class Meta:
        db_table = 'api_provider_inventory'
        verbose_name = "Provider Inventory"
        verbose_name_plural = "Provider Inventories"
        unique_together = (('code_provider', 'code_product'),)
        
    def __str__(self):
        return str(self.pk)
    
# Enterprise End --------------------------------------------------------------------------------------------------------------------------------------------


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------

class Warehouse(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)    
    
    class Meta:
        db_table = 'api_warehouse'
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"

    def __str__(self):
        return str(self.code)


class WarehouseInventory(Inventory):
    code_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'api_warehouse_inventory'
        verbose_name = "Warehouse Inventory"
        verbose_name_plural = "Warehouse Inventories"
        unique_together = (('code_warehouse', 'code_product'),)

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
    code_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_cost_center'
        verbose_name = "Cost Center"
        verbose_name_plural = "Cost Centers"

    def __str__(self):
        return str(self.code)
    

class CostCenterInventory(Inventory):
    code_cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_cost_center_inventory'
        verbose_name = "Cost Center Inventory"
        verbose_name_plural = "Cost Center Inventories"
        unique_together = (('code_cost_center', 'code_product'),)

    def __str__(self):
        return str(self.pk)

# Client End ------------------------------------------------------------------------------------------------------------------------------------------------


# Operations ------------------------------------------------------------------------------------------------------------------------------------------------

class Order(models.Model):    
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    existence = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class DeliverySC208(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    request_voucher_1 = models.IntegerField(null=False)
    request_voucher_2 = models.IntegerField(null=False)
    request_plan = models.IntegerField(null=False)    
    date_stamp = models.DateField(auto_now=True, editable=False)    
    ci_cost_center_receiver = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    ci_warehouse_dispatcher = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    order_warehouse_inventory = models.ForeignKey(WarehouseInventory, on_delete=models.CASCADE)   
    order_cost_center_inventory = models.ForeignKey(CostCenterInventory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_delivery_sc_2_08'
        verbose_name = "Delivery SC-2-08"
        verbose_name_plural = "Deliveries SC-2-08"

    def __str__(self):
        return str(self.voucher)
    
    
class DeliveryListSC208(Order):
    delivery_voucher = models.ForeignKey(DeliverySC208, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'api_delivery_list_sc_2_08'
        verbose_name = "Delivery List SC-2-08"
        verbose_name_plural = "Delivery Lists SC-2-08"
        unique_together = (('delivery_voucher', 'order_product'),)    
        
    def clean(self):
        delivery_obj = DeliverySC208.objects.get(voucher=self.delivery_voucher)
        #warehouse_inventory_id = delivery_obj.values()['order_warehouse_inventory']
        #cost_center_inventory_id = delivery_obj.values()['order_cost_center_inventory']        
        #warehouse_inventory_obj = WarehouseInventory.objects.filter(pk=warehouse_inventory_id)
        #cost_center_inventory_obj = CostCenterInventory.objects.filter(pk=cost_center_inventory_id)
        
        #if warehouse_inventory_obj.values('quantity')['quantity'] < self.quantity:
        #    raise ValidationError({'quantity': _('Deliver quantity must be less or equal to stored quantity')})
     
    def __str__(self):
        return str(self.pk)
    
    
class DevolutionSC208(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    ci_cost_center_dispatcher = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    ci_warehouse_receiver = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    order_warehouse_inventory = models.ForeignKey(WarehouseInventory, on_delete=models.CASCADE)
    order_cost_center_inventory = models.ForeignKey(CostCenterInventory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_devolution_sc_2_08'
        verbose_name = "Devolution SC-2-08"
        verbose_name_plural = "Devolutions SC-2-08"

    def __str__(self):
        return str(self.voucher)


class DevolutionListSC208(Order):
    devolution_voucher = models.ForeignKey(DevolutionSC208, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_devolution_list_sc_2_08'
        verbose_name = "Devolution List SC-2-08"
        verbose_name_plural = "Devolution Lists SC-2-08"
        unique_together = (('devolution_voucher', 'order_product'),)
        
    def __str__(self):
        return str(self.pk)
    
    
class AdjustSC216(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    concept = models.CharField(null=False, max_length=255)
    ci_store_manager = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    ci_inventory_manager = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    order_warehouse_inventory = models.ForeignKey(WarehouseInventory, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'api_adjust_sc_2_16'
        verbose_name = "Adjust SC-2-16"
        verbose_name_plural = "Adjusts SC-2-16"

    def __str__(self):
        return str(self.voucher)
    

class AdjustListSC216(Order):
    adjust_voucher = models.ForeignKey(AdjustSC216, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_adjust_list_sc_2_16'
        verbose_name = "Adjust List SC-2-16"
        verbose_name_plural = "Adjust Lists SC-2-16"
        unique_together = (('adjust_voucher', 'order_product'),)
        
    def __str__(self):
        return str(self.pk)


class ReceptionSC204(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    bill_number = models.CharField(null=False, max_length=255)
    ci_warehouse_receiver = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    ci_store_manager = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    ci_driver = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    order_warehouse_inventory = models.ForeignKey(WarehouseInventory, on_delete=models.CASCADE)
    order_provider_inventory = models.ForeignKey(ProviderInventory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_reception_sc_2_04'
        verbose_name = "Reception SC-2-04"
        verbose_name_plural = "Receptions SC-2-04"

    def __str__(self):
        return str(self.voucher)
    

class ReceptionListSC204(Order):
    reception_voucher = models.ForeignKey(ReceptionSC204, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_reception_list_sc_2_04'
        verbose_name = "Reception List SC-2-04"
        verbose_name_plural = "Recepton Lists SC-2-04"
        unique_together = (('reception_voucher', 'order_product'),)
        
    def __str__(self):
        return (self.pk)

# Operations End --------------------------------------------------------------------------------------------------------------------------------------------