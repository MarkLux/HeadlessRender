# -*- coding:utf-8
# import threading
import time

from common.util import invalid_html, filter_toutiao_url
from drivers.chrome_headless import ChromeHeadlessDriver
from drivers.firefox_headless import FirefoxHeadlessDriver
from selenium.common.exceptions import TimeoutException
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# from multiprocessing.pool import ThreadPool

# _pool = ThreadPool(4)

HANLDE_COUNT = 0
# handle_lock = threading.Lock()
FAILED_COUNT = 0
# failed_lock = threading.Lock()
TIMEOUT_COUNT = 0
# timeout_lock = threading.Lock()
TOTAL_TIME_USED = 0
# total_time_lock = threading.Lock()

SAMPLE_DIR = '../samples/'


def read_csv(file_name, col_num=[0]):
    data = []
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            cell = []
            csv = line.split(',')
            for col in col_num:
                if col >= len(csv):
                    continue
                cell.append(str(csv[col]))
            data.append(cell)
    return data


def save_html(html, file_name):
    # 修改编码
    with open(SAMPLE_DIR + file_name, 'w') as f:
        f.write(html)


def test():
    # init_conf()
    data = read_csv('data.csv', [0, 1])
    # driver = ChromeHeadlessDriver()
    driver = FirefoxHeadlessDriver()

    def render(ad_id, url):
        if filter_toutiao_url(url):
            # print 'filter toutiao url %s' % url
            return
        global HANLDE_COUNT
        # handle_lock.acquire()
        HANLDE_COUNT += 1
        # handle_lock.release()
        start_time = time.time()
        print 'crawling %s: %s' % (str(HANLDE_COUNT), url)
        try:
            html = driver.get_html(url)
        except Exception as e:
            print e.message
            html = ''

        if invalid_html(html, url):
            print '%s failed' % str(ad_id)
            global FAILED_COUNT
            # failed_lock.acquire()
            FAILED_COUNT += 1
            # failed_lock.release()
            return
        if html:
            end_time = time.time()
            time_used = end_time - start_time
            global TOTAL_TIME_USED
            # total_time_lock.acquire()
            TOTAL_TIME_USED += time_used
            print 'total failed: %s, avg time: %s' % (str(FAILED_COUNT), str(TOTAL_TIME_USED / HANLDE_COUNT))
            # total_time_lock.release()
            print 'time used: %s s' % str(time_used)
            save_html(html, ad_id)
        return

    for datum in data:
        if len(datum) < 2:
            continue
        # _pool.apply(render, args=(datum[0], datum[1]))
        render(datum[0], datum[1])

    avg_time = TOTAL_TIME_USED / HANLDE_COUNT

    print 'result:'
    print 'handled: %s, failed: %s, timeout: %s' % (str(HANLDE_COUNT), str(FAILED_COUNT), str(TIMEOUT_COUNT))
    print 'total_time: %s, avg_time: %s' % (str(TOTAL_TIME_USED), str(avg_time))


if __name__ == '__main__':
    test()
