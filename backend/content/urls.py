from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('products', ProductViewSet, basename='products')
router.register('providers', ProviderViewSet, basename='providers')

router.register('listwarehouses', GetWarehouseViewSet, basename='listwarehouses')
router.register('warehouses', WarehouseViewSet, basename='warehouses')
# router.register('warehouses_inventories', WarehouseInventoryViewSet, basename='warehouses_inventories')

router.register('listunits', GetUnitViewSet, basename='listunits')
router.register('units', UnitViewSet, basename='units')

router.register('listcost_centers', GetCostCenterViewSet, basename='listcost_centers')
router.register('cost_centers', CostCenterViewSet, basename='cost_centers')
# router.register('cost_centers_inventories', CostCenterInventoryViewSet, basename='cost_centers_inventories')

urlpatterns = [ path('api/', include(router.urls)), ]

# urlpatterns = [
#     path('products/', product_list),
#     path('products/<int:pk>/', product_details),
#     path('providers/', provider_list),
#     path('providers/<int:pk>/', provider_details),
 
#     path('warehouses/', warehouse_list),
#     path('warehouses/<int:pk>/', warehouse_details),
#     #path('warehouses_inventory/', warehouse_inventory_list),
#     #path('warehouses_inventory/<int:pk>/', warehouse_inventory_details),
 
#     path('units/', unit_list),
#     path('units/<int:pk>/', unit_details),
 
#     path('cost_centers/', cost_center_list),
#     path('cost_centers/<int:pk>/', cost_center_details),
#     #path('cost_centers_inventory/', cost_center_inventory_list),
#     #path('cost_centers_inventory/<int:pk>/', cost_center_inventory_details),
 
 
#     # path('delivery_SC208/', delivery_SC208_list),
#     # path('delivery_SC208/<int:pk>/', delivery_SC208_details),
#     # path('delivery_list_SC208/', delivery_list_SC208_list),
#     # path('delivery_list_SC208/<int:pk>/', delivery_list_SC208_details),
#     # path('devolution_SC208/', devolution_SC208_list),
#     # path('devolution_SC208/<int:pk>/', devolution_SC208_details),
#     # path('devolution_list_SC208/', devolution_list_SC208_list),
#     # path('devolution_list_SC208/<int:pk>/', devolution_list_SC208_details),
#     # path('adjust_SC216/', adjust_SC216_list),
#     # path('adjust_SC216/<int:pk>/', adjust_SC216_details),
#     # path('adjust_list_SC216/', adjust_list_SC216_list),
#     # path('adjust_list_SC216/<int:pk>/', adjust_list_SC216_details),
#     # path('reception_SC204/', reception_SC204_list),
#     # path('reception_SC204/<int:pk>/', reception_SC204_details),
#     # path('reception_list_SC204/', reception_list_SC204_list),
#     # path('reception_list_SC204/<int:pk>/', reception_list_SC204_details),

# ]