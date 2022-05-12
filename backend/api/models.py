from django.db import models

# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------

class Provider(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    
    class Meta:
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
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"

    def __str__(self):
        return self.name


class Warehouse_Inventory(models.Model):
    number_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    code_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    
    class Meta:
        verbose_name = "Warehouse_Inventory"
        verbose_name_plural = "Warehouse_Inventories"
        unique_together = (('number_warehouse', 'code_product', 'code_provider'),)

    def __str__(self):
        return "warehouse number: " + self.number_warehouse + " " +  "code product: " + self.code_product + " " + "code provider: " + self.code_provider
    
# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

class Unit(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(null=False, max_length=50)
    
    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"

    def __str__(self):
        return self.name
    
    
class Cost_Center(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    code_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cost_Center"
        verbose_name_plural = "Cost_Centers"

    def __str__(self):
        return self.name

class Cost_Center_Inventory(models.Model):
    code_cost_center = models.ForeignKey(Cost_Center, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)
    code_provider = models.ForeignKey(Product, to_field='code_provider', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    
    class Meta:
        verbose_name = "Cost_Center_Inventory"
        verbose_name_plural = "Cost_Center_Inventorys"
        unique_together = (('code_cost_center', 'code_product', 'code_provider'),)

    def __str__(self):
        return "code cost center: " + self.code_cost_center + " " +  "code product: " + self.code_product + " " + "code provider: " + self.code_provider

# Client End ------------------------------------------------------------------------------------------------------------------------------------------------
    