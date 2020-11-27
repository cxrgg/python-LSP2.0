# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.http import Request
# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline

from scrapylsp.settings import IMAGES_STORE
from scrapylsp.utils import subBrackets, subUrlAfter, mkdir


class ScrapylspPipeline(ImagesPipeline):
    # 调用这个函数这要是为了将title传给file_path使用，
    def get_media_requests(self, item, info):
        imgUrl = item["imgUrl"]

        # 中间路径名称
        midFilePath = subBrackets(item['name'])

        # mkdir(IMAGES_STORE +midFilePath)
        yield Request(imgUrl, meta={'midFilePath': midFilePath})

    def file_path(self, request, response=None, info=None):
        # 提取出title
        midFilePath = request.meta['midFilePath']
        # print(midFilePath)
        prefix = midFilePath
        # https://pic.meinvtu123.net/tupian/2019/allimg/190321/21133024-1-3B4.jpg
        # 使用split('-')切割，提取最后一个作为文件名
        # name = request.url.split('-')[-1]
        # 构建完整存储路径并且返回
        # filename = os.path.join(image_store, name)
        # filename = prefix + "/" + subUrlAfter(request.url)
        print(prefix)
        filename = u'{0}/{1}'.format(prefix, subUrlAfter(request.url))
        print(filename)
        # print(filename)
        return filename

    def item_completed(self, results, item, info):
        # 图片下载完成后，返回的结果results
        print(results)
        return item
