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
    account = models.IntegerField(null=False)
    account_sub = models.IntegerField(null=False)
    description = models.CharField(null=False, max_length=50)
    unit = models.CharField(null=False, max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

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
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    code_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)
    
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
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    code_unit = models.ForeignKey(Unit, to_field='code', on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cost_center'
        verbose_name = "CostCenter"
        verbose_name_plural = "CostCenters"

    def __str__(self):
        return self.name

# Client End ------------------------------------------------------------------------------------------------------------------------------------------------


# Operations ------------------------------------------------------------------------------------------------------------------------------------------------

class DeliverySC208(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    request_voucher_1 = models.IntegerField(null=False)
    request_voucher_2 = models.IntegerField(null=False)
    request_plan = models.IntegerField(null=False)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    existence = models.DecimalField(max_digits=10, decimal_places=4)
    ci_cost_center_receiver = models.IntegerField(null=False)
    ci_warehouse_dispatcher = models.IntegerField(null=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    # I have doubts with the realtion of code_product should be with product
    # or with Warehouse, but I can't hace 2 fields refering the same table
    code_product = models.ForeignKey(Product, to_field='code', on_delete=models.CASCADE)
    number_warehouse = models.ForeignKey(Warehouse, to_field='number', on_delete=models.CASCADE)
    code_cost_center = models.ForeignKey(CostCenter, to_field='code', on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'delivery_sc_2_08'
        verbose_name = "DeliverySC208"
        verbose_name_plural = "DeliverySC208s"

    def __str__(self):
        return self.voucher

# Operations End --------------------------------------------------------------------------------------------------------------------------------------------