# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RightmoveItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
    date_added = scrapy.Field()
    phone = scrapy.Field()
    seller = scrapy.Field()
    description = scrapy.Field()



    pass
