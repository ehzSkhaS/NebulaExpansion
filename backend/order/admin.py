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
    list_per_page = 10

