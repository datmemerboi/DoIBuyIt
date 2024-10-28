class WoolworthsProduct:
    def __init__(self):
        self.barcode: str = None
        self.name: str = None
        self.display_name: str = None
        self.slug: str = None
        self.price: float = None
        self.source_url: str = None
        self.cost_per_unit: float = None
        self.cost_per_unit_measure: str = None
        self.images: dict[str, str] = {
            "small": None,
            "medium": None,
            "large": None,
        }
        self.brand: str = None
        self.previous_price: float = None

    def to_dict(self) -> dict:
        return {
            "barcode": self.barcode,
            "name": self.name,
            "display_name": self.display_name,
            "slug": self.slug,
            "price": self.price,
            "source_url": self.source_url,
            "cost_per_unit": self.cost_per_unit,
            "cost_per_unit_measure": self.cost_per_unit_measure,
            "images": self.images,
            "brand": self.brand,
            "previous_price": self.previous_price,
        }


def scrape_to_woolworths_product(scrape_product: dict):
    """
    Convert a scraped product to a WoolworthsProduct.
    """
    prod = WoolworthsProduct()
    prod.barcode = scrape_product["Barcode"]
    prod.name = scrape_product["Name"]
    prod.display_name = scrape_product["DisplayName"]
    prod.slug = scrape_product["UrlFriendlyName"]
    prod.price = scrape_product["Price"]
    prod.source_url = f"https://www.woolworths.com.au/shop/productdetails/{scrape_product['Stockcode']}/{scrape_product['UrlFriendlyName']}"
    prod.cost_per_unit = scrape_product["CupPrice"]
    prod.cost_per_unit_measure = scrape_product["CupMeasure"]
    prod.images = {
        "small": scrape_product["SmallImageFile"],
        "medium": scrape_product["MediumImageFile"],
        "large": scrape_product["LargeImageFile"],
    }
    prod.brand = scrape_product["Brand"]
    prod.previous_price = (
        scrape_product["WasPrice"] if scrape_product["WasPrice"] else None
    )
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
