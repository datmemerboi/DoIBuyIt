import json
import django
import requests
from sys import argv
from os import path, environ


environ.setdefault("DJANGO_SETTINGS_MODULE", "doibuyit.settings")
django.setup()

from config.constants import RESULTS_FOLDER
from load.product import load_product_data
from load.price import load_price_data, load_vendor_product_data
from utils.date import make_prefix
from transform.product import create_product_df
from transform.price import create_price_df
from transform.dataframe import save_csv
from transform.woolworths import pick_products
from spiders.woolworths import Woolworths


session = requests.Session()
session.get(
    "https://www.woolworths.com.au",
    headers={
        "Accept": "application/json, */*",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.",
    },
)

product_list = []
for i in range(1, 5):
    print(".", end="")
    product_list.extend(
        pick_products(
            Woolworths.category(
                session=session, category_name="HalfPrice", page=i, size=30
            )
        )
    )
print()

price_df = create_price_df(product_list)
product_df = create_product_df(product_list)

price_csv_name = f"{make_prefix()}price-result.csv"
price_csv_path = path.abspath(path.join(RESULTS_FOLDER, price_csv_name))
save_csv(price_df, price_csv_path)

product_csv_name = f"{make_prefix()}product-result.csv"
product_csv_path = path.abspath(path.join(RESULTS_FOLDER, product_csv_name))
save_csv(product_df, product_csv_path)

load_product_data(product_df)
load_vendor_product_data(price_df)
load_price_data(price_df)
