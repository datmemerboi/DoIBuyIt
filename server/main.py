import json
from sys import argv

from utils.woolworths import pick_products
from spiders.woolworths import Woolworths

print(json.dumps(pick_products(Woolworths.category(argv[1])), indent=2))
