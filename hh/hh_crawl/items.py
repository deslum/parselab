# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PersonItem(Item):
    full_name = Field()
    vacancy = Field()
    money = Field()
    birth_date = Field()
    last_hh_change_date = Field()
    date_added = Field()
    phone = Field()
    email = Field()
    link = Field()
    payment_required = Field()
    # define the fields for your item here like:
    # name = Field()
    pass
