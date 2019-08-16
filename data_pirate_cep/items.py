# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DataPirateCepItem(scrapy.Item):
    address = scrapy.Field(serializer=str)
    range_cep = scrapy.Field(serializer=str)
    uf = scrapy.Field(serializer=str)