from .models import *
from .serializers import *
from rest_framework import viewsets

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
