# -*- coding: utf-8 -*-
import base64

from colorama import Fore, Style

import scrapy
from scrapy_splash import SplashRequest


class ShootSpider(scrapy.Spider):
    name = "shoot"
    allowed_domains = ['https://thoughtmaybe.com/']
    start_urls = ['https://thoughtmaybe.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,
                                self.parse,
                                endpoint='render.jpeg',
                                args=self.settings.get('SPLASH_ARGS'))

    def parse(self, response):
        img = base64.b64decode(response.body)

        # print(f'{Fore.RED} {type(response.body)}')

        fn = response.url.replace('http://', '')
        fn = response.url.replace('https://', '')
        fn = fn.replace('/', '.')
        fn = fn.rstrip('.')
        fn+= '.jpeg'
        yield {'img': response.body, 'fn': fn}

