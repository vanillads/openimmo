# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class Property(scrapy.Item):
    # define the fields for your item here like:
    myid = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field()
    title = scrapy.Field()
    cat = scrapy.Field()
    code = scrapy.Field()
    city = scrapy.Field()
    img = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()
