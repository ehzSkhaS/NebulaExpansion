from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('deliveries_SC_2_08', DeliverySC208ViewSet, basename='deliveries_SC_2_08')
router.register('deliveries_lists_SC_2_08', DeliveryListSC208ViewSet, basename='deliveries_lists_SC_2_08')

router.register('listdevolutions_SC_2_08', GetDevolutionSC208ViewSet, basename='listdevolutions_SC_2_08')
router.register('devolutions_SC_2_08', DevolutionSC208ViewSet, basename='devolutions_SC_2_08')
router.register('devolutions_lists_SC_2_08', DevolutionListSC208ViewSet, basename='devolutions_lists_SC_2_08')

router.register('listadjusts_SC_2_16', GetAdjustSC216ViewSet, basename='listadjusts_SC_2_16')
router.register('adjusts_SC_2_16', AdjustSC216ViewSet, basename='adjusts_SC_2_16')
router.register('adjusts_lists_SC_2_16', AdjustListSC216ViewSet, basename='adjusts_lists_SC_2_16')

router.register('listreceptions_SC_2_04', GetReceptionSC204ViewSet, basename='listreceptions_SC_2_04')
router.register('receptions_SC_2_04', ReceptionSC204ViewSet, basename='receptions_SC_2_04')
router.register('receptions_lists_SC_2_04', ReceptionListSC204ViewSet, basename='receptions_lists_SC_2_04')

urlpatterns = [ path('api/', include(router.urls)), ]