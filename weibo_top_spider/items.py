# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboTopSpiderItem(scrapy.Item):
    # 排名
    rank = scrapy.Field()
    # 热搜名称
    name = scrapy.Field()
    # 标签
    tag = scrapy.Field()
