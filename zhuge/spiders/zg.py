# -*- coding: utf-8 -*-
import scrapy
from zhuge.items import NewHouseItem
from scrapy_redis.spiders import RedisSpider


class ZgSpider(RedisSpider):
    name = "zg"
    allowed_domains = ["zhuge.com"]
    redis_key = "zhuge:start_urls" 

    def parse(self, response):
        provinces = response.xpath("//li[@class='area-city-box']")
        for pr in provinces:
            province_name = pr.xpath("./p/text()").get()
            citys = pr.xpath(".//div/a")

            for city in citys:
                city_name = city.xpath("./text()").get()
                city_url = city.xpath(".//@href").get()
                #print(city_url)
                city_url_text = city_url.split('.')[0]

                NewHouse_link = 'http:' + city_url_text + '.xinfang.zhuge.com'
                if NewHouse_link:

                OldHouse_link = 'http:' + city_url_text + '.ershoufang.zhuge.com'

                    yield scrapy.Request(url=NewHouse_link, callback=self.parse_new, meta={"info": (province_name, city_name, NewHouse_link)})
                    break
                yield scrapy.Request(url=OldHouse_link, callback=self.parse_esf, meta={"info": (province_name, city_name)})

    def parse_new(self, response):
        province, city, new_url = response.meta.get('info')
        house_list = response.xpath("//div[@class='house_details']")
        for house in house_list:
            house_name = house.xpath(".//a[contains(@class, house_title)]/text()").get()
            house_url = house.xpath(".//a[contains(@class, house_title)]/@href").get()
            #print(house_name+":  "+ house_url)
            house_detail_url = "http:" + house_url + "loupanxiangqing"
            yield scrapy.Request(url=house_detail_url, callback=self.parse_new_detail, meta={"info": (house_name, house_detail_url)})

        next_page = response.xpath("//a[@class='laypage-next']/@href").get()
        next_page_url = new_url + next_page

        if next_page:
           yield scrapy.Request(url=next_page_url, callback=self.parse_new, meta={"info": (province, city, new_url)})


    def parse_esf(self, response):
        province,city = response.meta.get('info')  
        pass

    def parse_new_detail(self, response):
        house_name, new_detail_url = response.meta.get('info')
        detail_item = NewHouseItem()
        ul = response.xpath("//ul[contains(@class, 'detail_ul')]")
        detail_item['style'] = ul[0].xpath(".//li[2]//i[2]/text()").get()
        detail_item['fitup'] = ul[0].xpath(".//li[3]//i[2]/text()").get()
        detail_item['property'] = ul[0].xpath(".//li[4]//i[2]/text()").get()
        detail_item['company'] = ul[0].xpath(".//li[6]//i[2]/text()").get()

        detail_item['area'] = ul[2].xpath(".//li[1]//i[2]/text()").get()
        detail_item['floor'] = ul[2].xpath(".//li[2]//i[2]/text()").get()
        detail_item['house_area'] = ul[2].xpath(".//li[3]//i[2]/text()").get()
        detail_item['greening_rate'] = ul[2].xpath(".//li[4]//i[2]/text()").get()
        detail_item['parking_num'] = ul[2].xpath(".//li[7]//i[2]/text()").get()
        detail_item['fee'] = ul[2].xpath(".//li[11]//i[2]/text()").get()

        detail_item['info'] = response.xpath("//div[@class='navitem'][4]//div[contains(@class, 'loupan_huodong')]/text()").get()
        yield detail_item








