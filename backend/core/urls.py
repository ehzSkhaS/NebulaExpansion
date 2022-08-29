"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from content.views import *
from order.views import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)


# router.register('users', UserViewSet)
router.register('products', ProductViewSet, basename='products')
router.register('cost_centers', CostCenterViewSet, basename='cost_centers')
router.register('units', UnitViewSet, basename='units')
router.register('warehouses', WarehouseViewSet, basename='warehouses')
router.register('providers', ProviderViewSet, basename='providers')

router.register('deliveries', DeliverySC208ViewSet, basename='deliveries')
router.register('deliveries_lists', DeliveryListSC208ViewSet, basename='deliveries_lists')
router.register('devolutions', DevolutionSC208ViewSet, basename='devolutions')
router.register('devolutions_lists', DevolutionListSC208ViewSet, basename='devolutions_lists')
router.register('adjusts', AdjustSC216ViewSet, basename='adjusts')
router.register('adjusts_lists', AdjustListSC216ViewSet, basename='adjusts_lists')
router.register('receptions', ReceptionSC204ViewSet, basename='receptions')
router.register('receptions_lists', ReceptionListSC204ViewSet, basename='receptions_lists')

router.register('cost_centers_readonly', GetCostCenterViewSet, basename='cost_centers_readonly')
# router.register('cost_centers_inventories', CostCenterInventoryViewSet, basename='cost_centers_inventories')
router.register('units_readonly', GetUnitViewSet, basename='units_readonly')
router.register('warehouses_readonly', GetWarehouseViewSet, basename='warehouses_readonly')
# router.register('warehouses_inventories', WarehouseInventoryViewSet, basename='warehouses_inventories')
router.register('devolutions_readonly', GetDevolutionSC208ViewSet, basename='devolutions_readonly')
router.register('adjusts_readonly', GetAdjustSC216ViewSet, basename='adjusts_readonly')
router.register('receptions_readonly', GetReceptionSC204ViewSet, basename='receptions_readonly')


urlpatterns = [
    # path('auth/', include(router.urls)), 
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
    # path('', include('content.urls')),
    # path('', include('order.urls')),
]
