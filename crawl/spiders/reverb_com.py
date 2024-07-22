import json
from collections.abc import Iterator
from datetime import datetime
from urllib.parse import parse_qs, urlparse

from itemloaders import ItemLoader
from scrapy import Request, Spider
from scrapy.http import HtmlResponse
from scrapy.utils.project import get_project_settings

from crawl.items.product import ReverbProductItem
from crawl.services.links import get_scraping_links
from crawl.utils.extractors import chain_get
from crawl.utils.payload import build_product_payload, build_search_payload


class ReverbComSpider(Spider):
    name = "reverb.com"

    allowed_domains = ["reverb.com"]

    settings = get_project_settings()

    reverb_api_url = "https://rql.reverb.com/graphql"

    default_headers = {
        "content-type": "application/json",
        "origin": "https://reverb.com",
        "referer": "https://reverb.com/",
        "user-agent": settings["USER_AGENT"],
        "x-display-currency": "USD",
        "x-experiments": "proximity_features",
        "x-postal-code": "07936",
        "x-reverb-app": "REVERB",
        "x-secondary-user-enabled": "false",
        "x-shipping-region": "US_CON",
    }

    products_per_page = 12

    custom_settings = {
        "RETRY_TIMES": 2,
        "DOWNLOAD_DELAY": 1,
        "ITEM_PIPELINES": {"crawl.pipelines.TelegramNotificationPipeline": 300},
    }

    def start_requests(self) -> Iterator[Request]:
        for item in get_scraping_links():
            if "query" in item["link"]:
                filters = self._extract_query_params(url=item["link"])
                payload = build_search_payload(**filters, limit=self.products_per_page)
                callback = self.parse_reverb_search_api
            else:
                slug = self._extract_url_slug(url=item["link"])
                filters = self._extract_query_params(url=item["link"])
                payload = build_product_payload(
                    **filters, slug=slug, limit=self.products_per_page
                )
                callback = self.parse_reverb_product_api

            yield Request(
                method="POST",
                url=self.reverb_api_url,
                callback=callback,
                headers=self.default_headers,
                body=json.dumps(payload),
                cb_kwargs={"link": item["link"]},
            )

    def parse_reverb_product_api(self, response: HtmlResponse, link: str) -> list[dict]:
        data = chain_get(response.json(), "data", "allListings")
        yield from (
            self.parse_reverb_product(product=product, link=link)
            for product in data["listings"]
        )

    def parse_reverb_search_api(self, response: HtmlResponse, link: str) -> list[dict]:
        data = chain_get(response.json(), "data", "listingsSearch")
        yield from (
            self.parse_reverb_product(product=product, link=link)
            for product in data["listings"]
        )

    def parse_reverb_product(self, product: dict, link: str) -> ReverbProductItem:
        l = ItemLoader(item=ReverbProductItem(), selector=product)

        l.add_value("seller_name", chain_get(product, "shop", "name"))
        l.add_value(
            "seller_location", chain_get(product, "shop", "address", "displayLocation")
        )
        l.add_value(
            "seller_rating",
            chain_get(product, "seller", "feedbackSummary", "receivedCount"),
        )

        l.add_value("id", product["id"])
        l.add_value("title", product["title"])
        l.add_value("listing_type", product["listingType"])
        l.add_value("condition", chain_get(product, "condition", "displayName"))
        l.add_value("price", chain_get(product, "pricing", "buyerPrice", "display"))
        l.add_value(
            "shipping",
            chain_get(product, "shipping", "shippingPrices", 0, "rate", "display"),
        )
        l.add_value(
            "product_link",
            self._make_product_url(product_id=product["id"], slug=product["slug"]),
        )
        l.add_value("link", link)
        l.add_value("timestamp", chain_get(product, "publishedAt", "seconds"))

        l.add_value(
            "published",
            self._convert_timestamp_to_date(
                timestamp=chain_get(product, "publishedAt", "seconds")
            ),
        )

        return l.load_item()

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
    def _extract_query_params(url: str) -> dict[str, str]:
        params = parse_qs(qs=urlparse(url).query)
        return {param: values[0] for param, values in params.items()}
