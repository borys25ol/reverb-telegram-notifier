import logging

from scrapy import Item, Spider
from scrapy.exceptions import NotConfigured
from scrapy.settings import BaseSettings
from tinydb import Query, TinyDB

from crawl.utils.telegram import send_message

logger = logging.getLogger(__name__)


class TelegramNotificationPipeline:
    """
    Process Reverb listings and send a message to the Telegram group
    if a new listing is available.
    """

    def __init__(self, db_path: str) -> None:
        self.listings: list[dict] = []
        self.db = TinyDB(db_path)

    @classmethod
    def from_settings(cls, settings: BaseSettings) -> "TelegramNotificationPipeline":
        if not settings.get("TELEGRAM_BOT_TOKEN"):
            raise NotConfigured("Telegram Bot token not provided")

        if not settings.get("TELEGRAM_CHAT_ID"):
            raise NotConfigured("Telegram Chat ID not provided")

        local_db_path = settings.get("JSON_DB_PATH")

        return cls(db_path=local_db_path)

    def process_item(self, item: Item, spider: Spider) -> Item:
        self.listings.append(item)
        return item

    def close_spider(self, spider: Spider) -> None:
        new_products = self._process_scraped_listings(listings=self.listings)
        for product in new_products:
            send_message(product=product)

    def _process_scraped_listings(self, listings: list[dict]) -> list[dict]:
        new_products = []

        for item in listings:
            for product in item["listings"]:
                if not self._check_if_product_exists(product_id=product["id"]):
                    logger.info(f"Inserting product with id: {product['id']}")
                    new_products.append(product)
                    self.db.insert(document=product)
                else:
                    logger.info(f"Product with id: {product['id']} already exists")

        return new_products

    def _check_if_product_exists(self, product_id: str) -> bool:
        product = Query()
        return bool(self.db.search(product.id == product_id))
