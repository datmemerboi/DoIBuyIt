import numpy as np
import pandas as pd
from pandas import json_normalize, DataFrame

from utils.date import to_timestamp


def create_price_df(products: list[dict]) -> DataFrame:
    df = json_normalize(products)

    # Fill NaNs
    df.fillna(
        {"price": -1, "cost_per_unit": -1},  # Price is not available (None)
        inplace=True,
    )

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


def poly_fit(src_df: DataFrame, trg_df: DataFrame, column: str) -> np.ndarray:
    df = pd.concat([src_df, trg_df], join="inner")
    dates = df["viewed_date"]
    timestamps = dates.apply(to_timestamp)
    values = df[column]
    return np.polyfit(timestamps, values, 1)
