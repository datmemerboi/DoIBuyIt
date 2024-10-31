import pandas as pd

from utils.date import get_previous_wednesday, get_upcoming_tuesday


def create_price_df(products: list[dict], vendor: str) -> pd.DataFrame:
    df = pd.json_normalize(products)

    price_df = df[
        ["barcode", "price", "previous_price", "cost_per_unit", "cost_per_unit_measure"]
    ].copy()
    price_df["vendor"] = vendor
    price_df["viewed_date"] = get_previous_wednesday()
    price_df["tentative_end_date"] = get_upcoming_tuesday()

    # Re-order columns
    price_df = price_df[
        [
            "barcode",
            "vendor",
            "price",
            "previous_price",
            "viewed_date",
            "tentative_end_date",
            "cost_per_unit",
            "cost_per_unit_measure",
        ]
    ]

    return price_df
