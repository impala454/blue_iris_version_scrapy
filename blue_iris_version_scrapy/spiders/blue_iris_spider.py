import datetime
import scrapy


class BlueIrisSpider(scrapy.Spider):
    name = "version"

    def start_requests(self):
        url = 'http://blueirissoftware.com/updates/'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        s = response.css('h3::text').extract_first()
        version = s[:s.find('(') - 1].split()[1]
        yield {
            'version': version,
            'version_major': int(version.split('.')[0]),
            'version_minor': int(version.split('.')[1]),
            'version_patch': int(version.split('.')[2]),
            'version_build': int(version.split('.')[3]),
            'date': datetime.datetime.strptime(s[s.find('(') + 1:s.find(')')], '%B %d, %Y').date()
        }
