# -*- coding: utf-8 -*-
import scrapy
import re
from Fang.items import FangItem
from urllib import request

class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath('//div[@class="outCont"]//tr')
        province = None
        #解析省份
        for tr in trs:
            tds = tr.xpath(".//td[2]//text()").extract()
            if '\xa0' not in tds:
                province_td = tds[0]
                province = province_td
            else:
                province_td = province
            #海外不要
            if province == '其它':
                continue
            # print(province_td)

            #分别解析城市和城市链接
            citys = tr.xpath(".//td[3]/a")
            for city_a in citys:
                city = city_a.xpath("./text()").extract()[0]
                city_href = city_a.xpath("./@href").extract()[0]
                print(province_td,city,city_href)
                # 构建新房、二手房链接
                url_base = city_href.split('.')
                scheme = url_base[0]
                domain = url_base[1] + '.' + url_base[2]

                #北京特殊
                if 'bj' in scheme:
                    newhouse_url = 'https://newhouse.fang.com/house/s/'
                    esf_url = 'https://esf.fang.com/'
                else:
                    newhouse_url = scheme + '.' + 'newhouse' + '.' + domain + 'house/s/'
                    esf_url = scheme + '.' + 'esf' + '.' + domain
                print(newhouse_url,esf_url)

                yield scrapy.Request(url=newhouse_url,callback=self.parse_newhouse,meta={'info':(province_td,city)})
                yield scrapy.Request(url=esf_url,callback=self.parse_esf,meta={'info':(province_td,city)})

                break
            break



    def parse_newhouse(self,response):
        province,city = response.meta.get('info')
        lis = response.xpath("//div[@class='nl_con clearfix']/ul/li")
        for li in lis:
            name_mid = li.xpath('.//div[@class="nlcd_name"]/a/text()').extract()
            if name_mid != []:
                name = name_mid[0].strip()
            # print(name)

            price_mid = li.xpath('.//div[@class="nhouse_price"]//text()').extract()
            if price_mid != []:
                price = ''.join(price_mid)
            price = re.sub(r'广告|\s','',price)
            print(price)

            jushi_mid = li.xpath('.//div[@class="house_type clearfix"]/a/text()').extract()
            if jushi_mid != []:
                jushi = jushi_mid
            jushi = list(map(lambda x:re.sub(r'\s','',x),jushi))
            jushi = list(filter(lambda x:x.endswith('居'),jushi))
            # print(jushi)

            area_mid = li.xpath('.//div[@class="house_type clearfix"]/text()').extract()
            if area_mid != []:
                area = area_mid
            area = list(map(lambda x:re.sub(r'－|/|\s','',x),area))
            area = list(filter(lambda x:x.endswith('平米'),area))
            # print(area)

            address_mid =  li.xpath('.//div[@class="address"]/a/@title').extract()
            if address_mid != []:
                address = address_mid[0]
            # print(address)

            onsale_mid = li.xpath('.//div[@class="fangyuan"]/span/text()').extract()
            if onsale_mid != []:
                onsale = onsale_mid[0]
            # print(onsale)

            origin_mid = li.xpath('.//div[@class="nlcd_name"]/a/@href').extract()
            if origin_mid != []:
                origin = origin_mid[0]
            print(origin)
            # print(province,city,jushi,area,address,onsale,origin)
            item = FangItem(province=province,city=city,jushi=jushi,area=area,address=address,onsale=onsale,origin=origin)
            yield item

        next_url = response.xpath('//div[@class="page"]//a[@class="next"]/@href').get()
        next_url = request.urljoin(response.url,next_url)
        if next_url:
            yield scrapy.Request(url=next_url,callback=self.parse_newhouse,meta={'info':(province_td,city)})


    # def parse_esf(self,response):
    #     province,city = response.meta.get('info')
