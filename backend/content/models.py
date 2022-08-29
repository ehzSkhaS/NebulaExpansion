from django.db import models


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
    price = models.FloatField(null=False)

    class Meta:
        db_table = 'product'
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['code']

    def __str__(self):
        return str(self.code)


# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------

class Provider(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    
    class Meta:
        db_table = 'provider'
        verbose_name = "Provider"
        verbose_name_plural = "Providers"
        ordering = ['code']

    def __str__(self):
        return str(self.code)
    
# Enterprise End --------------------------------------------------------------------------------------------------------------------------------------------


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------

class Warehouse(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    products = models.ManyToManyField(Product, through='WarehouseInventory')
    
    class Meta:
        db_table = 'warehouse'
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"
        ordering = ['code']
        
    def __str__(self):
        return str(self.code)

    @property
    def inventory(self):
        inventories = WarehouseInventory.objects.filter(warehouse=self)
        filtered = inventories.values('product', 'quantity')
        return filtered


class WarehouseInventory(Inventory):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'warehouse_inventory'
        verbose_name = "Warehouse Inventory"
        verbose_name_plural = "Warehouses Inventories"
        unique_together = (('warehouse', 'product'),)
        ordering = ['warehouse']

    def __str__(self):
        return str(self.pk)
        
# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

class Unit(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(null=False, max_length=50)
    
    class Meta:
        db_table = 'unit'
        verbose_name = "Unit"
        verbose_name_plural = "Units"
        ordering = ['code']

    def __str__(self):
        return self.code
    
    @property
    def cost_centers(self):
        centers = CostCenter.objects.filter(unit=self)
        filtered = centers.values('code', 'name')      
        return filtered
    
    
class CostCenter(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    unit = models.ForeignKey(Unit, related_name='centers', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CostCenterInventory')

    class Meta:
        db_table = 'cost_center'
        verbose_name = "Cost Center"
        verbose_name_plural = "Cost Centers"
        ordering = ['code']

    def __str__(self):
        return str(self.code)
    
    @property
    def inventory(self):
        inventories = CostCenterInventory.objects.filter(cost_center=self)
        filtered = inventories.values('product', 'quantity')
        return filtered
    

class CostCenterInventory(Inventory):
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'cost_center_inventory'
        verbose_name = "Cost Center Inventory"
        verbose_name_plural = "Cost Centers Inventories"
        unique_together = (('cost_center', 'product'),)
        ordering = ['cost_center']

    def __str__(self):
        return str(self.pk)

# Client End ------------------------------------------------------------------------------------------------------------------------------------------------
