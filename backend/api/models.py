from django.db import models

# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------

class Provider(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    
    class Meta:
        db_table = 'provider'
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self):
        return self.name
    
# Enterprise End --------------------------------------------------------------------------------------------------------------------------------------------

    
class Product(models.Model):
    code = models.IntegerField(primary_key=True)
    code_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    account = models.IntegerField(null=False)
    account_sub = models.IntegerField(null=False)
    description = models.CharField(null=False, max_length=50)
    unit = models.CharField(null=False, max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'product'
        verbose_name = "Product"
        verbose_name_plural = "Products"
        unique_together = (('code', 'code_provider'),)

    def __str__(self):
        return self.description


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------

class Warehouse(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    
    class Meta:
        db_table = 'warehouse'
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"

    def __str__(self):
        return self.name


class WarehouseInventory(models.Model):
    number_warehouse = models.ForeignKey(Warehouse, primary_key=True, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)
    code_provider = models.ForeignKey(Product, to_field='code_provider', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    
    class Meta:
        db_table = 'warehouse_inventory'
        verbose_name = "WarehouseInventory"
        verbose_name_plural = "WarehouseInventories"
        unique_together = (('code_product', 'code_provider'),)
        unique_together = (('number_warehouse', 'code_product', 'code_provider'),)

    def __str__(self):
        return "warehouse number: " + self.number_warehouse + " " +  "code product: " + self.code_product + " " + "code provider: " + self.code_provider
    
# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

class Unit(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(null=False, max_length=50)
    
    class Meta:
        db_table = 'unit'
        verbose_name = "Unit"
        verbose_name_plural = "Units"

    def __str__(self):
        return self.name
    
    
class CostCenter(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    code_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cost_center'
        verbose_name = "CostCenter"
        verbose_name_plural = "CostCenters"

    def __str__(self):
        return self.name

class CostCenterInventory(models.Model):
    code_cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE)
    #code_product = models.ForeignKey(Product, to_field='code', related_name='costcenterinventory_product_related', related_query_name='costcenterinventory_product', on_delete=models.CASCADE)
    #code_provider = models.ForeignKey(Product, to_field='code_provider', related_name='costcenterinventory_product_related', related_query_name='costcenterinventory_product', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)    
    
    class Meta:
        db_table = 'cost_center_inventory'
        verbose_name = "CostCenterInventory"
        verbose_name_plural = "CostCenterInventories"
        #unique_together = (('code_product', 'code_provider'),)
        #unique_together = (('code_cost_center', 'code_product', 'code_provider'),)

    #def __str__(self):
     #   return "code cost center: " + self.code_cost_center + " " +  "code product: " + self.code_product + " " + "code provider: " + self.code_provider

# Client End ------------------------------------------------------------------------------------------------------------------------------------------------
    