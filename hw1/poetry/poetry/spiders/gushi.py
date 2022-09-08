import scrapy
from poetry.items import PoetryItem
from scrapy import Request


class GushiSpider(scrapy.Spider):
    name = 'gushi'
    allowed_domains = ['gushici.net']
    start_urls = ['https://www.gushici.net/shici/23/42903.html']
    poem_num = 10000
    cur_poem_num = 0

    def parse(self, response):
        title = response.xpath('/html/body/div[2]/div[1]/div[1]/div[1]/h1/text()').extract()[0]
        author = response.xpath('/html/body/div[2]/div[1]/div[1]/div[1]/p/a[2]/text()').extract()[0]
        dynasty = response.xpath('/html/body/div[2]/div[1]/div[1]/div[1]/p/a[1]/text()').extract()[0]
        contents = response.xpath('/html/body/div[2]/div[1]/div[1]/div[1]/div/text()').extract()

        content = ','.join(contents).strip()
        poem = PoetryItem()
        poem['title'] = title
        poem['author'] = author
        poem['dynasty'] = dynasty
        poem['content'] = content
        yield poem
        self.cur_poem_num += 1
        # is_next_poem = False
        if self.cur_poem_num < self.poem_num:
            page_box_num = len(response.xpath('/html/body/div[2]/div[1]/div').extract())
            for i in range(2, page_box_num+1):
                if response.xpath(f'/html/body/div[2]/div[1]/div[{i}]/@class').extract()[0] == 'gushici':
                    next_url = 'https://www.gushici.net' + \
                        response.xpath(f'/html/body/div[2]/div[1]/div[{i}]/div[1]/p[1]/a/@href').extract()[0]
                    yield Request(next_url, callback=self.parse)
