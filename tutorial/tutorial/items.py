from scrapy.item import Item, Field

class QuestionItem(Item):
        url = Field()
        question = Field()
        title = Field()
        answer = Field()
        geolocation = Field()
