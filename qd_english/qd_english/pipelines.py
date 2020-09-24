# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter

# 记得去settings.py中打开ITEM_PIPELINES

class QdEnglishPipeline:
    def __init__(self):
        self.f = open('data.csv', mode='a', encoding='utf_8_sig', newline='')
        # 字段信息与items字段信息名称一致
        self.csv_write = csv.DictWriter(self.f, fieldnames=['title', 'title_href', 'info', 'img_url'])
        self.csv_write.writeheader()
        
    def process_item(self, item, spider):
        self.csv_write.writerow(dict(item))
        return item
    
    def close_file(self):
        self.f.close()