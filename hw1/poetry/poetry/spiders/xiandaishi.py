import scrapy
from poetry.items import PoetryItem
from scrapy import Request

class XiandaishiSpider(scrapy.Spider):
    name = 'xiandaishi'
    allowed_domains = ['zgshige.com']
    start_urls = ['https://www.zgshige.com/c/2022-03-24/20924939.shtml']
    poem_num = 1000
    cur_poem_num = 0

    def parse(self, response):
        title = response.xpath('/html/body/div[5]/div[2]/div[1]/div[1]/h3/text()').extract()[0]
        authors = response.xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div/span[1]/span/text()').extract()
        dynasty = '现代'
        contents = response.xpath('//*[@id="content"]/div[2]/text()').extract()
        content_raw = ''.join(contents).split()
        content = ','.join(content_raw)
        content = content.replace('\u200b', '')
        author = ''.join(authors).strip()
        poem = PoetryItem()
        poem['title'] = title
        poem['author'] = author
        poem['dynasty'] = dynasty
        poem['content'] = content

        yield poem

        self.cur_poem_num += 1
        if self.cur_poem_num < self.poem_num:
            link = response.xpath('/html/body/div[4]/div[2]/div[1]/div[9]/ul/li[2]/a/@href').extract()[0]

            if 'https://www.zgshige.com' in link:
                next_url = link
            else:
                next_url = 'https://www.zgshige.com' + link

            yield Request(next_url, callback=self.parse)
