from os import path
import pandas as pd
from config.constants import RESULTS_FOLDER
from transform.price import poly_fit
from utils.date import make_prefix


src_path = path.abspath(path.join(RESULTS_FOLDER, "2025-01-19T10:29_price-result.csv"))
target_path = path.abspath(
    path.join(RESULTS_FOLDER, "2025-01-20T17:22_price-result.csv")
)

src = pd.read_csv(src_path)
target = pd.read_csv(target_path)

print(poly_fit(src, target, "price"))
