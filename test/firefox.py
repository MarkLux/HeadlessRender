import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected



options = Options()
options.add_argument("--headless")
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("permissions.default.stylesheet", 2)
firefox_profile.set_preference("permissions.default.image", 2)
path = '/usr/local/Cellar/geckodriver/0.19.1/bin/geckodriver'
driver = webdriver.Firefox(firefox_options=options, executable_path=path)
print("Firefox Headless Browser Invoked")
start = time.time()
driver.set_script_timeout(2)
driver.set_page_load_timeout(2)
try:
    driver.get('http://subad1.richclick.cn/web/29-69-30/index.html')
except Exception as e:
    print e
print driver.page_source
end = time.time()
print 'time used: %s s' % str(end - start)
try:
    WebDriverWait(driver, 2).until(expected.presence_of_element_located((By.TAG_NAME, 'body')))
    print driver.find_element_by_tag_name('body').text
except Exception:
    driver.execute_script('window.stop()')
driver.quit()

'''
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument(
    "--user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
options.add_argument('--disable-gpu')

prefs = {'profile.managed_default_content_settings.images': 2}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)
print 'Headless chrome launched'
start_time = time.time()
driver.get('http://subad1.richclick.cn/web/29-69-30/index.html')
end_time = time.time()
print 'time used: %s' % str(end_time - start_time)
try:
    WebDriverWait(driver, 2).until(expected.presence_of_element_located((By.TAG_NAME, 'body')))
    print driver.find_element_by_tag_name('body').text
except Exception:
    driver.execute_script('window.stop()')
driver.quit()
'''