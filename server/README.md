# Getting Started with Django and Uvicorn

1. **Install dependencies**:
  ```bash
  uv sync --all-groups
  ```
2. Import data
  ```bash
  python manage.py shell < main.py
  ```
3. Run the django server
  ```bash
  uv run python manage.py runserver 8080
  ```

# NOTES for Coles Spider
Typical page: https://www.coles.com.au/on-special?pid=homepage_cat_explorer_specials&filter_Special=halfprice&page=1
Typical product: https://www.coles.com.au/product/pringles-bbq-stacked-potato-chips-134g-2784070

https://github.com/nguyentansinh123/PriceChecking/blob/main/backend/src/controller/func/Coles/halfPrice.ts

https://github.com/nguyentansinh123/Scraping-Coles-Woolworths-IGA/blob/main/colesspecialCatalogs.js

https://github.com/adambadge/coles-scraper/issues/1

https://www.coles.com.au/api/bff/products/123011?storeId=647&subscription-key=eae83861d1cd4de6bb9cd8a2cd6f041e

curl -X GET \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36" \
  "https://www.coles.com.au/api/bff/products/123011?storeId=647&subscription-key=eae83861d1cd4de6bb9cd8a2cd6f041e"
