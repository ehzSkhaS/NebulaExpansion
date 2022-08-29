from .models import *
from rest_framework import serializers

from content.serializers import WarehouseSerializer, SimpleCostCenterSerializer

class DeliverySC208Serializer(serializers.ModelSerializer):
    class Meta:
        model = DeliverySC208
        fields = '__all__'
        
        
class DeliveryListSC208Serializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryListSC208
        fields = '__all__'
        

class GetDevolutionSC208Serializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(read_only=True)
    cost_center = SimpleCostCenterSerializer(read_only=True)
    class Meta:
        model = DevolutionSC208
        depth = 1
        fields = [
            'voucher',
            'date_stamp',
            'warehouse_receiver',
            'cost_center_dispatcher',
            'warehouse',
            'cost_center',
            'list'
        ]

        
class DevolutionSC208Serializer(serializers.ModelSerializer):
    class Meta:
        model = DevolutionSC208
        fields = '__all__'
        
        
class DevolutionListSC208Serializer(serializers.ModelSerializer):
    class Meta:
        model = DevolutionListSC208
        fields = '__all__'


class GetAdjustSC216Serializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(read_only=True)
    class Meta:
        model = AdjustSC216
        depth = 1
        fields = [
            'voucher',
            'date_stamp',
            'concept',
            'store_manager',
            'inventory_manager',
            'warehouse',
            'list'
        ]
        
        
class AdjustSC216Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdjustSC216
        fields = '__all__'
        
        
class AdjustListSC216Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdjustListSC216
        fields = '__all__'
        
        
class GetReceptionSC204Serializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(read_only=True)
    class Meta:
        model = ReceptionSC204
        depth = 1
        fields = [
            'voucher',
            'date_stamp',
            'bill_number',
            'warehouse_receiver',
            'store_manager',
            'driver',
            'warehouse',
            'provider',
            'list'
        ]
        
        
class ReceptionSC204Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReceptionSC204
        fields = '__all__'
        
        
class ReceptionListSC204Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReceptionListSC204
        fields = '__all__'
