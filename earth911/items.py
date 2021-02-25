# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose

def get_city(City):
    if City:
        City = City.split(' ')[:-2]
        City = ' '.join(City)
        City = City.rstrip(',')
        return City
    return City

def get_state(State):
    if State:
        return State.split(' ')[-2]
    return State

def get_zip(Zip_Code):
    if Zip_Code:
        return Zip_Code.split(' ')[-1]
    return Zip_Code

class Earth911Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field(
        output_processor = TakeFirst()
    )
    Phone_Number = scrapy.Field(
        output_processor = TakeFirst()
    )
    Street_Address = scrapy.Field(
        output_processor = TakeFirst()
    )
    City = scrapy.Field(
        input_processor=MapCompose(get_city),
        output_processor = TakeFirst()
    )
    State = scrapy.Field(
        input_processor=MapCompose(get_state),
        output_processor = TakeFirst()
    )
    Zip_Code = scrapy.Field(
        input_processor=MapCompose(get_zip),
        output_processor = TakeFirst()
    )
