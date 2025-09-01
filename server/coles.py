from datetime import timedelta
import django
from bs4 import BeautifulSoup
import json

import scrapy

span_class = "price__value"


class ColesSpider(scrapy.Spider):
    name = "coles"
    start_urls = ["https://www.coles.com.au/on-special"]
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    


    def parse(self, res):
        url = "https://www.coles.com.au/on-special"

        headers = {
            'User-Agent': self.user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-ch-ua-platform": '"macOS"',
            'Referrer': 'https://www.coles.com.au/',
            'Origin': 'https://www.coles.com.au',
        }

        scrapy.Request(url, headers=headers)

        print(res.text)
        for price in res.css("product__title"):
            yield {"price": "found"}
