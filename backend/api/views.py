from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.decorators import api_view

#TODO: the next import is necessary for testing the post and update methods
#from django.views.decorators.csrf import csrf_exempt


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

# Enterprise End --------------------------------------------------------------------------------------------------------------------------------------------


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------


class GetWarehouseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = GetWarehouseSerializer
        

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
        
     
class WarehouseInventoryViewSet(viewsets.ModelViewSet):
    queryset = WarehouseInventory.objects.all()
    serializer_class = WarehouseInventorySerializer
    
# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

class GetUnitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = GetUnitSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class GetCostCenterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CostCenter.objects.all()
    serializer_class = GetCostCenterSerializer


class CostCenterViewSet(viewsets.ModelViewSet):
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterSerializer


class CostCenterInventoryViewSet(viewsets.ModelViewSet):
    queryset = CostCenterInventory.objects.all()
    serializer_class = CostCenterInventorySerializer


# Client End ------------------------------------------------------------------------------------------------------------------------------------------------


# Operations ------------------------------------------------------------------------------------------------------------------------------------------------

class DeliverySC208ViewSet(viewsets.ModelViewSet):
    queryset = DeliverySC208.objects.all()
    serializer_class = DeliverySC208Serializer


class DeliveryListSC208ViewSet(viewsets.ModelViewSet):
    queryset = DeliveryListSC208.objects.all()
    serializer_class = DeliveryListSC208Serializer


class GetDevolutionSC208ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DevolutionSC208.objects.all()
    serializer_class = GetDevolutionSC208Serializer


class DevolutionSC208ViewSet(viewsets.ModelViewSet):
    queryset = DevolutionSC208.objects.all()
    serializer_class = DevolutionSC208Serializer


class DevolutionListSC208ViewSet(viewsets.ModelViewSet):
    queryset = DevolutionListSC208.objects.all()
    serializer_class = DevolutionListSC208Serializer


class GetAdjustSC216ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdjustSC216.objects.all()
    serializer_class = GetAdjustSC216Serializer


class AdjustSC216ViewSet(viewsets.ModelViewSet):
    queryset = AdjustSC216.objects.all()
    serializer_class = AdjustSC216Serializer


class AdjustListSC216ViewSet(viewsets.ModelViewSet):
    queryset = AdjustListSC216.objects.all()
    serializer_class = AdjustListSC216Serializer


class GetReceptionSC204ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReceptionSC204.objects.all()
    serializer_class = GetReceptionSC204Serializer


class ReceptionSC204ViewSet(viewsets.ModelViewSet):
    queryset = ReceptionSC204.objects.all()
    serializer_class = ReceptionSC204Serializer


class ReceptionListSC204ViewSet(viewsets.ModelViewSet):
    queryset = ReceptionListSC204.objects.all()
    serializer_class = ReceptionListSC204Serializer

# Operations End --------------------------------------------------------------------------------------------------------------------------------------------




















