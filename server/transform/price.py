from pandas import json_normalize, DataFrame


def create_price_df(products: list[dict]) -> DataFrame:
    df = json_normalize(products)

    # Re-order columns
    return df[
        [
            "barcode",
            "vendor",
            "price",
            "viewed_date",
            "tentative_end_date",
            "cost_per_unit",
            "cost_per_unit_measure",
            "previous_price",
            "url",
        ]
    ]
