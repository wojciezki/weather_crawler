import scrapy
from scrapy.spiders import CrawlSpider, Rule
from weather.items import WeatherItem
from scrapy.linkextractors import LinkExtractor


class WeatherSpider(CrawlSpider):
    name = 'weather'
    allowed_domains = 'weather.com'
    start_urls = ['https://weather.com/weather/tenday/l/UKXX0085:1:UK',]

    def parse(self, response):
        divs = response.xpath('//div[@id="twc-scrollabe"]')

        for days in divs:
            import pdb
            pdb.set_trace()
            item = WeatherItem()
            # //*[@id="APP"]/div/div[7]/div[2]/div[3]/main/div[1]/span/div[1]/div[2]/div[1]/span/text()
            # item['day'] = days.css("div.date::text").extract(),
            item['day'] = days.xpath('//span[@class="day-detail clearfix"]/text()').extract_first()
            item['description'] = days.xpath('//td[@class="description"]//span/text()').extract_first()
            item['low_temp'] = days.xpath("//td[@class='temp']/div/span[1]/text()").extract_first()
            item['high_temp'] = days.xpath("//td[@class='temp']/div/span[3]/text()").extract_first()
            item['precip'] = days.xpath("//td[@class='precip']/div/span[2]/span/text()")\
                .extract_first()
            item['wind'] = days.xpath('//td[@class="wind"]/span/text()').extract_first()
            item['humidity'] = days.xpath('//td[@class="humidity"]/span/span/text()').extract_first()

            yield item

