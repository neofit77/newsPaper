# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class newsPaperItem(scrapy.Item):
    Author_Name = scrapy.Field()
    Publication_Date = scrapy.Field()
    Keywords = scrapy.Field()
    Article_text = scrapy.Field()
