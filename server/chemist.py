from datetime import timedelta
import django
from bs4 import BeautifulSoup
import json

from os import environ
from requests_cache import CachedSession

from config.constants import HTTP_GET_HEADERS


# from spiders.coles import Coles as spider
# from config.constants import HTTP_GET_HEADERS

environ.setdefault("DJANGO_SETTINGS_MODULE", "doibuyit.settings")
django.setup()


session = CachedSession(
    "cachedRequests",
    backend="filesystem",
    serializer="json",
    allowable_methods=["HEAD", "GET", "POST"],
    expire_after=3600,
    stale_while_revalidate=timedelta(minutes=5),
)
session.cache.delete(older_than=timedelta(days=1))

url = "https://www.coles.com.au/on-special?filter_Special=halfprice&page=1"
response = session.get(
    url=url, headers=HTTP_GET_HEADERS, refresh=True
)  # Must be fresh, build updates constantly
soup = BeautifulSoup(response.text, features="html.parser")
print(soup.prettify())
api_data = json.loads(
    str(soup.find(id="__NEXT_DATA__").contents[0])
    if soup.find(id="__NEXT_DATA__")
    else "{}"
)

print(api_data)