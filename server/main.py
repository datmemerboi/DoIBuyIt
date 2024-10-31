import json
from os import path
from sys import argv

from requests_cache import CachedSession

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
                session=session, category_name="half-price", page=i, size=30
            )
        )
    )
print()

price_df = create_price_df(product_list, Woolworths.vendor)
product_df = create_product_df(product_list)

price_csv_path = path.abspath(path.join(__file__, "..", "..", "data", "price_result.csv"))
save_csv(price_df, price_csv_path)
product_csv_path = path.abspath(path.join(__file__, "..", "..", "data", "product_result.csv"))
save_csv(product_df, product_csv_path)

# result_csv_path = path.abspath(path.join(__file__, "..", "..", "data", "result.csv"))
# parsed_json_path = path.abspath(
#     path.join(__file__, "..", "..", "data", "parsed_sample.json")
# )

# json.dump(product_list, open(parsed_json_path, "w"), indent=2)
# save_csv(product_list_to_df(product_list), result_csv_path)
