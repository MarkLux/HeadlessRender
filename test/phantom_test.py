# -*- coding:utf-8
import time

# from adweb.djangosite.audit.inspect_const import log_init
from common.util import invalid_html, filter_toutiao_url
from drivers.phantom_js import PhantomJsDriver
# from ssad.common.db.session import config_ad_read_session, config_ad_write_session
# from adweb.djangosite.audit.ad_inspect_consumer import get_tetris_html
# from adweb.djangosite.adsite_common.common import get_read_ad

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
    with open(SAMPLE_DIR + file_name, 'w') as f:
        f.write(html)

'''
def init_conf():
    """
    初始化ad_data和redis访问
    """
    from adweb.common.deploy_conf import conf
    config_ad_read_session(conf)
    config_ad_write_session(conf)
    from ssad.common.notification.dals import init_notify
    init_notify(conf)
    log_init(conf, "ad_crawl_service")
'''

def test():
    # init_conf()
    start_time = time.time()
    handled = 0
    failed = 0
    data = read_csv('data.csv', [0, 1])
    driver = PhantomJsDriver()
    for datum in data:
        # ad = get_read_ad(int(datum[0]))
        # html = get_tetris_html(ad)
        if filter_toutiao_url(datum[1]):
            print 'filter toutiao url %s' % datum[1]
            continue
        if len(datum) < 2:
            continue
        handled += 1
        print 'crawling %s' % datum[1]
        html = driver.get_html(datum[1])
        if invalid_html(html, datum[1]):
            print '%s failed,url: %s' % (str(datum[0]), datum[1])
            failed += 1
        else:
            save_html(html, str(datum[0]))
    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time / handled

    print 'result:'
    print 'handled: %s, failed %s ' % (str(handled), str(failed))
    print 'total_time: %s, avg_time: %s' % (str(total_time), str(avg_time))


if __name__ == '__main__':
    test()
