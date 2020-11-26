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
    start_urls = ['https://qqc6k.com:5561/luyilu/']

    def parse(self, response):
        base_url = 'https://qql6k.com:5561'
        base_path = "../pic/"
        img_paths = response.xpath('//h2/a/@href').extract()
        names = response.xpath('//h2/a/@title').extract()
        # print("*"*200)
        # print(names)
        for img_path, name in zip(img_paths, names):
            item = ScrapylspItem()
            item["name"] = name
            mkdir(base_path + name)
            scrapy.Request(base_url + img_path, callback=self.parse_img(path=name))
        next_path = response.xpath('//div[2]/ul/li[6]/a/@href').extract_first()
        print()
        if next_path != "javascript:;":
            next_path = "https://qqc6k.com:5561/luyilu/" + next_path
            scrapy.Request(next_path, callback=self.parse())

    def parse_img(self, response, path):
        pass
