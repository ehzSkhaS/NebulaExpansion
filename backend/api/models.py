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

    def __str__(self):
        return self.description


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------

class Warehouse(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    code_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    
    class Meta:
        db_table = 'warehouse'
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"

    def __str__(self):
        return self.name
    
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
    code_unit = models.ForeignKey(Unit, to_field='code', on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        db_table = 'cost_center'
        verbose_name = "CostCenter"
        verbose_name_plural = "CostCenters"

    def __str__(self):
        return self.name

# Client End ------------------------------------------------------------------------------------------------------------------------------------------------
    