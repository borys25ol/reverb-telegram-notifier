from crawl.clients import get_mongo_scraping_link_collection


def get_scraping_links() -> list[dict]:
    collection = get_mongo_scraping_link_collection()
    return list(collection.find(filter={}, projection={"name": 1, "link": 1}))
