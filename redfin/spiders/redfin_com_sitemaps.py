import scrapy


class RedfinComSitemaps(scrapy.Spider):
    name = 'redfin_com_sitemaps'
    start_urls = ['https://www.redfin.com/sitemap']

    def parse(self, response):
        for link in response.xpath('//ul/li/div/a/@href').getall():
            if link.startswith('/sitemap/'):
                yield response.follow(link, callback=self.parse)
            else:
                yield {'url': link}
