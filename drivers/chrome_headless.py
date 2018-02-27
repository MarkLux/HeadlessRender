# -*- coding:utf-8
from base_driver import BaseDriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from config.constant import PAGE_LOAD_TIMEOUT


class ChromeHeadlessDriver(BaseDriver):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument(
            "--user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
        self.options.add_argument('--disable-gpu')

        self.prefs = {'profile.managed_default_content_settings.images': 2}
        self.options.add_experimental_option('prefs', self.prefs)

        self.driver = webdriver.Chrome(chrome_options=self.options)
        # self.driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        # self.driver.set_script_timeout(SCRIPT_LOAD_TIMEOUT)

    def get_html(self, url):
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, PAGE_LOAD_TIMEOUT, 0.5).until(
                expected.presence_of_element_located((By.TAG_NAME, 'body')))
            return self.driver.page_source.encode('utf-8')
        except Exception as e:
            print 'exception:' + e.message

    def setting(self, settings={}):
        pass
