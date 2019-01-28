# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' #爬虫名称
    allowed_domains = ['itcast.cn'] #允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 最开始请求的url地址

    def parse(self, response):
        # # 处理start_urls对应的响应
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)

        list_li = response.xpath("//div[@class='tea_con']//li")
        # list1 = []
        for li in list_li:
            item = {}
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # list_li.append(item)
            # print(item)
            #yield后面的值必须是 Request对象, BaseItem类, dict字典 or None,列表会出错
            yield item  #item的值传到pipelines


