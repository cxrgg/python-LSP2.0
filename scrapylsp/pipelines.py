from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline

from scrapylsp.utils import subUrlAfter


class ScrapylspPipeline(ImagesPipeline):
    # 调用这个函数这要是为了将title传给file_path使用，
    def get_media_requests(self, item, info):
        imgUrl = item["imgUrl"]

        # 中间路径名称
        yield Request(imgUrl, meta={'name': item['name']})

    def file_path(self, request, response=None, info=None):
        # 提取出title
        name = request.meta['name']
        filename = u'{0}/{1}'.format(name, subUrlAfter(request.url))
        return filename

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        else:
            print("图片下载中" + '*' * 20 + image_paths[0])
        return item
