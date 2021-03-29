import io
# import os
from csv import DictReader

import scrapy

from .redfin_web_page import RedfinPage


# TODO: 
# remove comments if new solution proves to be better
# this_directory = os.path.dirname(os.path.realpath(__file__))


class RedfinComSpider(scrapy.Spider):
    name = 'redfin_com'
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_poet.InjectionMiddleware': 543,
        }
    }


    start_urls = ['https://www.redfin.com/sitemap']
    
    def parse(self, response):
        for link in response.xpath('//ul/li/div/a/@href').getall():
            if link.startswith('/sitemap/'):
                yield response.follow(link, callback=self.parse)
            elif '/home/' in link:
                yield response.follow(link, callback=self.parse_listing)
            else:
                yield response.follow(link, callback=self.parse_listing_overview)


    '''
    def start_requests(self):
        for line in open(f'{this_directory}/url_strings'):
            yield scrapy.Request(
                f'https://www.redfin.com/city/{line}',
                callback=self.parse_listing_overview
            )
    '''

    def parse_listing_overview(self, response):
        csv_link = response.xpath('//a[@id="download-and-save"]/@href').get()
        yield response.follow(csv_link, callback=self.parse_listings_csv)

    def parse_listings_csv(self, response):
        r = DictReader(io.StringIO(response.text))
        # That's the name of the column in the csv. I'm not kidding.
        column_name = 'URL (SEE http://www.redfin.com/buy-a-home/comparative-market-analysis FOR INFO ON PRICING)'
        for row in r:
            yield scrapy.Request(row[column_name], callback=self.parse_listing)

    def parse_listing(self, response, page: RedfinPage):
        return page.to_item()
