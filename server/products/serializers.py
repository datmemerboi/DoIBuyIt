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
    class Meta:
        model = Price
        fields = "__all__"

    def create(self, validated_data):
        price = Price.objects.create(**validated_data)
        return price

    def update(self, instance, validated_data):
        instance.price = validated_data.get("price", instance.price)
        instance.viewed_date = validated_data.get("viewed_date", instance.viewed_date)
        instance.tentative_end_date = validated_data.get(
            "tentative_end_date", instance.tentative_end_date
        )
        instance.cost_per_unit = validated_data.get(
            "cost_per_unit", instance.cost_per_unit
        )
        instance.cost_per_unit_measure = validated_data.get(
            "cost_per_unit_measure", instance.cost_per_unit_measure
        )
        instance.save()
        return instance
