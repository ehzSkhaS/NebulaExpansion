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
    price = models.FloatField(null=False)

    class Meta:
        db_table = 'api_product'
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
        db_table = 'api_provider'
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
        db_table = 'api_warehouse'
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
        db_table = 'api_warehouse_inventory'
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
        db_table = 'api_unit'
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
        db_table = 'api_cost_center'
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
        db_table = 'api_cost_center_inventory'
        verbose_name = "Cost Center Inventory"
        verbose_name_plural = "Cost Centers Inventories"
        unique_together = (('cost_center', 'product'),)
        ordering = ['cost_center']

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
    warehouse_dispatcher = models.DecimalField(max_digits=11, decimal_places=0)
    cost_center_receiver = models.DecimalField(max_digits=11, decimal_places=0)    
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)   
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_delivery_sc_2_08'
        verbose_name = "Delivery SC-2-08"
        verbose_name_plural = "Orders Delivery SC-2-08"
        ordering = ['voucher']

    def __str__(self):
        return str(self.voucher)
    
    
class DeliveryListSC208(Order):
    delivery = models.ForeignKey(DeliverySC208, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'api_delivery_list_sc_2_08'
        verbose_name = "Delivery List SC-2-08"
        verbose_name_plural = "Orders Delivery SC-2-08 Lists"
        unique_together = (('delivery', 'product'),)
        ordering = ['delivery']
        
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
            filter_l = DeliveryListSC208.objects.filter(
                product=self.product,
                delivery=self.delivery
            )
            filter_w = WarehouseInventory.objects.filter(
                product=self.product,
                warehouse=warehouse
            )
            filter_c = CostCenterInventory.objects.filter(
                product=self.product,
                cost_center=cost_center
            )
        
            if not filter_l.exists():
                if filter_w.exists():
                    quantity_w = filter_w.get().quantity
                    
                    if quantity_w >= self.quantity :
                        self.existence = quantity_w
                        filter_w.select_for_update().update(
                            quantity = quantity_w - self.quantity
                        )
                
                        if filter_c.exists():
                            quantity_c = filter_c.get().quantity
                            filter_c.select_for_update().update(
                                quantity = quantity_c + self.quantity
                            )
                        else:
                            CostCenterInventory.objects.create(
                                product=self.product,
                                cost_center=cost_center,
                                quantity=self.quantity
                            )
                    else:
                        raise ValidationError({'quantity': 'devolution quantity must be less or equal to stored quantity'})
                else:
                    raise ValidationError({'product': 'devolution product must be avaliable on the warehouse inventory'})
        
        validate_quantity()
     
    
class DevolutionSC208(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    warehouse_receiver = models.DecimalField(max_digits=11, decimal_places=0)
    cost_center_dispatcher = models.DecimalField(max_digits=11, decimal_places=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_devolution_sc_2_08'
        verbose_name = "Devolution SC-2-08"
        verbose_name_plural = "Orders Devolution SC-2-08"
        ordering = ['voucher']

    def __str__(self):
        return str(self.voucher)
    
    @property
    def list(self):
        devolutionlist = DevolutionListSC208.objects.filter(devolution=self)
        filtered = devolutionlist.values('product', 'quantity', 'existence')
        for e in filtered:            
            e['product'] = Product.objects.filter(code=e['product']).values()        
        return filtered


class DevolutionListSC208(Order):
    devolution = models.ForeignKey(DevolutionSC208, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_devolution_list_sc_2_08'
        verbose_name = "Devolution List SC-2-08"
        verbose_name_plural = "Orders Devolution SC-2-08 Lists"
        unique_together = (('devolution', 'product'),)
        ordering = ['devolution']
        
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
            filter_l = DevolutionListSC208.objects.filter(
                product=self.product,
                devolution=self.devolution
            )
            filter_w = WarehouseInventory.objects.filter(
                product=self.product,
                warehouse=warehouse
            )
            filter_c = CostCenterInventory.objects.filter(
                product = self.product,
                cost_center = cost_center
            )
            
            if not filter_l.exists():
                if filter_c.exists():
                    quantity_c = filter_c.get().quantity
                    
                    if quantity_c >= self.quantity:
                        self.existence = quantity_c
                        filter_c.select_for_update().update(
                            quantity = quantity_c - self.quantity
                        )
                        
                        if filter_w.exists():
                            quantity_w = filter_w.get().quantity
                            filter_w.select_for_update().update(
                                quantity = quantity_w + self.quantity
                            )
                        else:
                            WarehouseInventory.objects.create(
                                product=self.product,
                                warehouse=warehouse,
                                quantity=self.quantity
                            )
                    else:
                        raise ValidationError({'quantity': 'devolution quantity must be less or equal to stored quantity'})
                else:
                    raise ValidationError({'product': 'devolution product must be avaliable on the cost center inventory'})
        
        validate_quantity()
    
    
class AdjustSC216(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    concept = models.CharField(null=False, max_length=255)
    store_manager = models.DecimalField(max_digits=11, decimal_places=0)
    inventory_manager = models.DecimalField(max_digits=11, decimal_places=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'api_adjust_sc_2_16'
        verbose_name = "Adjust SC-2-16"
        verbose_name_plural = "Orders Adjust SC-2-16"
        ordering = ['voucher']

    def __str__(self):
        return str(self.voucher)
    
    @property
    def list(self):
        adjustlist = AdjustListSC216.objects.filter(adjust=self)
        filtered = adjustlist.values('product', 'quantity', 'existence')
        for e in filtered:            
            e['product'] = Product.objects.filter(code=e['product']).values()        
        return filtered
    

class AdjustListSC216(Order):
    adjust = models.ForeignKey(AdjustSC216, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_adjust_list_sc_2_16'
        verbose_name = "Adjust List SC-2-16"
        verbose_name_plural = "Orders Adjust SC-2-16 Lists"
        unique_together = (('adjust', 'product'),)
        ordering = ['adjust']
        
    def __str__(self):
        return str(self.pk)
    
    def clean(self):
        warehouse = AdjustSC216.objects.get(
            voucher = self.adjust.voucher
        ).warehouse
        
        def validate_quantity():
            filter_l = AdjustListSC216.objects.filter(
                product=self.product,
                adjust=self.adjust
            )
            filter_w = WarehouseInventory.objects.filter(
                product = self.product,
                warehouse = warehouse
            )
            
            if not filter_l.exists():
                if filter_w.exists():
                    quantity = filter_w.get().quantity
                    
                    if quantity >= self.quantity or self.quantity < 0:
                        self.existence = quantity
                        
                        filter_w.select_for_update().update(
                            quantity = self.existence - self.quantity
                        )
                    else :
                        raise ValidationError({'quantity': 'adjust quantity must be less or equal to stored quantity'})
                else:
                    raise ValidationError({'product': 'adjust product must be avaliable on the warehouse inventory'})
            
        validate_quantity()


class ReceptionSC204(models.Model):
    voucher = models.AutoField(primary_key=True, unique_for_year="date_stamp", editable=False)
    date_stamp = models.DateField(auto_now=True, editable=False)
    bill_number = models.CharField(null=False, max_length=255)
    warehouse_receiver = models.DecimalField(max_digits=11, decimal_places=0)
    store_manager = models.DecimalField(max_digits=11, decimal_places=0)
    driver = models.DecimalField(max_digits=11, decimal_places=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_reception_sc_2_04'
        verbose_name = "Reception SC-2-04"
        verbose_name_plural = "Orders Reception SC-2-04"
        ordering = ['voucher']

    def __str__(self):
        return str(self.voucher)
    
    @property
    def list(self):
        receptionlist = ReceptionListSC204.objects.filter(reception=self)
        filtered = receptionlist.values('product', 'quantity', 'existence')
        for e in filtered:            
            e['product'] = Product.objects.filter(code=e['product']).values()        
        return filtered
    

class ReceptionListSC204(Order):
    reception = models.ForeignKey(ReceptionSC204, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'api_reception_list_sc_2_04'
        verbose_name = "Reception List SC-2-04"
        verbose_name_plural = "Orders Reception SC-2-04 Lists"
        unique_together = (('reception', 'product'),)
        ordering = ['reception']
        
    def __str__(self):
        return str(self.pk)
    
    def clean(self):
        warehouse = ReceptionSC204.objects.get(
            voucher = self.reception.voucher
        ).warehouse
        
        def validate_quantity():
            filter_l = ReceptionListSC204.objects.filter(
                product=self.product,
                reception=self.reception
            )
            filter_w = WarehouseInventory.objects.filter(
                product=self.product,
                warehouse=warehouse
            )
            
            if not filter_l.exists():
                if filter_w.exists():
                    self.existence = filter_w.get().quantity
                    filter_w.select_for_update().update(
                        quantity = self.existence + self.quantity
                    )
                else :
                    WarehouseInventory.objects.create(
                        product=self.product,
                        warehouse=warehouse,
                        quantity=self.quantity
                    )
        
        validate_quantity()
        
# Operations End --------------------------------------------------------------------------------------------------------------------------------------------