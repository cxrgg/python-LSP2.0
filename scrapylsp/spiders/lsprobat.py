import scrapy

from scrapylsp.items import ItemName, ItemImage
from scrapylsp.utils import subUrlBefore


class LsprobatSpider(scrapy.Spider):
    name = 'lsprobat'

    allowed_domains = ['qql6k.com']
    start_urls = ['https://qql6k.com:5561/luyilu/']

    def parse(self, response):
        base_url = 'https://qql6k.com:5561'
        img_paths = response.xpath('//h2/a/@href').extract()
        names = response.xpath('//h2/a/@title').extract()

        for img_path, name in zip(img_paths, names):
            # item = ItemName()
            # item["name"] = name
            # yield item
            yield scrapy.Request(base_url + img_path, callback=self.parse_img)

        # 文件列表下一页自动跳转
        next_path = response.xpath('//div[2]/ul/li/a/@href').extract()[-1]
        print("-" * 200)
        print(next_path)
        print("-" * 200)
        if next_path != "javascript:;":
            next_path = "https://qql6k.com:5561/luyilu/" + next_path
            print("列表" + next_path)
            yield scrapy.Request(next_path, callback=self.parse)

    def parse_img(self, response):
        # 处理图片页面:获取文件夹名称和图片下载链接
        imgUrls = response.xpath("//div/article/p/img/@src").extract()
        name = response.xpath("//h1/text()").extract_first()
        for imgUrl in imgUrls:
            item = ItemImage()
            item["name"] = name
            item["imgUrl"] = imgUrl
            yield item
        # 当前图片页面下一页前缀
        pic_prefix_next = subUrlBefore(response.request.url)

        # 图片页面下一页,自动跳转
        next_img_path = response.xpath("//div[2]/ul/li/@href").extract()[-1]
        if next_img_path is not None:
            next_img_path = pic_prefix_next + next_img_path
            print("*" * 200)
            print("图片页面下一页地址" + next_img_path)
            yield scrapy.Request(next_img_path, callback=self.parse_img)
