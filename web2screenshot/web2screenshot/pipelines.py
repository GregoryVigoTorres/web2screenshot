# -*- coding: utf-8 -*-
import os
from colorama import Fore, Style
import logging


class ScreenerPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        logging.info('{}Data Root{}{}'.format(Fore.CYAN,
                                              crawler.settings.get('DATA_DIR'),
                                              Style.RESET_ALL))
        C = cls()
        C.root = crawler.settings.get('DATA_DIR')
        return C

    def process_item(self, item, spider):
        img_path = os.path.join(self.root, item['fn'])

        with open(img_path, mode='wb') as fd:
            fd.write(item['img'])

        return item
