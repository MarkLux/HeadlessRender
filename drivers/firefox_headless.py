# -*- coding:utf-8
from base_driver import BaseDriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from config.constant import PAGE_LOAD_TIMEOUT, SCRIPT_LOAD_TIMEOUT, FIREFOX_EXE_PATH


class FirefoxHeadlessDriver(BaseDriver):
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.set_preference("permissions.default.stylesheet", 2)
        self.options.set_preference("permissions.default.image", 2)

        self.driver = webdriver.Firefox(firefox_options=self.options, executable_path=FIREFOX_EXE_PATH)
        self.driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        self.driver.set_script_timeout(SCRIPT_LOAD_TIMEOUT)

    def get_html(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            if isinstance(e, TimeoutException):
                print 'timeout: %s' % e.message
                return self.driver.page_source.encode('utf-8')
            else:
                print e.message
                return ''

        return self.driver.page_source.encode('utf-8')

    def setting(self, settings={}):
        pass
