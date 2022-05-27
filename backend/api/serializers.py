from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'code',
            'account',
            'account_sub',
            'description',
            'unit',
            'price'
        ]

#   I can do better that duplicate each modelserializer
#   avoiding the put method error on required private key
class ProductSerializerV2(serializers.ModelSerializer):
    # code = serializers.
    class Meta:
        model = Product
        fields = [
            'account',
            'account_sub',
            'description',
            'unit',
            'price'
        ]
        
# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = [
            'code',
            'name'
        ]
        
# Enterprise End --------------------------------------------------------------------------------------------------------------------------------------------


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'code',
            'name'
        ]
        

# Inventory can't have a create or update method        
""" class WarehouseInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseInventory
        fields = [
            'warehouse',
            'product'
        ] """
        
# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = [
            'code',
            'name'
        ]
        
        
class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = [
            'code',
            'name',
            'unit'
        ]
        

# Inventory can't have a create or update method
"""class CostCenterInventorySerializer(serializers.Serializer):    
    cost_center = serializers.PrimaryKeyRelatedField(queryset=CostCenter.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.DecimalField()"""