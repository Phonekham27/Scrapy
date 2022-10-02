import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.baoquangbinh.vn/chinh-tri/202210/dien-mung-nhan-ky-niem-73-nam-ngay-thanh-lap-nuoc-cong-hoa-nhan-dan-trung-hoa-2203929/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath("//h2[@id='title']").get()
        content = response.xpath("//div[@class='col-md-8 mb-5']/div[2]/div[3]").extract_first().strip()
        day = response.xpath("//div[@class='d-flex justify-content-between align-items-end page-detail-meta mb-3']/ul[@class='list-unstyled list-inline mb-0']/li[@class='list-inline-item']").get()
        print('tieu de', title)
        print('content', content)
        print('day', day)