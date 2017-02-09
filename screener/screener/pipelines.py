# -*- coding: utf-8 -*-
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScreenerPipeline(object):
    def process_item(self, item, spider):
        root = '/home/lemur/Desktop'
        img_path = os.path.join(root, item['fn'])
        with open(img_path, mode='wb') as fd:
            fd.write(item['img'])

        return item
