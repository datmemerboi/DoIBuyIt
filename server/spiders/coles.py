from requests import Session
from config.constants import HTTP_GET_HEADERS
from products.models import VendorSlugEnum


class Coles:
    name: str = "Coles"
    vendor: str = VendorSlugEnum.COLES.value
    category_url: str = "https://shop.coles.com.au/a/national/everything/search"

    headers: dict = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-platform": "macOS",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    }

    @staticmethod
    def category(
        session: Session,
        category: str,
        page: int = 1,
        size: int = 50,
    ) -> list:
        url = (
            f"https://www.coles.com.au/on-special?filter_Special=halfprice&page={page}"
        )
        print(url)
        print(Coles.headers)
        res = session.get(url=url, headers=Coles.headers, timeout=30)
        if res.status_code != 200:
            print(
                f"Failed to fetch category: {category},"
                + f"status code: {res.status_code}"
            )
            return []
        data = res.text
        print(data)
        # if "products" not in data or not data["products"]:
        #     print(f"No products found for category: {category}")
        #     return []
        # return data["products"]
