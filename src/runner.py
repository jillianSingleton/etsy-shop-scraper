thonpython
import json
import logging
from pathlib import Path

from extractors.shop_parser import ShopParser
from outputs.exporters import Exporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def load_inputs():
    data_file = Path(__file__).resolve().parents[1] / "data" / "inputs.sample.json"
    with open(data_file, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    logging.info("Starting Etsy Shop Scraper...")

    inputs = load_inputs()
    shops = inputs.get("shops", [])
    item_limit = inputs.get("itemLimit", None)

    parser = ShopParser(item_limit=item_limit)
    exporter = Exporter()

    all_results = []

    for shop_name in shops:
        logging.info(f"Processing shop: {shop_name}")
        try:
            shop_data = parser.scrape_shop(shop_name)
            all_results.extend(shop_data)
        except Exception as e:
            logging.error(f"Error scraping {shop_name}: {e}")

    exporter.export_json(all_results)
    logging.info("Scraping completed successfully.")

if __name__ == "__main__":
    main()