@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)        
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, pk):
    try:
        product = Product.objects.get(code=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)    
    elif request.method == 'PUT':
        product = Product.objects.get(code=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# Enterprise ------------------------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def provider_list(request):
    if request.method == 'GET':
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def provider_details(request, pk):
    try:
        provider = Provider.objects.get(code=pk)
    except Provider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)
    elif request.method == 'PUT':
        provider = Provider.objects.get(code=pk)
        serializer = ProviderSerializer(instance=provider, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Enterprise End --------------------------------------------------------------------------------------------------------------------------------------------


# Store -----------------------------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def warehouse_list(request):
    if request.method == 'GET':
        warehouses = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def warehouse_details(request, pk):
    try:
        warehouse = Warehouse.objects.get(code=pk)
    except Warehouse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = WarehouseSerializer(warehouse)
        return Response(serializer.data)
    elif request.method == 'PUT':
        warehouse = Warehouse.objects.get(code=pk)
        serializer = WarehouseSerializer(instance=warehouse, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def warehouse_inventory_list(request):
    if request.method == 'GET':
        warehouses_inventory = WarehouseInventory.objects.all()
        serializer = WarehouseInventorySerializer(warehouses_inventory, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def warehouse_inventory_details(request, pk):
    try:
        warehouse_inventory = WarehouseInventory.objects.get(pk=pk)
    except WarehouseInventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = WarehouseInventorySerializer(warehouse_inventory)
        return Response(serializer.data)
    
# Store End -------------------------------------------------------------------------------------------------------------------------------------------------


# Client ----------------------------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def unit_list(request):
    if request.method == 'GET':
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def unit_details(request, pk):
    try:
        unit = Unit.objects.get(code=pk)
    except Unit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UnitSerializer(unit)
        return Response(serializer.data)    
    elif request.method == 'PUT':
        unit = Unit.objects.get(code=pk)
        serializer = ProductSerializer(instance=unit, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        unit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def cost_center_list(request):
    if request.method == 'GET':
        cost_centers = CostCenter.objects.all()
        serializer = CostCenterSerializer(cost_centers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CostCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def cost_center_details(request, pk):
    try:
        cost_center = CostCenter.objects.get(code=pk)
    except CostCenter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CostCenterSerializer(cost_center)
        return Response(serializer.data)
    elif request.method == 'PUT':
        cost_center = CostCenter.objects.get(code=pk)
        serializer = CostCenterSerializer(instance=cost_center, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cost_center.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET'])
def cost_center_inventory_list(request):
    if request.method == 'GET':
        cost_centers_inventory = CostCenterInventory.objects.all()
        serializer = CostCenterInventorySerializer(cost_centers_inventory, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def cost_center_inventory_details(request, pk):
    try:
        cost_center_inventory = CostCenterInventory.objects.get(pk=pk)
    except CostCenterInventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CostCenterInventorySerializer(cost_center_inventory)
        return Response(serializer.data)

# Client End ------------------------------------------------------------------------------------------------------------------------------------------------


# Operations ------------------------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def delivery_SC208_list(request):
    if request.method == 'GET':
        deliveries_SC208 = DeliverySC208.objects.all()
        serializer = DeliverySC208Serializer(deliveries_SC208, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DeliverySC208Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def delivery_SC208_details(request, pk):
    try:
        delivery_SC208 = DeliverySC208.objects.get(voucher=pk)
    except DeliverySC208.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DeliverySC208Serializer(delivery_SC208)
        return Response(serializer.data)
    elif request.method == 'PUT':
        delivery_SC208 = DeliverySC208.objects.get(voucher=pk)
        serializer = DeliverySC208Serializer(instance=delivery_SC208, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        delivery_SC208.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def delivery_list_SC208_list(request):
    if request.method == 'GET':
        deliveries_list_SC208 = DeliveryListSC208.objects.all()
        serializer = DeliveryListSC208Serializer(deliveries_list_SC208, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DeliveryListSC208Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def delivery_list_SC208_details(request, pk):
    try:
        delivery_list_SC208 = DeliveryListSC208.objects.get(pk=pk)
    except DeliveryListSC208.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DeliveryListSC208Serializer(delivery_list_SC208)
        return Response(serializer.data)
    elif request.method == 'PUT':
        delivery_list_SC208 = DeliveryListSC208.objects.get(pk=pk)
        serializer = DeliveryListSC208Serializer(instance=delivery_list_SC208, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        delivery_list_SC208.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def devolution_SC208_list(request):
    if request.method == 'GET':
        devolutions_SC208 = DevolutionSC208.objects.all()
        serializer = DevolutionSC208Serializer(devolutions_SC208, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DevolutionSC208Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def devolution_SC208_details(request, pk):
    try:
        devolution_SC208 = DevolutionSC208.objects.get(voucher=pk)
    except DevolutionSC208.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DevolutionSC208Serializer(devolution_SC208)
        return Response(serializer.data)
    elif request.method == 'PUT':
        devolution_SC208 = DevolutionSC208.objects.get(voucher=pk)
        serializer = DevolutionSC208Serializer(instance=devolution_SC208, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        devolution_SC208.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def devolution_list_SC208_list(request):
    if request.method == 'GET':
        devolutions_list_SC208 = DevolutionListSC208.objects.all()
        serializer = DevolutionListSC208Serializer(devolutions_list_SC208, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DevolutionListSC208Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def devolution_list_SC208_details(request, pk):
    try:
        devolution_list_SC208 = DevolutionListSC208.objects.get(pk=pk)
    except DevolutionListSC208.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DevolutionListSC208Serializer(devolution_list_SC208)
        return Response(serializer.data)
    elif request.method == 'PUT':
        devolution_list_SC208 = DevolutionListSC208.objects.get(pk=pk)
        serializer = DevolutionListSC208Serializer(instance=devolution_list_SC208, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        devolution_list_SC208.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def adjust_SC216_list(request):
    if request.method == 'GET':
        adjusts_SC216 = AdjustSC216.objects.all()
        serializer = AdjustSC216(adjusts_SC216, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdjustListSC216(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def adjust_SC216_details(request, pk):
    try:
        adjust_SC216 = AdjustSC216.objects.get(voucher=pk)
    except AdjustSC216.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AdjustSC216Serializer(adjust_SC216)
        return Response(serializer.data)
    elif request.method == 'PUT':
        adjust_SC216 = AdjustSC216.objects.get(voucher=pk)
        serializer = AdjustSC216Serializer(instance=adjust_SC216, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        adjust_SC216.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def adjust_list_SC216_list(request):
    if request.method == 'GET':
        adjusts_list_SC216 = AdjustListSC216.objects.all()
        serializer = AdjustListSC216Serializer(adjusts_list_SC216, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdjustListSC216Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def adjust_list_SC216_details(request, pk):
    try:
        adjust_list_SC216 = AdjustListSC216.objects.get(pk=pk)
    except AdjustListSC216.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AdjustListSC216Serializer(adjust_list_SC216)
        return Response(serializer.data)
    elif request.method == 'PUT':
        adjust_list_SC216 = AdjustListSC216.objects.get(pk=pk)
        serializer = AdjustListSC216Serializer(instance=adjust_list_SC216, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        adjust_list_SC216.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reception_SC204_list(request):
    if request.method == 'GET':
        receptions_SC204 = ReceptionSC204.objects.all()
        serializer = ReceptionSC204Serializer(receptions_SC204, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReceptionSC204Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def reception_SC204_details(request, pk):
    try:
        reception_SC204 = ReceptionSC204.objects.get(voucher=pk)
    except ReceptionSC204.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReceptionSC204Serializer(reception_SC204)
        return Response(serializer.data)
    elif request.method == 'PUT':
        reception_SC204 = ReceptionSC204.objects.get(voucher=pk)
        serializer = ReceptionSC204Serializer(instance=reception_SC204, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        reception_SC204.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reception_list_SC204_list(request):
    if request.method == 'GET':
        receptions_list_SC204 = ReceptionListSC204.objects.all()
        serializer = ReceptionListSC204Serializer(receptions_list_SC204, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReceptionListSC204Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def reception_list_SC204_details(request, pk):
    try:
        reception_list_SC204 = ReceptionListSC204.objects.get(pk=pk)
    except ReceptionListSC204.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReceptionListSC204Serializer(reception_list_SC204)
        return Response(serializer.data)
    elif request.method == 'PUT':
        reception_list_SC204 = ReceptionListSC204.objects.get(pk=pk)
        serializer = ReceptionListSC204Serializer(instance=reception_list_SC204, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        reception_list_SC204.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Operations End --------------------------------------------------------------------------------------------------------------------------------------------

