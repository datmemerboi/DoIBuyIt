import json

# import numpy as np
import pandas as pd

from config.constants import CSV_FILE_DATE_FORMAT


def product_list_to_df(products: list[dict]) -> pd.DataFrame:
    return pd.json_normalize(products)


def df_to_product_list(df: pd.DataFrame) -> list[dict]:
    return json.loads(df.to_json(orient="records"))


def save_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False, date_format=CSV_FILE_DATE_FORMAT)
