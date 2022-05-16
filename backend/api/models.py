from django.db import models

class Inventory(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    
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
        return self.description
    

# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------

class Provider(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    
    class Meta:
        db_table = 'api_provider'
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self):
        return self.name


class ProviderInventory(Inventory):
    code_provider = models.ForeignKey(Provider, to_field='code', primary_key=True, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)    

    class Meta:        
        db_table = 'api_provider_inventory'
        verbose_name = "ProviderInventory"
        verbose_name_plural = "ProviderInventories"
        unique_together = (('code_provider', 'code_product'),)
        
    def __str__(self):
        return self.quantity
    
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
        return self.name


class WarehouseInventory(Inventory):
    code_warehouse = models.ForeignKey(Warehouse, to_field='code', primary_key=True, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'api_warehouse_inventory'
        verbose_name = "WarehouseInventory"
        verbose_name_plural = "WarehouseInventories"
        unique_together = (('code_warehouse', 'code_product'),)

    def __str__(self):
        return self.quantity
        
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
        return self.name
    
    
class CostCenter(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    code_unit = models.ForeignKey(Unit, to_field='code', on_delete=models.CASCADE)    

    class Meta:
        db_table = 'api_cost_center'
        verbose_name = "CostCenter"
        verbose_name_plural = "CostCenters"

    def __str__(self):
        return self.name
    

class CostCenterInventory(Inventory):
    code_cost_center = models.ForeignKey(CostCenter, to_field='code', primary_key=True, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_cost_center_inventory'
        verbose_name = "CostCenterInventory"
        verbose_name_plural = "CostCenterInventories"
        unique_together = (('code_cost_center', 'code_product'),)

    def __str__(self):
        return self.quantity

# Client End ------------------------------------------------------------------------------------------------------------------------------------------------


# Operations ------------------------------------------------------------------------------------------------------------------------------------------------

class Order(models.Model):    
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    existence = models.DecimalField(max_digits=10, decimal_places=4)
    order_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class DeliverySC208(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    request_voucher_1 = models.IntegerField(null=False)
    request_voucher_2 = models.IntegerField(null=False)
    request_plan = models.IntegerField(null=False)    
    date_stamp = models.DateField(auto_now=True, editable=False)    
    ci_cost_center_receiver = models.IntegerField(null=False)
    ci_warehouse_dispatcher = models.IntegerField(null=False)   
    order_warehouse_inventory = models.ForeignKey(WarehouseInventory, to_field='code_warehouse', on_delete=models.CASCADE)   
    order_cost_center_inventory = models.ForeignKey(CostCenterInventory, to_field='code_cost_center', on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_delivery_sc_2_08'
        verbose_name = "DeliverySC208"
        verbose_name_plural = "DeliverySC208s"

    def __str__(self):
        return self.voucher
    
    
class DeliveryListSC208(Order):
    delivery_voucher = models.ForeignKey(DeliverySC208, to_field='voucher', primary_key=True, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_delivery_list_sc_2_08'
        verbose_name = "DeliveryListSC208"
        verbose_name_plural = "DeliveryListSC208s"
        unique_together = (('delivery_voucher', 'order_product'),)
        
    def __str__(self):
        return self.quantity
    
    
class DevolutionSC208(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    ci_cost_center_dispatcher = models.IntegerField(null=False)
    ci_warehouse_receiver = models.IntegerField(null=False)
    order_warehouse_inventory = models.ForeignKey(WarehouseInventory, to_field='code_warehouse', on_delete=models.CASCADE)
    order_cost_center_inventory = models.ForeignKey(CostCenterInventory, to_field='code_cost_center', on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_devolution_sc_2_08'
        verbose_name = "DevolutionSC208"
        verbose_name_plural = "DevolutionSC208s"

    def __str__(self):
        return self.voucher


class DevolutionListSC208(Order):
    devolution_voucher = models.ForeignKey(DevolutionSC208, to_field='voucher', primary_key=True, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_devolution_list_sc_2_08'
        verbose_name = "DevolutionListSC208"
        verbose_name_plural = "DevolutionListSC208s"
        unique_together = (('devolution_voucher', 'order_product'),)
        
    def __str__(self):
        return self.quantity
    
    
class AdjustSC216(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    concept = models.CharField(null=False, max_length=255)
    ci_store_manager = models.IntegerField(null=False)
    ci_inventory_manager = models.IntegerField(null=False)
    order_warehouse_inventory = models.ForeignKey(WarehouseInventory, to_field='code_warehouse', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'api_adjust_sc_2_16'
        verbose_name = "AdjustSC216"
        verbose_name_plural = "AdjustSC216s"

    def __str__(self):
        return self.voucher
    

class AdjustListSC216(Order):
    adjust_voucher = models.ForeignKey(AdjustSC216, to_field='voucher', primary_key=True, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_adjust_list_sc_2_16'
        verbose_name = "AdjustListSC216"
        verbose_name_plural = "AdjustListSC216s"
        unique_together = (('adjust_voucher', 'order_product'),)
        
    def __str__(self):
        return self.quantity


class ReceptionSC204(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    bill_number = models.CharField(null=False, max_length=255)
    ci_warehouse_receiver = models.IntegerField(null=False)
    ci_store_manager = models.IntegerField(null=False)
    ci_driver = models.IntegerField(null=False)
    order_warehouse_inventory = models.ForeignKey(WarehouseInventory, to_field='code_warehouse', on_delete=models.CASCADE)
    order_provider_inventory = models.ForeignKey(ProviderInventory, to_field='code_provider', on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_reception_sc_2_04'
        verbose_name = "ReceptionSC204"
        verbose_name_plural = "ReceptionSC204s"

    def __str__(self):
        return self.voucher
    

class ReceptionListSC216(Order):
    reception_voucher = models.ForeignKey(ReceptionSC204, to_field='voucher', primary_key=True, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_reception_list_sc_2_04'
        verbose_name = "ReceptionListSC204"
        verbose_name_plural = "ReceptonListSC204s"
        unique_together = (('reception_voucher', 'order_product'),)
        
    def __str__(self):
        return self.quantity

# Operations End --------------------------------------------------------------------------------------------------------------------------------------------