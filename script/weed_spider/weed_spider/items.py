import scrapy

class Post(scrapy.Item):
    name = scrapy.Field()
    family = scrapy.Field() #科
    image_url = scrapy.Field()
    # location = scrapy.Field()
    # shooting_date = scrapy.Field()
    # post_data = scrapy.Field()
    # contributor__name = scrapy.Field()
