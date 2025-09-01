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

HTTP_GET_HEADERS = {
    "Orgin": "https://www.coles.com.au",
    "Referer": "https://www.coles.com.au/",
    "Accept": "*/*",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    + "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 "
    + "Safari/537.",
}
