from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display = (
        'code',
        'account',
        'account_sub',
        'description',
        'unit',
        'price'
    )
    list_filter = (
        'account',
        'account_sub',
        'description',
        'unit',
        'price'
    )
    search_fields = (
        'code',
        'account',
        'account_sub',
        'description',
        'unit',
        'price'
    )
    list_per_page = 10


# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------
    
@admin.register(Provider)
class ProviderModel(admin.ModelAdmin):
    list_display = (
        'code',
        'name'
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'code',
        'name'
    )
    list_per_page = 10

    
@admin.register(ProviderInventory)
class ProviderInventoryModel(admin.ModelAdmin):
    list_display = (
        'pk',
        'provider',
        'product',
        'quantity'
    )
    list_filter = (
        'provider',
        'product',
        'quantity'
    )
    search_fields = (
        'pk',
        'provider',
        'product',
        'quantity'
    )
    list_per_page = 10

# Enterprise End --------------------------------------------------------------------------------------------------------------------------------------------


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------    

@admin.register(Warehouse)
class WarehouseModel(admin.ModelAdmin):
    list_display = (
        'code',
        'name'
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'code',
        'name'
    )
    list_per_page = 10


@admin.register(WarehouseInventory)
class WarehouseInventoryModel(admin.ModelAdmin):
    list_display = (
        'pk',
        'warehouse',
        'product',
        'quantity'
    )
    list_filter = (
        'warehouse',
        'product',
        'quantity'
    )    
    readonly_fields = (
        'quantity',
    )
    search_fields = (
        'pk',
        'warehouse',
        'product',
        'quantity'
    )
    list_per_page = 10

# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

@admin.register(Unit)
class UnitModel(admin.ModelAdmin):
    list_display = (
        'code',
        'name'
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'code',
        'name'
    )
    list_per_page = 10


@admin.register(CostCenter)
class CostCenterModel(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'unit'
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'code',
        'name',
        'unit'
    )
    list_per_page = 10

    
@admin.register(CostCenterInventory)
class CostCenterInventoryModel(admin.ModelAdmin):
    readonly_fields = (
        'quantity',
    )
    list_display = (
        'pk',
        'cost_center',
        'product',
        'quantity',
    )
    list_filter = (
        'cost_center',
        'product',
        'quantity',
    )
    search_fields = (
        'pk',
        'cost_center',
        'product',
        'quantity'
    )
    list_per_page = 10
    
# Client End ------------------------------------------------------------------------------------------------------------------------------------------------


# Operations ------------------------------------------------------------------------------------------------------------------------------------------------

@admin.register(DeliverySC208)
class DeliveryModel(admin.ModelAdmin):
    readonly_fields = (
        'voucher',
        'date_stamp',
    )
    list_display = (
        'voucher',
        'request_voucher_1',
        'request_voucher_2',
        'request_plan',
        'date_stamp',
        'warehouse_dispatcher',
        'cost_center_receiver',        
        'warehouse_inventory',
        'cost_center_inventory',
    )
    list_filter = (
        'request_voucher_1',
        'request_voucher_2',
        'request_plan',
        'date_stamp',
        'warehouse_dispatcher',
        'cost_center_receiver',
        'warehouse_inventory',
        'cost_center_inventory',
    )
    search_fields = (
        'voucher',
        'request_voucher_1',
        'request_voucher_2',
        'request_plan',
        'date_stamp',
        'warehouse_dispatcher',
        'cost_center_receiver',
        'warehouse_inventory',
        'cost_center_inventory',
    )
    list_per_page = 10
@admin.register(DeliveryListSC208)
class DeliveryListModel(admin.ModelAdmin):
    readonly_fields = (
        'existence',
    )
    list_display = (
        'delivery',
        'product',
        'quantity',
        'existence'
    )
    list_filter = (
        'product',
        'quantity',
        'existence'
    )
    search_fields = (
        'delivery',
        'product',
        'quantity',
        'existence'
    )
    list_per_page = 10
   
# Operations End --------------------------------------------------------------------------------------------------------------------------------------------