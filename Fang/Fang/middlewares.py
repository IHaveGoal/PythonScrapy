# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


import random

class FangDownloaderMiddleware(object):


    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        USER_AGENT = [
            'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
            'Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)',
            'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))',
            'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)'
        ]
        user_agent = random.choice(USER_AGENT)
        request.headers['User-Agent'] = user_agent

