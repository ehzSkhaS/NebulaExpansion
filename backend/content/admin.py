from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    fields = (
        'description',
        ('code', 'account', 'account_sub'),
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
    list_per_page = 10
    list_filter = []


@admin.register(
    Provider,
    Unit,
)
class ProviderUnitModel(admin.ModelAdmin):
    list_display = (
        'code',
        'name'
    )
    list_per_page = 10
    list_filter = []


@admin.register(Warehouse)
class WarehouseModel(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )
    list_per_page = 10
    list_filter = []
    
   
@admin.register(CostCenter)
class CostCenterModel(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'get_unit_code',
        'get_unit_name',
        'inventory'
    )    
    list_per_page = 10
    list_filter = []
    
    @admin.display(ordering='unit__code', description='unit code')
    def get_unit_code(self, obj):
        return obj.unit.code
    
    @admin.display(ordering='unit__name', description='unit name')
    def get_unit_name(self, obj):
        return obj.unit.name
    
    
@admin.register(CostCenterInventory)
class CostCenterInventoryModel(admin.ModelAdmin):
    readonly_fields = (
        'quantity',
    )
    list_display = (
        'get_cost_center_code',
        'get_cost_center_name',
        'get_product_code',
        'get_product_description',
        'get_product_unit',
        'get_product_price',
        'quantity',
    )
    list_per_page = 10
    list_filter = []
    
    @admin.display(ordering='cost_center__code', description='cost center code')
    def get_cost_center_code(self, obj):
        return obj.cost_center.code
    
    @admin.display(ordering='cost_center__name', description='cost center name')
    def get_cost_center_name(self, obj):
        return obj.cost_center.name
    
    @admin.display(ordering='product__code', description='product code')
    def get_product_code(self, obj):
        return obj.product.code
    
    @admin.display(ordering='product__description', description='description')
    def get_product_description(self, obj):
        return obj.product.description

    @admin.display(ordering='product__unit', description='unit')
    def get_product_unit(self, obj):
        return obj.product.unit
    
    @admin.display(ordering='product__price', description='price')
    def get_product_price(self, obj):
        return obj.product.price


@admin.register(WarehouseInventory)
class WarehouseInventoryModel(admin.ModelAdmin):
    readonly_fields = ('quantity',)    
    list_display = (
        'get_warehouse_code',
        'get_warehouse_name',
        'get_product_code',
        'get_product_description',
        'get_product_unit',
        'get_product_price',
        'quantity',
    )
    list_per_page = 10
    list_filter = []
    
    @admin.display(ordering='warehouse__code', description='warehouse code')
    def get_warehouse_code(self, obj):
        return obj.warehouse.code
    
    @admin.display(ordering='warehouse__name', description='warehouse name')
    def get_warehouse_name(self, obj):
        return obj.warehouse.name
    
    @admin.display(ordering='product__code', description='product code')
    def get_product_code(self, obj):
        return obj.product.code
    
    @admin.display(ordering='product__description', description='description')
    def get_product_description(self, obj):
        return obj.product.description

    @admin.display(ordering='product__unit', description='unit')
    def get_product_unit(self, obj):
        return obj.product.unit
    
    @admin.display(ordering='product__price', description='price')
    def get_product_price(self, obj):
        return obj.product.price
