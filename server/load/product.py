import pandas as pd
from django.db import transaction

from config import colors
from products.models import Product


def load_product_data(df: pd.DataFrame):
    """
    Load product data into the database using Django ORM

    Assumes django setup has been done.
    """
    print(f"{colors.MAGENTA}Loading product data into the database{colors.RESET}")
    all_barcordes = df["barcode"].unique().tolist()
    df.drop_duplicates("barcode", inplace=True)
    product_list = df.to_dict(orient="records")

    # Identify records by barcode
    existing_barcodes = Product.objects.filter(barcode__in=all_barcordes).values_list(
        "barcode", flat=True
    )

    # Segregate new and existing data
    insert_records = []
    update_records = []

    for record in product_list:
        if record["barcode"] in existing_barcodes:
            update_records.append(Product(**record))
        else:
            insert_records.append(Product(**record))

    print(f"Inserting {colors.BLUE}{len(insert_records)} new{colors.RESET} records")
    print(f"Updating {colors.YELLOW}{len(update_records)} existing{colors.RESET} records")

    with transaction.atomic():
        if insert_records:
            Product.objects.bulk_create(insert_records)
        if update_records:
            Product.objects.bulk_update(
                update_records, fields=["name", "brand", "image"]
            )
