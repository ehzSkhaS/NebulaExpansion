from django.contrib import admin
from .models import *


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
        'get_warehouse_code',
        'get_warehouse_name',
        'cost_center_receiver',        
        'get_cost_center_code',
        'get_cost_center_name',
    )
    list_filter = []
    list_per_page = 10
    
    @admin.display(ordering='warehouse__code', description='warehouse code')
    def get_warehouse_code(self, obj):
        return obj.warehouse.code
    
    @admin.display(ordering='warehouse__name', description='warehouse name')
    def get_warehouse_name(self, obj):
        return obj.warehouse.name
    
    @admin.display(ordering='cost_center__code', description='cost center code')
    def get_cost_center_code(self, obj):
        return obj.cost_center.code
    
    @admin.display(ordering='cost_center__name', description='cost center name')
    def get_cost_center_name(self, obj):
        return obj.cost_center.name
    
    
@admin.register(DeliveryListSC208)
class DeliveryListModel(admin.ModelAdmin):
    readonly_fields = (
        'existence',
    )
    list_display = (
        'delivery',
        'get_product_code',
        'get_product_description',
        'get_product_unit',
        'get_product_price',
        'quantity',
        'existence'
    )
    list_filter = []
    list_per_page = 10
    
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
        'get_warehouse_code',
        'get_warehouse_name',
        'cost_center_dispatcher',        
        'get_cost_center_code',
        'get_cost_center_name',
    )
    list_filter = []
    list_per_page = 10
    
    @admin.display(ordering='warehouse__code', description='warehouse code')
    def get_warehouse_code(self, obj):
        return obj.warehouse.code
    
    @admin.display(ordering='warehouse__name', description='warehouse name')
    def get_warehouse_name(self, obj):
        return obj.warehouse.name
    
    @admin.display(ordering='cost_center__code', description='cost center code')
    def get_cost_center_code(self, obj):
        return obj.cost_center.code
    
    @admin.display(ordering='cost_center__name', description='cost center name')
    def get_cost_center_name(self, obj):
        return obj.cost_center.name
    
    
@admin.register(DevolutionListSC208)
class DevolutionListModel(admin.ModelAdmin):
    readonly_fields = (
        'existence',
    )
    list_display = (
        'devolution',
        'get_product_code',
        'get_product_description',
        'get_product_unit',
        'get_product_price',
        'quantity',
        'existence'
    )
    list_filter = []
    list_per_page = 10    
    
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
        'get_warehouse_code',
        'get_warehouse_name',
    )
    list_filter = []
    list_per_page = 10
    
    @admin.display(ordering='warehouse__code', description='warehouse code')
    def get_warehouse_code(self, obj):
        return obj.warehouse.code
    
    @admin.display(ordering='warehouse__name', description='warehouse name')
    def get_warehouse_name(self, obj):
        return obj.warehouse.name
    
    
@admin.register(AdjustListSC216)
class AdjustListModel(admin.ModelAdmin):
    readonly_fields = (
        'existence',
    )
    list_display = (
        'adjust',
        'get_product_code',
        'get_product_description',
        'get_product_unit',
        'get_product_price',
        'quantity',
        'existence'
    )
    list_filter = []
    list_per_page = 10
    
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
        'get_warehouse_code',
        'get_warehouse_name',
        'get_provider_code',
        'get_provider_name',
    )
    list_filter = []
    list_per_page = 10
    
    @admin.display(ordering='warehouse__code', description='warehouse code')
    def get_warehouse_code(self, obj):
        return obj.warehouse.code
    
    @admin.display(ordering='warehouse__name', description='warehouse name')
    def get_warehouse_name(self, obj):
        return obj.warehouse.name
    
    @admin.display(ordering='provider__code', description='provider code')
    def get_provider_code(self, obj):
        return obj.provider.code
    
    @admin.display(ordering='provider__name', description='provider name')
    def get_provider_name(self, obj):
        return obj.provider.name
    
    
@admin.register(ReceptionListSC204)
class ReceptionListModel(admin.ModelAdmin):
    readonly_fields = (
        'existence',
    )
    list_display = (
        'reception',
        'get_product_code',
        'get_product_description',
        'get_product_unit',
        'get_product_price',
        'quantity',
        'existence'
    )
    list_filter = []
    list_per_page = 10

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
