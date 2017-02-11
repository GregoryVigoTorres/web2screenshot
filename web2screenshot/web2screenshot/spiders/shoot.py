# -*- coding: utf-8 -*-
import re
from urllib.parse import urlparse, urlunparse
import base64

from colorama import Fore, Style

import lxml.html
import scrapy
from scrapy_splash import SplashRequest


class ShootSpider(scrapy.Spider):
    name = "shoot"
    # allowed_domains = []
    start_urls = ['https://thoughtmaybe.com/']
    link_urls = []

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,
                                self.parse,
                                endpoint='render.json',
                                args=self.settings.get('SPLASH_ARGS'))

    def extract_links(self, doc, response):
        """
        only get local links
        """
        links = doc.xpath('.//a')

        base_url = urlparse(response.url)

        def gen_links(links):
            for i in links:
                href = i.attrib.get('href')

                if not href:
                    continue

                href = href.strip()

                if href in self.link_urls:
                    continue

                if 'mailto:' in href:
                    continue

                if href.startswith('#'):
                    continue

                if '#' in href:
                    anchor = href.find('#')
                    href = href[0:anchor]

                # get real URLs for relative HREFs
                parsed_url = urlparse(href)

                if not parsed_url.scheme or parsed_url.netloc:
                    href = urlunparse((base_url.scheme,
                                       base_url.netloc,
                                       parsed_url.path,
                                       parsed_url.params,
                                       parsed_url.query,
                                       parsed_url.fragment))

                yield href

        hrefs = list(gen_links(links))
        self.link_urls.extend(hrefs)
        return set(hrefs)

    def parse(self, response):
        fn = response.url.replace('http://', '')
        fn = response.url.replace('https://', '')
        fn = fn.replace('/', '.')
        fn = fn.rstrip('.')
        fn+= '.jpeg'

        self.logger.info(f'{Fore.RED}{response.url} -> {fn}{Style.RESET_ALL}')

        img = base64.b64decode(response.data['jpeg'])

        doc = lxml.html.fromstring(response.text)
        links = self.extract_links(doc, response)

        yield {'img': img,
               'fn': fn}

        for url in links:
            yield SplashRequest(url,
                                self.parse,
                                endpoint='render.json',
                                args=self.settings.get('SPLASH_ARGS'))
