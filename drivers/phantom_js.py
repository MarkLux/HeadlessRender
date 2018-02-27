# -*- coding:utf-8

import signal
from base_driver import BaseDriver
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from config.constant import PHANTOM_JS_EXE_PATH, PAGE_LOAD_TIMEOUT, SCRIPT_LOAD_TIMEOUT


class PhantomJsDriver(BaseDriver):

    def __init__(self):
        self.service_args = []
        self.service_args.append('--load-images=no')  # 关闭图片加载
        self.service_args.append('--disk-cache=yes')  # 开启缓存
        self.service_args.append('--ignore-ssl-errors=true')  # 忽略https错误
        self.dcap = dict(DesiredCapabilities.PHANTOMJS)
        self.dcap["phantomjs.page.settings.userAgent"] = (
            'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4 NewsArticle/5.8.2')
        self.driver = webdriver.PhantomJS(PHANTOM_JS_EXE_PATH, desired_capabilities=self.dcap, service_args=self.service_args)
        self.driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        self.driver.set_script_timeout(SCRIPT_LOAD_TIMEOUT)

    def get_html(self, url):
        try:
            self.driver.get(url)
            return self.driver.page_source.encode('utf-8')
        except Exception as e:
            print e.message

    def setting(self, settings={}):
        pass

    def __del__(self):
        self.driver.service.process.send_signal(signal.SIGTERM)
        self.driver.quit()