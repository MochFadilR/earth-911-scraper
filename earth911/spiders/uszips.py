import scrapy
from scrapy.loader import ItemLoader
from ..items import Earth911Item
import pandas as pd

data = pd.read_csv('earth911/uszips.csv')
zip_list = data['zip']
zip_set = set(zip_list)
zip_codes = list(zip_set)
urls = []

for zip in zip_codes:
    urls.append(f'https://search.earth911.com/?what=%234+Rigid+Plastics&where={zip}&max_distance=25')

class UszipsSpider(scrapy.Spider):
    name = 'uszips'
    allowed_domains = ['earth911.com']
    start_urls = ['https://search.earth911.com/?what=%234+Rigid+Plastics&where=93446&max_distance=25']

    def parse(self, response):
        listings = response.xpath('//ul[@class="result-list"]/li')
        print(listings[2])
        listing = listings[2]
        Name = listing.xpath('//h2/a/text()').get()
        Phone_Number = listing.xpath('//p[@class="phone"]/text()').get()
        Street_Address = listing.xpath('//p[@class="address1"]/text()').get()
        City = listing.xpath('//p[@class="address3"]/text()').get().split(' ')[:-2]
        City = ' '.join(City)
        City = City.rstrip(',')
        State = listing.xpath('//p[@class="address3"]/text()').get().split(' ')[-2]
        Zip_Code = listing.xpath('//p[@class="address3"]/text()').get().split(' ')[-1]

        # yield loader.load_item() 
    
        yield {
            "Name": Name,
            "Phone Number": Phone_Number,
            "Street Address": Street_Address,
            "City": City,
            "State": State,
            "Zip Code": Zip_Code
        }


# def start_requests(self):
    #     for zip_code in zip_list:
    #         yield scrapy.Request(
    #             url=f"https://search.earth911.com/?what=%234+Rigid+Plastics&where={zip_code}&max_distance=25",
    #             callback=self.parse)