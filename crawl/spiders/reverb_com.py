from datetime import datetime
from typing import Iterator
from urllib.parse import urlparse

import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse
from scrapy.utils.project import get_project_settings

from crawl.const import LINKS_TO_CHECK
from crawl.utils.extractors import chain_get
from crawl.utils.payload import get_json_body_template


class ReverbComSpider(scrapy.Spider):
    name = "reverb.com"

    allowed_domains = ["reverb.com"]

    settings = get_project_settings()

    reverb_api_url = "https://rql.reverb.com/graphql"

    default_headers = {
        "authority": "rql.reverb.com",
        "content-type": "application/json",
        "origin": "https://reverb.com",
        "referer": "https://reverb.com/",
        "user-agent": settings["USER_AGENT"],
        "x-display-currency": "USD",
        "x-context-id": "9b89817b-e8d2-4d01-b03d-fdee0879c523",
        "x-experiments": "proximity_features",
        "x-item-region": "US",
        "x-postal-code": "19809",
        "x-reverb-app": "REVERB",
        "x-shipping-region": "US_CON",
    }

    products_per_page = 12

    custom_settings = {
        "RETRY_TIMES": 2,
        "DOWNLOAD_DELAY": 1,
        "ITEM_PIPELINES": {"crawl.pipelines.TelegramNotificationPipeline": 300},
    }

    def start_requests(self) -> Iterator[Request]:
        for item in LINKS_TO_CHECK:
            slug = self._extract_url_slug(url=item["link"])
            payload = self._build_request_payload(
                slug=slug, limit=self.products_per_page, offset=0
            )
            yield Request(
                method="POST",
                url=self.reverb_api_url,
                callback=self.parse_reverb_api,
                headers=self.default_headers,
                body=payload,
                cb_kwargs={"product_name": item["name"], "category_link": item["link"]},
            )

    def parse_reverb_api(
        self, response: HtmlResponse, product_name: str, category_link: str
    ) -> dict:
        data = chain_get(response.json(), 0, "data", "allListings")

        products_feed = {"category": product_name, "listings": []}

        for item in data["listings"]:
            seller_data = {
                "seller_name": chain_get(item, "shop", "name"),
                "seller_location": chain_get(
                    item, "shop", "address", "displayLocation"
                ),
                "seller_rating": chain_get(
                    item, "seller", "feedbackSummary", "receivedCount"
                ),
            }

            product_data = {
                "id": item["id"],
                "title": item["title"],
                "listing_type": item["listingType"],
                "condition": chain_get(item, "condition", "displayName"),
                "price": chain_get(item, "pricing", "buyerPrice", "display"),
                "shipping": chain_get(
                    item, "shipping", "shippingPrices", 0, "rate", "display"
                ),
                "product_link": self._make_product_url(
                    product_id=item["id"], slug=item["slug"]
                ),
                "category_link": category_link,
                "timestamp": chain_get(item, "publishedAt", "seconds"),
                "published": self._convert_timestamp_to_date(
                    timestamp=chain_get(item, "publishedAt", "seconds")
                ),
            }

            products_feed["listings"].append({**product_data, **seller_data})

        return products_feed

    @staticmethod
    def _make_product_url(product_id: str, slug: str) -> str:
        return f"https://reverb.com/item/{product_id}-{slug}"

    @staticmethod
    def _convert_timestamp_to_date(timestamp: int) -> str:
        return datetime.fromtimestamp(timestamp).isoformat()

    @staticmethod
    def _extract_url_slug(url: str) -> str:
        return urlparse(url).path.split("/")[-1]

    @staticmethod
    def _build_request_payload(slug: str, limit: int = 12, offset: int = 0) -> str:
        template = get_json_body_template()
        return template.render(slug=slug, limit=limit, offset=offset)
