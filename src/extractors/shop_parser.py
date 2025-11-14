thonpython
import requests
import logging
from .listing_parser import ListingParser

class ShopParser:
    BASE_URL = "https://www.etsy.com/shop/{}"

    def __init__(self, item_limit=None):
        self.item_limit = item_limit
        self.listing_parser = ListingParser()

    def scrape_shop(self, shop_name: str):
        url = self.BASE_URL.format(shop_name)
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            raise ValueError(f"Failed accessing shop page: {shop_name}")

        logging.info(f"Fetched shop page for {shop_name}")

        # Real Etsy scraping would require HTML parsing; simplified here
        # Simulated structure for demonstration
        shop_info = {
            "shop_name": shop_name,
            "shop_url": url,
        }

        listings = self.listing_parser.scrape_listings(shop_name, self.item_limit)
        results = []

        for listing in listings:
            merged = {
                **listing,
                **shop_info,
            }
            results.append(merged)

        return results