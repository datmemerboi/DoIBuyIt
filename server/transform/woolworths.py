from utils.date import get_previous_wednesday, get_upcoming_tuesday


class WoolworthsProduct:
    def __init__(self):
        self.barcode: str = None
        self.name: str = None
        self.brand: str = None
        self.image: str = None

        self.price: float = None
        self.viewed_date: str = None
        self.tentative_end_date: str = None
        self.cost_per_unit: float = None
        self.cost_per_unit_measure: str = None
        self.previous_price: float = None

        self.vendor: str = "WWL"
        self.url: str = None

    def to_dict(self) -> dict:
        return {
            "barcode": self.barcode,
            "name": self.name,
            "brand": self.brand,
            "image": self.image,
            "price": self.price,
            "viewed_date": self.viewed_date,
            "tentative_end_date": self.tentative_end_date,
            "cost_per_unit": self.cost_per_unit,
            "cost_per_unit_measure": self.cost_per_unit_measure,
            "previous_price": self.previous_price,
            "vendor": self.vendor,
            "url": self.url,
        }


def scrape_to_woolworths_product(scrape_product: dict):
    """
    Convert a scraped product to a WoolworthsProduct.
    """
    prod = WoolworthsProduct()
    prod.barcode = scrape_product["Barcode"]
    prod.name = scrape_product["DisplayName"]
    prod.brand = scrape_product["Brand"]
    prod.image = scrape_product["LargeImageFile"]

    prod.price = scrape_product["Price"]
    prod.viewed_date = get_previous_wednesday()
    prod.tentative_end_date = get_upcoming_tuesday()
    prod.cost_per_unit = scrape_product["CupPrice"]
    prod.cost_per_unit_measure = scrape_product["CupMeasure"]
    prod.previous_price = (
        scrape_product["WasPrice"] if scrape_product["WasPrice"] else None
    )

    prod.url = f"https://www.woolworths.com.au/shop/productdetails/{scrape_product['Stockcode']}/{scrape_product['UrlFriendlyName']}"

    return prod


def pick_products(res: list) -> list:
    """
    Convert woolworths response to a product list.
    """
    products = []
    for p in res["Bundles"]:
        if p.get("Products") is None or len(p["Products"]) < 0:
            continue
        products.append(scrape_to_woolworths_product(p["Products"][0]).to_dict())
    return products
