from urllib.parse import urlencode
from requests_cache import CachedSession


class Woolworths:
    name: str = "Woolworths"
    vendor: str = "W"
    category_url: str = "https://www.woolworths.com.au/apis/ui/browse/category"

    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    @staticmethod
    def category(session: CachedSession, category_name: str, page: int = 1, size: int = 36) -> list:
        url = Woolworths.category_url
        headers = {
            "Accept": "application/json, */*",
            "Content-Type": "application/json",
            "Referer": "https://www.woolworths.com.au/shop/browse/specials/half-price",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.",
        }
        body = {
            "categoryId": "specialsgroup.3676",
            "pageNumber": page,
            "pageSize": size,
            "sortType": "TraderRelevance",
            "url": "/shop/browse/specials/half-price",
            "location": "/shop/browse/specials/half-price",
            "formatObject": '{"name":"Half Price"}',
            "isSpecial": True,
            "isBundle": False,
            "isMobile": False,
            "filters": [],
            "token": "",
            "gpBoost": 0,
            "isHideUnavailableProducts": False,
            "isRegisteredRewardCardPromotion": False,
            "enableAdReRanking": False,
            "groupEdmVariants": True,
            "categoryVersion": "v2",
        }
        res = session.post(url=url, headers=headers, json=body, timeout=30)

        if res.status_code != 200:
            print(res.status_code)
            print(f"Failed to fetch data for category: {category_name}")
            return []
        return res.json()

    @staticmethod
    def search(keyword: str) -> list:
        session = CachedSession()
        _filter = [{"Key": "Category", "Items": [{"Term": "1-E5BEE36E"}]}]

        if Woolworths._session_id is None:
            session.get("https://www.woolworths.com.au", refresh=True)
            Woolworths._session_id = id(session)

        url = "https://www.woolworths.com.au/apis/ui/Search/products"
        headers = {
            "Accept": "application/json, */*",
            "Content-Type": "application/json",
            "Referer": f"https://www.woolworths.com.au/shop/search/products?searchTerm={keyword}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.",
        }
        body = {
            "Filters": [],
            "IsSpecial": False,
            "Location": f'/shop/search/products?{urlencode({"searchTerm": keyword})}',
            "PageNumber": 1,
            "PageSize": 36,
            "SearchTerm": keyword,
            "SortType": "TraderRelevance",
        }
        res = session.post(url=url, headers=headers, json=body, timeout=10)

        if res.status_code != 200:
            print(res.status_code)
            print(f"Failed to fetch data for {keyword}")
            return []
        return res.json()


if __name__ == "__main__":
    pass
