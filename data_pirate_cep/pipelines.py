# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem
from data_pirate_cep.utils import beautify_item, validate_item, write_addresses

class DataPirateCepPipeline(object):
    def open_spider(self, spider):
        with open('uf.json', 'r', encoding='utf-8') as uf_file:
            ufs_string = uf_file.readline()
            ufs = json.loads(ufs_string).get('ufs')
            for uf in ufs:
                spider.addresses[uf] = []

    def process_item(self, item, spider):
        if validate_item(item):
            beautify_item(item)
            spider.addresses[item.get('uf')].append([item.get('address'), item.get('range_cep')])
            return item
        else:
            raise DropItem('Invalid Item')

    def close_spider(self, spider):
        write_addresses(spider.addresses)
        print('jsonlines file created')
