import pandas as pd


def create_product_df(products: list[dict]) -> pd.DataFrame:
    df = pd.json_normalize(products)
    return df[["barcode", "name", "brand", "image"]]
