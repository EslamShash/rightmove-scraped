import scrapy
from scrapy_selenium import SeleniumRequest
from ..items import RightmoveItem
class YorkSpider(scrapy.Spider):
    name = 'york'
    increment_by = 24
    index_number = 0
    def start_requests(self):
        yield SeleniumRequest(
            url="https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E1498&radius=40.0&propertyTypes=&mustHave=&dontShow=&furnishTypes=&keywords=",
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        items = RightmoveItem()
        homes = response.css(".l-searchResult.is-list")
        for home in homes:
            items['title'] = home.css(".propertyCard-title").css("::text").get()
            items['address'] = home.css(".propertyCard-address").css("::text").get()
            items['price'] = home.css(".propertyCard-priceValue").css("::text").get()
            items['date_added'] = home.css(".propertyCard-branchSummary-addedOrReduced").css("::text").get()
            items['phone'] = home.css(".propertyCard-contactsPhoneNumber").css("::text").get()
            items['seller'] = home.css(".propertyCard-content .propertyCard-branchLogo > a").css("::attr(title)").get()
            items['description'] = home.css("span[data-test='property-description']").css("::text").get()
            yield items
        next_page = f"https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E1498&radius=40.0&index={self.index_number}&propertyTypes=&mustHave=&dontShow=&furnishTypes=&keywords="
        if self.index_number < 1100:
            self.index_number += self.increment_by
            yield SeleniumRequest(
                url=next_page,
                wait_time=3,
                callback=self.parse
            )

