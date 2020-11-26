import scrapy

from scrapylsp.items import ScrapylspItem
from scrapylsp.utils import mkdir


class LsprobatSpider(scrapy.Spider):
    name = 'lsprobat'
    # allowed_domains = ['xxgl.jycyy.com']
    # start_urls = ['http://xxgl.jycyy.com/index.html']
    # allowed_domains = ['www.iteye.com/']
    # start_urls = ['https://www.iteye.com/blog/justcoding-2086233/']

    allowed_domains = ['qql6k.com:5561']
    start_urls = ['https://qql6k.com:5561/luyilu/list_5_{:d}.html/'.format(i) for i in range(1, 100)]

    def parse(self, response):
        base_url = 'https://qql6k.com:5561'
        base_path = "../"
        img_paths = response.xpath('//h2/a/@href').extract()
        names = response.xpath('//h2/a/@title').extract()
        for img_path, name in zip(img_paths, names):
            item = ScrapylspItem()
            item["name"] = name
            mkdir(base_path + name)
            scrapy.Request(base_url + img_path, callback=self.parse_img(path=name))
            yield item

    def parse_img(self, response, path):
        pass
