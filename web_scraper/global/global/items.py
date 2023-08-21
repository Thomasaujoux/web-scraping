# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DistributeurItem(scrapy.Item):
    horloge = scrapy.Field()
    distributeur = scrapy.Field()
    url = scrapy.Field()
    nom = scrapy.Field()
    prix = scrapy.Field()
    origine = scrapy.Field()
    quantite = scrapy.Field()
    EAN = scrapy.Field()
    reference = scrapy.Field()
    description_legale = scrapy.Field()
    description_marketing = scrapy.Field()
    ingredients = scrapy.Field()
    industriel= scrapy.Field()
    conservation = scrapy.Field()
    label = scrapy.Field()
    valeurs_nutritionnelles = scrapy.Field()
    fil_ariane = scrapy.Field()
    html = scrapy.Field()
    allergene=scrapy.Field()
    nutri_score=scrapy.Field()
    conseil_preparation=scrapy.Field()
    pass
