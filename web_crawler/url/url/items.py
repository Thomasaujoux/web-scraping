# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScraperItem(scrapy.Item):
    # The source URL
    url_from = scrapy.Field()
    # The destination URL
    url_to = scrapy.Field()