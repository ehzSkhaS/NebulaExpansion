from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        products_serializer = ProductSerializer(data=data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse(products_serializer.data, status=201)
        return JsonResponse(products_serializer.errors, status=400)
