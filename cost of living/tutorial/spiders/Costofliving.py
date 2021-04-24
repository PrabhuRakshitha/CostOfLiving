import scrapy

from ..items import TutorialItem

class AuthorSpider(scrapy.Spider):
    name = 'COL'

    start_urls = ['https://www.numbeo.com/cost-of-living/country_result.jsp?country=United+States']

    def parse(self, response):
        for city in response.css('a.discreet_link'):
            city_href = city.css('a.discreet_link::attr(href)').get()
            yield response.follow(city_href, self.parse_city)

    def parse_city(self, response):
        loc_data = response.xpath('//body/div//span/a/span/text()').getall()
        count = 8
        for data in response.xpath('//body/div/table/tr'):
            col_data = TutorialItem()
            col_data['city'] = loc_data[2]
            col_data['country'] = loc_data[1]
            col_data['item_desc'] = data.xpath('//td/text()')[count].get()
            col_data['item_desc'] = col_data['item_desc'].strip()
            col_data['value'] = data.xpath('//td/text()')[count + 1].get()
            col_data['value'] = (col_data['value'].strip()).split()[0]
            count = count + 3

            yield col_data

