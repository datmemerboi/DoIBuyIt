import json
from typing import Tuple
import logging

from config.constants import WWL_CATEGORY_MAP_FILE, COL_CATEGORY_MAP_FILE

logger = logging.getLogger(__name__)


def _get_category_map_file(vendor: str):
    match (vendor):
        case "WWL":
            return WWL_CATEGORY_MAP_FILE
        case "COL":
            return COL_CATEGORY_MAP_FILE
        case _:
            logger.error(f"Vendor not supported: {vendor}")
            return None


def get_category_id_url(vendor: str, category_name: str) -> Tuple[str, str]:
    map_file_path = _get_category_map_file(vendor)
    if not map_file_path:
        return None, None

    map_file = open(map_file_path)
    category_map = json.load(map_file)
    map_file.close()

    # Key check (custom category key)
    if category_name in category_map:
        return (
            category_map[category_name]["id"],
            category_map[category_name]["url"],
        )

    # Name check (as seen on vendor site)
    for ctg in category_map.values():
        if ctg["name"] == category_name:
            return ctg["id"], ctg["url"]
    return None, None
