from .models import *
from .serializers import *
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

#TODO: the next import is necessary for testing the post and update methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)        
        return JsonResponse(serializer.data, safe=False)    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)                
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def product_details(request, pk):
    try:
        product = Product.objects.get(code=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        # I need to use v2 because the code field is required on update
        # for now I don't know how to change the validator for 
        # set code as allow_null
        serializer = ProductSerializerV2(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)


@csrf_exempt
def provider_list(request):
    if request.method == 'GET':
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProviderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)