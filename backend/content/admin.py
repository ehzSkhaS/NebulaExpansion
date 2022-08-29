from django.contrib import admin
from .models import *


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
    list_per_page = 10   


# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------
    
@admin.register(Provider)
class ProviderModel(admin.ModelAdmin):
    list_display = (
        'code',
        'name'
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
    list_per_page = 10

# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

@admin.register(Unit)
class UnitModel(admin.ModelAdmin):
    list_display = (
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
    list_per_page = 10
    
# Client End ------------------------------------------------------------------------------------------------------------------------------------------------

