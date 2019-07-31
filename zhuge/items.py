# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    house_name = scrapy.Field() #楼盘名字
    style = scrapy.Field() #物业类别
    company = scrapy.Field() #开发商
    fitup = scrapy.Field()  #装修状况
    property = scrapy.Field() #产权年限
    greening_rate = scrapy.Field() #绿化率
    parking_num = scrapy.Field() #停车位
    area = scrapy.Field() #占地面积
    house_area = scrapy.Field() #建筑面积
    floor = scrapy.Field() #楼层状况
    fee = scrapy.Field() #物业费
    info = scrapy.Field()

