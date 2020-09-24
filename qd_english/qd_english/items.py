# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QdEnglishItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    title_href = scrapy.Field()
    info = scrapy.Field()
    img_url = scrapy.Field()

    # scrapy 框架数据结构是一个类字典对象

