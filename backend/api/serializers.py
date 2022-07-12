from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.views import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


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
    
class GetWarehouseSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Warehouse
        fields = [
            'code',
            'name',
            'inventory',
            'products',
        ]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        for p in data['products']:
            for i in instance.inventory:
                if i['product'] == p['code']:                   
                    p.update([('quantity', i['quantity'])])
        data.pop('inventory')
        return data
    
    
class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'code',
            'name'
        ]
        

# Inventory can't have a create or update method 
class WarehouseInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseInventory
        fields = '__all__'
        depth = 1
        
# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

 
class GetUnitSerializer(serializers.ModelSerializer):
    # cost_centers = GetCostCenterSerializer(many=True, read_only=True)
    class Meta:
        model = Unit        
        fields = [
            'code',
            'name',
            'cost_centers',
        ]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        cc_dict = data.pop('cost_centers')
        # mod_cc_dict = {}
        # i = 0
        for p in cc_dict:
            # pass
            # inst = p['code']
            obj = CostCenter.objects.filter(code=p['code'])
            print(obj.values())
            cc = GetCostCenterSerializer(instance=obj, data=obj.values())#.to_representation()
            # cc = GetCostCenterSerializer(instance=p['code'], data=p)#.to_representation()
            # print(cc)
            
            # if cc.is_valid():
            #     print(cc.data)
            # else:
            #     print(cc.errors)
            # mod_cc_dict.update([(i, cc)])
            # i += 1
            # mod_cc_dict.update(cc
            # .update([('fifo', 500)])
            # print(mod_cc_dict)
            # k = GetCostCenterSerializer(instance=p['code'], data=p)
            # print(k)
            # print(k.to_representation)
            # if k.is_valid():
            #     print(k.data)
            # else:
            #     print(k.errors)
    #         p.update([('quantity', i['quantity'])])
    #     data.pop('inventory')
        # print(mod_cc_dict)
        # data.update([('cost_centers', mod_cc_dict)])
        return data



class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class GetCostCenterSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all(), many=False)
    class Meta:
        model = CostCenter
        depth =1
        fields = [
            'code',
            'name',
            'unit',
            'inventory',
            'products',
        ]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        for p in data['products']:
            for i in instance.inventory:
                if i['product'] == p['code']:                   
                    p.update([('quantity', i['quantity'])])
        data.pop('inventory')
        return data

class SimpleCostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        depth = 1
        fields = [
            'code',
            'name',
            'unit'
        ]
        
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
        
# Operations End --------------------------------------------------------------------------------------------------------------------------------------------        