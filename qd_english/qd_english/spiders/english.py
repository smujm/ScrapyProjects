import scrapy

from ..items import QdEnglishItem

class EnglishSpider(scrapy.Spider):
    name = 'english'
    allowed_domains = ['chinadaily.com.cn']
    start_urls = ['http://language.chinadaily.com.cn/thelatest/page_{}.html'.format(page) for page in range(1,293)]
    
    def parse(self, response):
        
        divs = response.xpath('//div[@class="gy_box"]')
        
        for div in divs:
            title = div.xpath('./div/p[1]/a/text()').get()
            title_href = 'http:' + div.xpath('./div/p[1]/a/@href').get()
            info = div.xpath('./div/p[2]/a/text()').get()
            img_url = 'http:' + div.xpath('./a/img/@src').get()
            
            
            item = QdEnglishItem(title=title, title_href=title_href, info=info, img_url=img_url)
            yield item
