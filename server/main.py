import json
from os import path
from sys import argv

from transform.dataframe import product_list_to_df, save_csv
from utils.woolworths import pick_products
from spiders.woolworths import Woolworths

product_list = pick_products(Woolworths.category(argv[1]))
result_csv_path = path.abspath(path.join(__file__, "..", "..", "data", "result.csv"))
parsed_json_path = path.abspath(path.join(__file__, "..", "..", "data", "parsed_sample.json"))

json.dump(product_list, open(parsed_json_path, 'w'), indent=2)
save_csv(product_list_to_df(product_list), result_csv_path)
