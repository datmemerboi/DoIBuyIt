from os import path
from dateutil.tz import gettz

# File locations
WWL_CATEGORY_MAP_FILE = path.abspath(
    path.join(path.dirname(__file__), "..", "..", "category_map.json")
)
RESULTS_FOLDER = path.abspath(path.join(path.dirname(__file__), "..", "..", "data"))

# Date formats
CSV_NAME_PREFIX_FORMAT = "%Y-%m-%dT%H:%M_"
CSV_FILE_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
APP_TIMEZONE_NAME = "Australia/Melbourne"
APP_TIMEZONE = gettz(APP_TIMEZONE_NAME)
