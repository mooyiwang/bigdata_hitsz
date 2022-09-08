import scrapy
from essay.items import EssayItem
from scrapy import Request


class MeiriyiwenSpider(scrapy.Spider):
    name = 'meiriyiwen'
    allowed_domains = ['meiriyiwen.com']
    start_urls = ['http://meiriyiwen.com/']
    item_num = 10000
    cur_item_num = 0

    def parse(self, response):
        title = response.xpath('string(//*[@id="article_show"]/h1)').extract()[0]
        author = response.xpath('string(//*[@id="article_show"]/p/span)').extract()[0]
        contents = response.xpath('string(//*[@id="article_show"]/div[1])').extract()[0]
        content_raw = ''.join(contents).split()
        content = ''.join(content_raw)
        content = content.replace('\u200b', '')

        item = EssayItem()
        item['title'] = title
        item['author'] = author
        item['content'] = content
        yield item
        self.cur_item_num += 1

        if self.cur_item_num < self.item_num:
            yield Request('http://meiriyiwen.com/', callback=self.parse, dont_filter=True)
