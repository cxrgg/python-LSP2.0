import scrapy

from scrapylsp.items import ItemImage
from scrapylsp.settings import IMAGES_STORE
from scrapylsp.utils import subUrlBefore, mkdir, subBrackets


class LsprobatSpider(scrapy.Spider):
    name = 'lsprobat'

    allowed_domains = ['qql6k.com']
    start_urls = ['https://qql6k.com:5561/luyilu/']

    def parse(self, response):
        base_url = 'https://qql6k.com:5561'
        img_paths = response.xpath('//h2/a/@href').extract()
        names = response.xpath('//h2/a/@title').extract()

        for img_path, name in zip(img_paths, names):
            # 这一图级的名字(一定要在这传,后面麻烦)
            name = subBrackets(name)
            mkdir(IMAGES_STORE + name)
            yield scrapy.Request(base_url + img_path, callback=self.parse_img, meta={'name': name})

        # 文件列表下一页自动跳转
        next_path = response.xpath('//div[2]/ul/li/a/@href').extract()[-1]
        if next_path:
            next_path = "https://qql6k.com:5561/luyilu/" + next_path
            yield scrapy.Request(next_path, callback=self.parse)

    def parse_img(self, response):
        # 处理图片页面:获取文件夹名称和图片下载链接
        imgUrls = response.xpath("//div/article/p/img/@src").extract()
        # 当前图片目录名
        name = response.meta['name']
        # name = response.xpath("//h1/text()").extract_first()
        for imgUrl in imgUrls:
            item = ItemImage()
            item["name"] = name
            item["imgUrl"] = imgUrl
            yield item
        # 当前图片页面下一页前缀
        pic_prefix_next = subUrlBefore(response.request.url)

        # 图片页面下一页,自动跳转
        next_img_paths = response.xpath("//div[2]/ul/li/a/@href").extract()
        if next_img_paths:
            next_img_path = pic_prefix_next + next_img_paths[-1]
            yield scrapy.Request(next_img_path, callback=self.parse_img, meta={'name': name})
