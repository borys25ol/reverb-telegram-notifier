import scrapy
from itemloaders.processors import TakeFirst


class ReverbProductItem(scrapy.Item):
    """
    Item to store info about Reverb product.
    """

    seller_name = scrapy.Field(output_processor=TakeFirst())
    seller_location = scrapy.Field(output_processor=TakeFirst())
    seller_rating = scrapy.Field(output_processor=TakeFirst())
    id = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    listing_type = scrapy.Field(output_processor=TakeFirst())
    condition = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    shipping = scrapy.Field(output_processor=TakeFirst())
    product_link = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    timestamp = scrapy.Field(output_processor=TakeFirst())
    published = scrapy.Field(output_processor=TakeFirst())
