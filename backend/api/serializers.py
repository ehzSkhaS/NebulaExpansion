from dataclasses import fields
from .models import *
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'
        
# Enterprise End --------------------------------------------------------------------------------------------------------------------------------------------


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'
        

# Inventory can't have a create or update method        
class WarehouseInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseInventory
        fields = '__all__'
        
# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
        
        
class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = '__all__'
        

# Inventory can't have a create or update method
class CostCenterInventorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = CostCenterInventory
        fields = '__all__'
        
# Client End ------------------------------------------------------------------------------------------------------------------------------------------------

        
# Operations ------------------------------------------------------------------------------------------------------------------------------------------------

class DeliverySC208Serializer(serializers.ModelSerializer):
    class Meta:
        model = DeliverySC208
        fields = '__all__'
        
        
class DeliveryListSC208Serializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryListSC208
        fields = '__all__'
        
        
class DevolutionSC208Serializer(serializers.ModelSerializer):
    class Meta:
        model = DevolutionSC208
        fields = '__all__'
        
        
class DevolutionListSC208Serializer(serializers.ModelSerializer):
    class Meta:
        model = DevolutionListSC208
        fields = '__all__'


class AdjustSC216Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdjustSC216
        fields = '__all__'
        
        
class AdjustSC216Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdjustSC216
        fields = '__all__'
        
        
class AdjustListSC216Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdjustListSC216
        fields = '__all__'
        
        
class ReceptionSC204Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReceptionSC204
        fields = '__all__'
        
        
class ReceptionListSC204Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReceptionListSC204
        fields = '__all__'        
        
# Operations End --------------------------------------------------------------------------------------------------------------------------------------------        