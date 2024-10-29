class WoolworthsProduct:
    def __init__(self):
        self.barcode: str = None
        self.stockcode: str = None
        self.name: str = None
        self.slug: str = None
        self.price: float = None
        self.cost_per_unit: float = None
        self.cost_per_unit_measure: str = None
        self.previous_price: float = None
        self.brand: str = None
        self.image: str = None

        self.source_base_url: str = "https://www.woolworths.com.au/shop/productdetails"

    def to_dict(self) -> dict:
        return {
            "barcode": self.barcode,
            "stockcode": self.stockcode,
            "name": self.name,
            "slug": self.slug,
            "price": self.price,
            "cost_per_unit": self.cost_per_unit,
            "cost_per_unit_measure": self.cost_per_unit_measure,
            "previous_price": self.previous_price,
            "brand": self.brand,
            "image": self.image,
        }


def scrape_to_woolworths_product(scrape_product: dict):
    """
    Convert a scraped product to a WoolworthsProduct.
    """
    prod = WoolworthsProduct()
    prod.barcode = scrape_product["Barcode"]
    prod.stockcode = scrape_product["Stockcode"]
    prod.name = scrape_product["DisplayName"]
    prod.slug = scrape_product["UrlFriendlyName"]
    prod.price = scrape_product["Price"]
    prod.cost_per_unit = scrape_product["CupPrice"]
    prod.cost_per_unit_measure = scrape_product["CupMeasure"]
    prod.previous_price = (
        scrape_product["WasPrice"] if scrape_product["WasPrice"] else None
    )
    prod.brand = scrape_product["Brand"]
    prod.image = scrape_product["MediumImageFile"]
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
