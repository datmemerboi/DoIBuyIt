import json
from os import path
from typing import Tuple

from config.constants import WWL_CATEGORY_MAP_FILE


def get_category_id_url(vendor: str, category_name: str) -> Tuple[str, str]:
    if vendor == "WWL":
        map_file = open(WWL_CATEGORY_MAP_FILE)
    else:
        return None, None
    category_map = json.load(map_file)
    map_file.close()
    # Key check
    if category_name in category_map:
        return category_map[category_name]["id"], category_map[category_name]["url"]

    # Name check
    for ctg in category_map.values():
        if ctg["name"] == category_name:
            return ctg["id"], ctg["url"]
    return None, None
