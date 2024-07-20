from crawl.utils.mongodb import get_mongo_product_collection


def get_available_product_ids() -> set[str]:
    collection = get_mongo_product_collection()
    result = collection.find(filter={}, projection={"id": 1})
    return {item["id"] for item in result}


def insert_new_products(products: list[dict]) -> None:
    collection = get_mongo_product_collection()
    collection.insert_many(documents=products)
