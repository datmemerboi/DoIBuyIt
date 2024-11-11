from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from products.models import Product, Price, VendorProduct
from products.serializers import ProductSerializer, PriceSerializer, VendorProductSerializer
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class VendorProductViewSet(viewsets.ModelViewSet):
    queryset = VendorProduct.objects.all()
    serializer_class = VendorProductSerializer

@csrf_exempt
def product_list(request):
    """
    List all products.
    """
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def price_list(request):
    """
    List all prices
    """
    if request.method == "GET":
        prices = Price.objects.all()
        serializer = PriceSerializer(prices, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PriceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
