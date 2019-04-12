from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger

class SeleniumMidd():
    def __init__(self,timeout=None,service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.brower = webdriver.Firefox()
        self.brower.set_window_size(1400,700)
        self.brower.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.brower,self.timeout)

    def __del__(self):
        self.brower.close()

    def process_request(self,request,spider):
        self.logger.debug('FireFox is Starting')
        page = request.meta.get('page',1)
        try:
            self.brower.get(request.url)
            js = ''
            if page > 1:
                submit = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
                submit.click()

            self.wait.until()
            self.wait.until()
            return HtmlResponse(url=request.url, body=self.brower.page_source, request=request,
                                encoding='utf-8',status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url,status=500,request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))
