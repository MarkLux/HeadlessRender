# coding:utf-8
import time

from selenium.webdriver.support.wait import WebDriverWait

from common.util import invalid_html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from drivers.chrome_headless import ChromeHeadlessDriver
from drivers.phantom_js import PhantomJsDriver

url = 'http://subad1.richclick.cn/web/29-69-30/index.html'


def chrome_test():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    prefs = {'profile.managed_default_content_settings.images': 2}
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(chrome_options=options)
    driver.set_page_load_timeout(5)
    driver.set_script_timeout(5)
    try:
        driver.get('http://subad1.richclick.cn/web/29-69-30/index.html')
    except Exception:
        driver.execute_script('window.stop()')

    print driver.page_source.encode('utf-8')  # raise TimeoutException this line.

    locator = (By.TAG_NAME, 'body')

    print 'not async'

    try:
        WebDriverWait(driver, 5, 0.5).until(expected.presence_of_element_located(locator), 'can not find element body')
        print driver.find_element_by_tag_name('body').text
    except TimeoutException:
        print 'timeout'
        driver.execute_script('window.stop()')


def phantom_js_test():
    phantom_driver = PhantomJsDriver()
    html = phantom_driver.get_html(url)
    print html
    if invalid_html(html, url):
        print 'invalid_html %s' % url

def firefox_test():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(executable_path='/Applications/Firefox.app/Contents/MacOS/firefox-bin', firefox_options=options)
    print "Firefox Headless Browser Invoked"
    wait = WebDriverWait(driver, timeout=10)
    driver.get('http://www.google.com')
    try:
        wait.until(expected.visibility_of_element_located((By.TAG_NAME, 'body')))
    except TimeoutException:
        driver.execute_script('window.stop()')

    print driver.page_source
    driver.quit()

if __name__ == '__main__':
    # start_time = time.time()
    # chrome_test()
    # chrome_endtime = time.time()
    # phantom_js_test()
    phantom_endtime = time.time()
    firefox_test()
    firefox_endtime = time.time()

    # print 'chrome headless: %s s' % str(chrome_endtime - start_time)
    # print 'phantom js: %s s' % str(phantom_endtime - chrome_endtime)
    print 'firefox: %s s' % str(firefox_endtime - phantom_endtime)

