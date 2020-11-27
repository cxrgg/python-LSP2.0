# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import requests
# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline

from scrapylsp.items import ItemName, ItemImage
from scrapylsp.settings import IMAGES_STORE
from scrapylsp.utils import subBrackets, mkdir, subUrlAfter


class ScrapylspPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        filePath = IMAGES_STORE + subBrackets(item['name'])
        mkdir(filePath)
        if isinstance(item, ItemName):
            # mkdir(IMAGES_STORE + subBrackets(item['name']))
            pass
        if isinstance(item, ItemImage):
            imgUrl = item["imgUrl"]
            with open(filePath + "/" + subUrlAfter(imgUrl), 'wb') as handle:
                response = requests.get(imgUrl, stream=True)
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
        return item

    # def file_path(self, request, response=None, info=None):
    #     # 提取url前面名称作为图片名。
    #     image_guid = request.url.split('/')[-1]
    #     # 接收上面meta传递过来的图片名称
    #     name = request.meta['name']
    #     # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
    #     name = re.sub(r'[？\\*|“<>:/]', '', name)
    #     # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
    #     filename = u'{0}/{1}'.format(name, image_guid)
    #     return filename
