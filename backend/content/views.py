from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


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
