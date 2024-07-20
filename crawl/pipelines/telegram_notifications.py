import logging

from itemadapter import ItemAdapter
from scrapy import Spider

from crawl.items.product import ReverbProductItem
from crawl.services.products import get_available_product_ids, insert_new_products
from crawl.utils.telegram import send_message

logger = logging.getLogger(__name__)


class TelegramNotificationPipeline:
    """
    Process Reverb listings and send a message to the Telegram group
    if a new listing is available.
    """

    def __init__(self) -> None:
        self.scraped_products: list[ItemAdapter] = []

    def process_item(
        self, item: ReverbProductItem, spider: Spider
    ) -> ReverbProductItem:
        self.scraped_products.append(ItemAdapter(item))
        return item

    def close_spider(self, spider: Spider) -> None:
        available_ids = get_available_product_ids()
        logger.info(f"Got {len(available_ids)} available products")

        if new_products := self._process_scraped_products(
            scraped_products=self.scraped_products, available_ids=available_ids
        ):
            insert_new_products(products=new_products)

        logger.info(f"Got {len(new_products)} new products after scraping")

        for product in new_products:
            send_message(product=product)

    @staticmethod
    def _process_scraped_products(
        scraped_products: list[ItemAdapter], available_ids: set[str]
    ) -> list[dict]:
        return [
            product.asdict()
            for product in scraped_products
            if product["id"] not in available_ids
        ]
