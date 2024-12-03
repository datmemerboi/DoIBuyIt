import pandas as pd
from django.db import transaction
from django.utils import dateparse

from products.models import Product, VendorProduct, Vendor, Price


def load_vendor_product_data(df: pd.DataFrame):
    """
    Load vendor product data into the database using Django ORM

    Assumes:
    - Django setup has been done
    - Product data has been loaded
    """
    print("Loading vendor-product data into the database")
    df.drop_duplicates(["barcode", "vendor"], inplace=True)
    existing_vendors = Vendor.objects.values_list("name", flat=True)
    vendors_to_insert = [
        Vendor(name=v)
        for v in df[~df["vendor"].isin(existing_vendors)]["vendor"].unique().tolist()
    ]
    Vendor.objects.bulk_create(vendors_to_insert)
    all_barcordes = df["barcode"].unique().tolist()

    product_vendors_map = {}
    for vp in VendorProduct.objects.filter(product__in=all_barcordes).values(
        "product", "vendor", "url"
    ):
        product_vendors_map.setdefault(vp.get("product"), []).append(vp.get("vendor"))

    insert_records = []
    update_records = []

    vp_list = df.to_dict(orient="records")

    for record in vp_list:
        if (
            record["barcode"] in product_vendors_map
            and record["vendor"] in product_vendors_map[record["barcode"]]
        ):
            vp = VendorProduct.objects.get(
                product=Product.objects.get(pk=record["barcode"]),
                vendor=Vendor.objects.get(pk=record["vendor"]),
            )
            vp.url = record["url"]
            update_records.append(vp)
        else:
            insert_records.append(
                VendorProduct(
                    product=Product.objects.get(pk=record.get("barcode")),
                    vendor=Vendor.objects.get(pk=record.get("vendor")),
                    url=record.get("url"),
                )
            )

    print(f"Inserting {len(insert_records)} new vendor-products")
    print(f"Updating {len(update_records)} existing vendor-products")

    with transaction.atomic():
        if insert_records:
            VendorProduct.objects.bulk_create(insert_records)
        if update_records:
            # TODO: All bulk_update() objects must have a primary key set.
            VendorProduct.objects.bulk_update(update_records, fields=["url"])


def load_price_data(df: pd.DataFrame):
    """
    Load price data into the database using Django ORM

    Assumes:
    - Django setup has been done
    - Product data has been loaded
    - VendorProduct data has been loaded
    """
    print("Loading price data into the database")
    df.drop_duplicates(
        ["barcode", "vendor", "viewed_date"], inplace=True
    )  # Unique product viewed on a day
    all_barcordes = df["barcode"].unique().tolist()
    all_vendors = df["vendor"].unique().tolist()

    existing_records = Price.objects.filter(
        product__in=all_barcordes, vendor_product__vendor__in=all_vendors
    ).values("product", "vendor_product", "viewed_date")

    existing_records_map = {}
    for er in existing_records:
        existing_records_map.setdefault(er.get("product"), []).append(
            {"vendor": er.get("vendor_product"), "viewed_date": er.get("viewed_date")}
        )

    insert_records = []
    update_records = []

    price_list = df.to_dict(orient="records")

    for record in price_list:
        if record.get("barcode") in existing_records_map:
            # Find first existing record with the same barcode, vendor and viewed_date

            is_existing_record = next(
                (
                    vendor_view_date
                    for vendor_view_date in existing_records_map[record.get("barcode")]
                    if record.get("vendor") == vendor_view_date.get("vendor")
                    and record.get("viewed_date") == vendor_view_date.get("viewed_date")
                ),
                None,
            )

            if is_existing_record:
                update_records.append(Price(**record))
        else:
            prod = Product.objects.get(pk=record.get("barcode"))
            vend = Vendor.objects.get(pk=record.get("vendor"))
            vp = VendorProduct.objects.get(product=prod, vendor=vend)

            insert_records.append(
                Price(
                    price=record.get("price"),
                    viewed_date=dateparse.parse_datetime(record.get("viewed_date")),
                    tentative_end_date=dateparse.parse_datetime(
                        record.get("tentative_end_date")
                    ),
                    cost_per_unit=record.get("cost_per_unit"),
                    cost_per_unit_measure=record.get("cost_per_unit_measure"),
                    product=prod,
                    vendor_product=vp,
                )
            )

    print(f"Inserting {len(insert_records)} new prices")
    print(f"Updating {len(update_records)} existing prices")

    with transaction.atomic():
        if insert_records:
            Price.objects.bulk_create(insert_records)
        if update_records:
            Price.objects.bulk_update(
                update_records,
                fields=["price", "cost_per_unit", "cost_per_unit_measure"],
            )
