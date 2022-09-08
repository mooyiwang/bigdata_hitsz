# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EssayItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()

