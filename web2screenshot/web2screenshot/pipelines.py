# -*- coding: utf-8 -*-
import os


class ScreenerPipeline(object):
    def process_item(self, item, spider):
        # set root in settings
        root = '/home/lemur/Desktop'
        img_path = os.path.join(root, item['fn'])
        with open(img_path, mode='wb') as fd:
            fd.write(item['img'])

        return item
