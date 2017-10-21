# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class WeatherItem(scrapy.Item):
    day = scrapy.Field()
    description = scrapy.Field()
    high_temp = scrapy.Field()
    low_temp = scrapy.Field()
    precip = scrapy.Field()
    wind = scrapy.Field()
    humidity = scrapy.Field()

