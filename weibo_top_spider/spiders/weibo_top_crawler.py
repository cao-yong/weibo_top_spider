import random

import scrapy
from scrapy.http import Request

from user_agent import agents
from weibo_top_spider.items import WeiboTopSpiderItem


class WeiboTopCrawler(scrapy.Spider):
    name = "weibo_top_spider"
    allowed_domains = ["weibo.com"]
    start_urls = [
        "https://s.weibo.com/top/summary/summary?cate=realtimehot"
    ]

    def start_requests(self):
        for url in self.start_urls:
            header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip,deflate,sdch',
                'Accept-Language': 'zdeprecatedh-CN,zh;q=0.8,en;q=0.6',
                'Host': 's.weibo.com',
                'User-Agent': random.choice(agents),
                'Referer': url,
            }
            yield Request(url, callback=self.parse, headers=header)

    def parse(self, response):
        self.logger.info('the url is :%s', response.url)
        if response.status == 200:
            hxs = scrapy.Selector(response)
            xs = hxs.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
            index = 0
            for x in xs:
                storage_item = WeiboTopSpiderItem()
                rank = index
                name = x.xpath('td[2]/a/text()').extract_first()
                tag = x.xpath('td[3]/i/text()').extract_first()
                storage_item['rank'] = rank
                storage_item['name'] = name
                storage_item['tag'] = tag
                if index != 0:
                    yield storage_item
                index += 1
            else:
                return ''
