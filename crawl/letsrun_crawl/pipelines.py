# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy_mongodb import MongoDBPipeline
import datetime


class LetsrunCrawlPipeline(object):

    def process_item(self, item, spider):
        return item


class LetsrunMongoPipeline(MongoDBPipeline):

    def process_item(self, item, spider):
        item = dict(self._get_serialized_fields(item))

        if self.config['buffer']:
            self.current_item += 1

            if self.config['append_timestamp']:
                item['scrapy-mongodb'] = {'ts': datetime.datetime.utcnow()}

            self.item_buffer.append(item)

            if self.current_item == self.config['buffer']:
                self.current_item = 0
                return self.insert_item(self.item_buffer, spider)

            else:
                return item

        post = self.collection.find_one(
            {'post_id': item['post_id']}
        )
        if post is not None:
            raise DropItem(
                "Duplicate post found for id {0}".format(item['post_id'])
            )
        else:
            return self.insert_item(item, spider)
