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
    #origine = scrapy.Field()
    quantite = scrapy.Field()
    EAN = scrapy.Field()
    reference = scrapy.Field()
    #description_legale = scrapy.Field()
    #description_marketing = scrapy.Field()
    #ingredients = scrapy.Field()
    #industriel= scrapy.Field()
    #conservation = scrapy.Field()
    label = scrapy.Field()
    valeurs_nutritionelles = scrapy.Field()
    fil_ariane = scrapy.Field()
    html = scrapy.Field()
    pass

# class FranprixItem(scrapy.Item):
#     nom=scrapy.Field()
#     pass