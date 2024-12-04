from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from utils.date import get_upcoming_tuesday, to_format_str
from products.models import Product, Price, Vendor, VendorProduct
from products.paginations import PricePagination, ProductPagination
from products.serializers import (
    ProductSerializer,
    PriceSerializer,
    VendorProductSerializer,
    VendorSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination


class PriceViewSet(viewsets.ModelViewSet):
    # Fetch products on discount this week,
    # sorted by price in ascending order.
    queryset = (
        Price.objects.exclude(price=-1)
        .filter(tentative_end_date=to_format_str(get_upcoming_tuesday(datetime.now())))
        .order_by("price")
    )
    serializer_class = PriceSerializer
    pagination_class = PricePagination
    # TODO: Query param to order price / filter above certain price.


class VendorsViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


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
