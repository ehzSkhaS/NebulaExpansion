from django.db import models


class Inventory(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=4, default=0, verbose_name='cantidad')

    class Meta:
        abstract = True


class Product(models.Model):
    code = models.IntegerField(primary_key=True, verbose_name='código')
    account = models.IntegerField(null=False, verbose_name='cuenta')
    account_sub = models.IntegerField(null=False, verbose_name='sub cuenta')
    description = models.CharField(null=False, max_length=50, verbose_name='descripción')
    unit = models.CharField(null=False, max_length=10, verbose_name='unidad')
    price = models.FloatField(null=False, verbose_name='precio')

    class Meta:
        db_table = 'product'
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['code']

    def __str__(self):
        return str(self.code)


# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------

class Provider(models.Model):
    code = models.IntegerField(primary_key=True, verbose_name='código')
    name = models.CharField(null=False, max_length=50, verbose_name='nombre')

    class Meta:
        db_table = 'provider'
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['code']

    def __str__(self):
        return str(self.code)

# Enterprise End --------------------------------------------------------------------------------------------------------------------------------------------


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------

class Warehouse(models.Model):
    code = models.IntegerField(primary_key=True, verbose_name='código')
    name = models.CharField(null=False, max_length=50, verbose_name='nombre')
    products = models.ManyToManyField(Product, through='WarehouseInventory')

    class Meta:
        db_table = 'warehouse'
        verbose_name = "Almacén"
        verbose_name_plural = "Almacenes"
        ordering = ['code']

    def __str__(self):
        return str(self.code)

    @property
    def inventory(self):
        inventories = WarehouseInventory.objects.filter(warehouse=self)
        filtered = inventories.values('product', 'quantity')
        return filtered


class WarehouseInventory(Inventory):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='almacén')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='producto')

    class Meta:
        db_table = 'warehouse_inventory'
        verbose_name = "Inventario de Almacén"
        verbose_name_plural = "Inventarios de Almacén"
        unique_together = (('warehouse', 'product'),)
        ordering = ['warehouse']

    def __str__(self):
        return str(self.pk)

# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

class Unit(models.Model):
    code = models.CharField(primary_key=True, max_length=15, verbose_name='código')
    name = models.CharField(null=False, max_length=50, verbose_name='nombre')

    class Meta:
        db_table = 'unit'
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"
        ordering = ['code']

    def __str__(self):
        return self.code

    @property
    def cost_centers(self):
        centers = CostCenter.objects.filter(unit=self)
        filtered = centers.values('code', 'name')
        return filtered


class CostCenter(models.Model):
    code = models.IntegerField(primary_key=True, verbose_name='código')
    name = models.CharField(null=False, max_length=50, verbose_name='nombre')
    unit = models.ForeignKey(Unit, related_name='centers', on_delete=models.CASCADE, verbose_name='unidad')
    products = models.ManyToManyField(Product, through='CostCenterInventory')

    class Meta:
        db_table = 'cost_center'
        verbose_name = "Centro de Costo"
        verbose_name_plural = "Centros de Costo"
        ordering = ['code']

    def __str__(self):
        return str(self.code)

    @property
    def inventory(self):
        inventories = CostCenterInventory.objects.filter(cost_center=self)
        filtered = inventories.values('product', 'quantity')
        return filtered


class CostCenterInventory(Inventory):
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE, verbose_name='centro de costo')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='producto')

    class Meta:
        db_table = 'cost_center_inventory'
        verbose_name = "Inventario de Cento de Costo"
        verbose_name_plural = "Inventarios de Centro de Costo"
        unique_together = (('cost_center', 'product'),)
        ordering = ['cost_center']

    def __str__(self):
        return str(self.pk)

# Client End ------------------------------------------------------------------------------------------------------------------------------------------------
