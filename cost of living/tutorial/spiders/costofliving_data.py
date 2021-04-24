
import scrapy

from ..items import TutorialItem ,CityItem

class AuthorSpider(scrapy.Spider):
    name = 'COLD'

    start_urls = ['https://www.numbeo.com/cost-of-living/country_result.jsp?country=India&displayCurrency=USD']

    def parse(self, response):
        for city in response.css('a.discreet_link'):
            city_href = city.css('a.discreet_link::attr(href)').get()
            yield response.follow(city_href, self.parse_city)

    def parse_city(self, response):
        loc_data = response.xpath('//body/div//span/a/span/text()').getall()
        count = 8
        city_data = CityItem()
        for data in response.xpath('//body/div/table/tr'):
            city_data['city'] = loc_data[2]
            city_data['country'] = loc_data[1]
            city_data['COL_data'] = data.xpath('//td/text()')[count].get()
            city_data['COL_data'] = city_data['COL_data'].strip()
            count = count + 3
            yield city_data