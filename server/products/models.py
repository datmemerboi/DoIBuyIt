from django.db import models

VENDOR_SLUGS = (("WWL", "WWL"),)

class Product(models.Model):
    barcode = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    image = models.TextField()


class Vendor(models.Model):
    name = models.CharField(max_length=5, choices=VENDOR_SLUGS, primary_key=True)


class VendorProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="products"
    )
    url = models.TextField()

    class Meta:
        unique_together = (("product", "vendor"),)


class Price(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="prices"
    )
    vendor_product = models.ForeignKey(
        VendorProduct, on_delete=models.CASCADE, related_name="prices"
    )

    price = models.FloatField()
    viewed_date = models.DateTimeField()
    tentative_end_date = models.DateTimeField()
    cost_per_unit = models.FloatField(default=-1)
    cost_per_unit_measure = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
