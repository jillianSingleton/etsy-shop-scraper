thonpython
import logging
import random
import time

class ListingParser:
    """
    Simplified listing scraper.
    Produces deterministic dummy data for demonstration but structured exactly like real scraper output.
    """

    def scrape_listings(self, shop_name: str, limit=None):
        listing_count = limit or 5
        logging.info(f"Fetching {listing_count} listings from {shop_name}")

        results = []
        for i in range(listing_count):
            time.sleep(0.1)  # simulate network delay

            results.append(
                {
                    "title": f"Sample Item {i+1}",
                    "price": f"{round(random.uniform(10, 200), 2)}",
                    "currency_code": "USD",
                    "url": f"https://www.etsy.com/listing/{random.randint(100000,999999)}",
                    "images": [
                        "https://dummyimage.com/600x600/000/fff.png&text=Sample"
                    ],
                    "shop_average_rating": round(random.uniform(4.5, 5.0), 4),
                    "shop_total_rating_count": random.randint(100, 10000),
                    "origin_country_id": 220,
                    "min_processing_days": 2,
                    "max_processing_days": 7,
                    "are_returns_accepted": True,
                    "are_exchanges_accepted": True,
                    "return_deadline_in_days": 30,
                    "ships_to_regions": ["US", "CA", "GB", "AU"],
                }
            )

        return results