# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#使用pipeline，要开启settings中的ITEM_PIPELINES
#多个pipeline的作用，不同的pipeline处理不同的item内容，一个爬虫项目包含多个爬虫，一个spider可能做不同的操作，比如存入不同的数据库
# pipeline的权重越小，优先级越高，pipeline中的process_item方法名不能改为其他名称

class Myspider02Pipeline(object):
    def process_item(self, item, spider):
        item["hello"] = "world"
        return item  #这个上一个判断要有return，否则下面打印就是None

class Myspider02Pipeline1(object):
    def process_item(self, item, spider):
        print(item)   #数值会先经过小的，后经过大的，经过小的添加hell world，如果下面大，先经过下面，这个打印就不会有helloworld
        return item


#实现存储方法
import json
class Myspider02Pipeline2(object):
    def process_item(self, item, spider):
        with open("xxxx.text",'a')as f:
            json.dumps(item,f,ensure_ascii=False,indent=2)
