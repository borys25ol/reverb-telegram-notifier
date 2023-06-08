import logging

from pymongo import MongoClient
from pymongo.collection import Collection
from scrapy.utils.project import get_project_settings

logging.getLogger("pymongo.ocsp_support").setLevel(level=logging.CRITICAL)
logging.getLogger("urllib3.connectionpool").setLevel(level=logging.CRITICAL)

settings = get_project_settings()


def get_mongo_client() -> MongoClient:
    if conn_str := settings["MONGO_URI"]:
        return MongoClient(conn_str)
    raise ValueError("Mongo connection string is not provided in settings!")


def get_mongo_product_collection() -> Collection:
    client = get_mongo_client()

    if not settings["MONGO_DB"]:
        raise ValueError("Mongo Database name is not provided in settings!")

    if not settings["MONGO_PRODUCT_COLLECTION"]:
        raise ValueError("Mongo Collection name is not provided in settings!")

    return client[settings["MONGO_DB"]][settings["MONGO_PRODUCT_COLLECTION"]]


def get_mongo_scraping_link_collection() -> Collection:
    client = get_mongo_client()

    if not settings["MONGO_DB"]:
        raise ValueError("Mongo Database name is not provided in settings!")

    if not settings["MONGO_SCRAPING_LINKS_COLLECTION"]:
        raise ValueError("Mongo Collection name is not provided in settings!")

    return client[settings["MONGO_DB"]][settings["MONGO_SCRAPING_LINKS_COLLECTION"]]
