from django.contrib import admin
from .models import *


admin.site.site_header = "ICRT Radio Warehouse Administration"
admin.site.site_title = "ICRT"
admin.site.index_title = "Administration"


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    fields = (
        ('code', 'account', 'account_sub'),
        'description',
        ('unit', 'price')
    )
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
    )
    ordering = (
        'code',
    )
    list_per_page = 10   


# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------
    
@admin.register(Provider)
class ProviderModel(admin.ModelAdmin):
    list_display = (
        'code',
        'name'
    )    
    ordering = (
        'code',
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
    ordering = (
        'code',
    )
    list_per_page = 10


@admin.register(WarehouseInventory)
class WarehouseInventoryModel(admin.ModelAdmin):
    list_display = (
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
    ordering = (
        'warehouse',
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
    ordering = (
        'code',
    )
    list_per_page = 10


@admin.register(CostCenter)
class CostCenterModel(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'unit'
    )    
    ordering = (
        'code',
    )
    list_per_page = 10

    
@admin.register(CostCenterInventory)
class CostCenterInventoryModel(admin.ModelAdmin):
    readonly_fields = (
        'quantity',
    )
    list_display = (
        'cost_center',
        'product',
        'quantity',
    )
    list_filter = (
        'cost_center',
        'product',
        'quantity',
    )    
    ordering = (
        'cost_center',
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
        'warehouse',
        'cost_center',
    )
    list_filter = (
        'request_voucher_1',
        'request_voucher_2',
        'request_plan',
        'date_stamp',
        'warehouse_dispatcher',
        'cost_center_receiver',
        'warehouse',
        'cost_center',
    )    
    ordering = (
        'voucher',
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
    ordering = (
        'delivery',
    )
    list_per_page = 10    
    
    
@admin.register(DevolutionSC208)
class DvolutionModel(admin.ModelAdmin):
    readonly_fields = (
        'voucher',
        'date_stamp',
    )
    list_display = (
        'voucher',
        'date_stamp',
        'warehouse_receiver',
        'cost_center_dispatcher',        
        'warehouse',
        'cost_center',
    )
    list_filter = (
        'date_stamp',
        'warehouse_receiver',
        'cost_center_dispatcher',        
        'warehouse',
        'cost_center',
    )    
    ordering = (
        'voucher',
    )
    list_per_page = 10
    
    
@admin.register(DevolutionListSC208)
class DevolutionListModel(admin.ModelAdmin):
    readonly_fields = (
        'existence',
    )
    list_display = (
        'devolution',
        'product',
        'quantity',
        'existence'
    )
    list_filter = (
        'product',
        'quantity',
        'existence'
    )    
    ordering = (
        'devolution',
    )
    list_per_page = 10    
    
    
@admin.register(AdjustSC216)
class AdjustModel(admin.ModelAdmin):
    readonly_fields = (
        'voucher',
        'date_stamp',
    )
    list_display = (
        'voucher',
        'date_stamp',
        'concept',
        'store_manager',
        'inventory_manager',
        'warehouse',
    )
    list_filter = (
        'date_stamp',
        'concept',
        'store_manager',
        'inventory_manager',
        'warehouse',
    )
    ordering = (
        'voucher',
    )
    list_per_page = 10
    
    
@admin.register(AdjustListSC216)
class AdjustListModel(admin.ModelAdmin):
    readonly_fields = (
        'existence',
    )
    list_display = (
        'adjust',
        'product',
        'quantity',
        'existence'
    )
    list_filter = (
        'product',
        'quantity',
        'existence'
    )    
    ordering = (
        'adjust',
    )
    list_per_page = 10
    

@admin.register(ReceptionSC204)
class ReceptionModel(admin.ModelAdmin):
    readonly_fields = (
        'voucher',
        'date_stamp',
    )
    list_display = (
        'voucher',
        'date_stamp',
        'bill_number',
        'warehouse_receiver',
        'store_manager',        
        'warehouse',
        'provider',
    )
    list_filter = (
        'date_stamp',
        'bill_number',
        'warehouse_receiver',
        'store_manager',        
        'warehouse',
        'provider',
    )
    ordering = (
        'voucher',
    )
    list_per_page = 10
    
    
@admin.register(ReceptionListSC204)
class ReceptionListModel(admin.ModelAdmin):
    readonly_fields = (
        'existence',
    )
    list_display = (
        'reception',
        'product',
        'quantity',
        'existence'
    )
    list_filter = (
        'product',
        'quantity',
        'existence'
    )
    ordering = (
        'reception',
    )
    list_per_page = 10
    
    

   
# Operations End --------------------------------------------------------------------------------------------------------------------------------------------