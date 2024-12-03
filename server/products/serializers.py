from rest_framework import serializers
from .models import Product, Price, VendorProduct, VENDOR_SLUGS


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class VendorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProduct
        fields = "__all__"


# TODO: ProductPriceSerializer biding barcode with top 2 prices,
# preferably with unique vendors.

# TODO: Use the same searializer, with additional args to fetch
# entire price history of the product.


class PriceSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Price
        fields = "__all__"

    def create(self, validated_data):
        price = Price.objects.create(**validated_data)
        return price

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
