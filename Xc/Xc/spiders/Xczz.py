# -*- coding: utf-8 -*-
import scrapy
from Xc.items import XcItem

class XczzSpider(scrapy.Spider):
    name = 'Xczz'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/']

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        item1 = response.xpath('//tr[@class="odd"]')
        item2 = response.xpath('//tr[@class=""]')
        items = item1 + item2
        print(items)

        infos = XcItem()

        for item in items:
            # print(item)
            country = item.xpath('./td/img/@alt').extract()
            if country != []:
                country  = country[0]
            else:
                country = None
            ipaddress = item.xpath('./td[2]/text()').extract()
            try:
                ipaddress = ipaddress[0]
            except:
                ipaddress = None
            port = item.xpath('./td[3]/text()').extract()
            try:
                port = port[0]
            except:
                port = None
            serveraddr = item.xpath('./td[4]/text()').extract()
            try:
                serveraddr = serveraddr[0]
            except:
                serveraddr = None
            isanonymous = item.xpath('./td[5]/text()').extract()
            try:
                isanonymous = isanonymous[0]
            except:
                isanonymous = None
            type = item.xpath('./td[6]/text()').extract()
            try:
                type = type[0]
            except:
                type = None
            alivetime = item.xpath('./td[7]/text()').extract()
            try:
                alivetime = alivetime[0]
            except:
                alivetime = None
            verifitime = item.xpath('./td[8]/text()').extract()
            try:
                verifitime = verifitime[0]
            except:
                verifitime = None
            print(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifitime)

            infos["country"] = country
            infos["ipaddress"] = ipaddress
            infos["port"] = port
            infos["serveraddr"] = serveraddr
            infos["isanonymous"] = isanonymous
            infos["alivetime"] = alivetime
            infos["verifitime"] = verifitime

            yield infos

