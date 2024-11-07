import json
from os import path
from sys import argv

from requests_cache import CachedSession

from config.constants import RESULTS_FOLDER
from utils.date import make_prefix
from transform.product import create_product_df
from transform.price import create_price_df
from transform.dataframe import product_list_to_df, save_csv
from utils.woolworths import pick_products
from spiders.woolworths import Woolworths

session = CachedSession()
session.get("https://www.woolworths.com.au", refresh=True)

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

price_df = create_price_df(product_list, Woolworths.vendor)
product_df = create_product_df(product_list)

price_csv_name = f"{make_prefix()}price-result.csv"
price_csv_path = path.abspath(path.join(RESULTS_FOLDER, price_csv_name))
save_csv(price_df, price_csv_path)

product_csv_name = f"{make_prefix()}product-result.csv"
product_csv_path = path.abspath(path.join(RESULTS_FOLDER, product_csv_name))
save_csv(product_df, product_csv_path)
