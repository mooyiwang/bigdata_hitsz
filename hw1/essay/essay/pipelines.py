# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter


class EssayPipeline:

    def __init__(self):
        self.txtfile = open('pure_text.txt', 'w', encoding='utf-8')
        self.jsonfile = open('all_data.json', 'wb')
        self.exporter = JsonItemExporter(self.jsonfile, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.txtfile.close()
        self.exporter.finish_exporting()
        self.jsonfile.close()

    def process_item(self, item, spider):
        self.txtfile.write(item['content'] + '\n')
        self.exporter.export_item(item)
        return item
