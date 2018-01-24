# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class CrawlertestPipeline(object):
    def __init__(self):
        self.file = codecs.open('nigga.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):

        if "Hong Kong" in item['text']:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
            return item

        return

    def spider_closed(self, spider):
        self.file.close()