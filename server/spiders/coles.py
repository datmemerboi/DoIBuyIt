import json
from typing import Any

from bs4 import BeautifulSoup
from requests import Session
import logging

from products.models import VendorSlugEnum
from server.products.exceptions import FailedBuildFetchError, FailedCategoryFetchError, UnableToInitSpiderError
from server.utils.category import get_category_id_url

# https://cdn.productimages.coles.com.au/productimages/2/2351254.jpg

#  https://www.coles.com.au/_next/data/20260224.3-acb5b6cbc710022f6d7fffaf69a9fd9b459e01bd/en/on-special.json?filter_Special=halfprice&pid=campaign_flyout_specials-catalogue_halfprice&page=2

logger = logging.getLogger(__name__)


def _generate_product_url(base_url: str, product_id: str | int, name: str, size: str | None = None) -> str:
    """
    Generates a product URL based on the given parameters.

    Args:
        base_url (str): The base URL of the product images.
        product_id (str | int): The unique identifier for the product.
        name (str): The name of the product, used for URL formatting.
        size (str | None): Optional size parameter to include in the URL.

    Returns:
        str: The generated product URL.
    """
    formatted_name = name.lower().replace(" ", "-")
    if size:
        formatted_name += f'-{size.lower().replace(" ", "-")}'
    url = f"{base_url}/product/{formatted_name}-{product_id}"
    return url


def _validate_incoming_category_data(data: dict[str, Any]) -> bool:
    """
    Validates the incoming category data from the Coles API.
    Requires consistent validation to ensure data structure similarity.

    Args:
        data (dict[str, Any]): The incoming category data to validate.
    Returns:
        bool: True if the data is valid, False otherwise.
    """
    if "pageProps" not in data:
        logger.error("Invalid category data: missing pageProps")
        return False
    if "results" not in data["pageProps"]:
        logger.error("Invalid category data: missing pageProps.results")
        return False
    if all(not record for record in data["pageProps"]["results"]):
        logger.error("Invalid category data: all results are empty")
        return False
    if any("_type" not in record for record in data["pageProps"]["results"]):
        logger.error("Invalid category data: missing _type in one or more records")
        return False
    products: list[dict[str, Any]] = [
        record
        for record in data["pageProps"]["results"]
        if isinstance(record.get("_type", ""), str) and record["_type"].lower() == "product"
    ]
    if not products:
        logger.error(f"Invalid category data: no product records found, {data['pageProps']['results']}")
        return False

    if any(
        "id" not in product
        or "name" not in product
        or "brand" not in product
        or "size" not in product
        or "pricing" not in product
        for product in products
    ):
        logger.error("Invalid category data: one or more product records missing required fields")
        return False

    if any(
        product["pricing"].get("now", None) is None
        or product["pricing"].get("was", None) is None
        or product["pricing"].get("comparable", None) is None
        for product in products
    ):
        logger.error("Invalid category data: one or more product records missing pricing information")
        return False

    # TODO: check for unit
    return True


class Coles:
    name: str = "Coles"
    vendor: str = VendorSlugEnum.COLES.value
    site_url: str = "https://www.coles.com.au"
    json_base_url: str = "https://www.coles.com.au/_next/data"
    # 20260224.3-acb5b6cbc710022f6d7fffaf69a9fd9b459e01bd/en/on-special.json?filter_Special=halfprice&page=2"
    ASSET_URL = "https://cdn.productimages.coles.com.au/productimages"

    _BUILD_ID: str | None = None

    _headers: dict = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",  # noqa: E501
        "Accept-Language": "en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",  # noqa: E501
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-platform": "macOS",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",  # noqa: E501
    }

    def __init__(self):
        """
        Initializes the Coles spider by fetching the current build ID from the website.

        Raises:
            UnableToInitSpiderError: If the build ID cannot be fetched.
        """
        if Coles._BUILD_ID is None:
            try:
                self._fetch_build_id()
            except FailedBuildFetchError as e:
                logger.error(e)
                raise UnableToInitSpiderError(vendor=self.vendor)

    def _fetch_build_id(self):
        """
        Fetches the current build ID from the Coles website and stores it in the class variable.

        Raises:
            FailedBuildFetchError: If the build ID cannot be fetched.
        """
        resp = None
        with Session() as session:
            resp = session.get(url=self.site_url, headers=Coles._headers, timeout=30)
        if not resp:
            raise FailedBuildFetchError(f"Failed to fetch build ID for vendor: {self.vendor}, no response received")
        if resp.status_code != 200:
            raise FailedBuildFetchError(
                f"Failed to fetch build ID for vendor: {self.vendor}, status code: {resp.status_code}"
            )
        if not resp.text:
            raise FailedBuildFetchError(
                f"Failed to fetch build ID for vendor: {self.vendor}, status code: {resp.status_code}"
            )

        soup = BeautifulSoup(resp.text, "html.parser")
        next_data_script = soup.find("script", id="__NEXT_DATA__")

        if not next_data_script:
            raise FailedBuildFetchError(f"Build ID missing for vendor: {self.vendor}, no __NEXT_DATA__ script found")

        data: dict[str, Any] = json.loads(next_data_script.string)
        build_id: str | None = data.get("buildId")
        if not build_id:
            raise FailedBuildFetchError(f"Build ID missing for vendor: {self.vendor}")

        Coles._BUILD_ID = build_id

    def category(
        self,
        session: Session,
        category: str,
        page: int = 1,
        size: int = 50,
    ) -> list:
        if not Coles._BUILD_ID:
            logger.error(f"Spider missing build ID for {self.vendor}, unable to fetch category data")
            return []

        category_id, _ = get_category_id_url(Coles.vendor, category)
        url: str = "/".join(
            [
                self.json_base_url,
                self._BUILD_ID,
                "en",
                f"on-special.json?filter_Special={category_id}&page={page}",
            ]
        )
        resp = session.get(url=url, headers=self._headers, timeout=30)
        if resp.status_code != 200:
            raise FailedCategoryFetchError(
                message=f"Failed to fetch category: {category}, vendor: {self.vendor}, resp: {resp.text}"
            )

        data = resp.text
        print(data)
        # if "products" not in data or not data["products"]:
        #     print(f"No products found for category: {category}")
        #     return []
        # return data["products"]
