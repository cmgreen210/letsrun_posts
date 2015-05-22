# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class LetsrunPostItem(scrapy.Item):

    thread_id = Field()
    post_id = Field()
    post_author = Field()

    subject = Field()
    timestamp = Field()

    in_reply_url = Field()
    reply_to_author = Field()

    post_text = Field()
