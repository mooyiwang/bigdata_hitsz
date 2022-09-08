# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PoetryPipeline:
    def __init__(self):
        self.full_file = ''
        self.pure_file = ''

    def process_item(self, item, spider):
        if item['content'] is not '':
            self.full_file = open('sanwen_full.txt', 'a', encoding='utf-8')
            self.pure_file = open('sanwen_pure.txt', 'a', encoding='utf-8')
            self.full_file.write(item['title'] + ' ' + item['author'] + ' ' + item['dynasty'] + ' ' + item['content'] + '\n')
            self.pure_file.write(item['content'] + '\n')
            self.full_file.close()
            self.pure_file.close()
        return item
