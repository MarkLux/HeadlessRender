# -*- coding:utf-8

'''
通用配置
'''

# 页面加载等待时长，秒
PAGE_LOAD_TIMEOUT = 3

# 异步脚本运行时长，秒
SCRIPT_LOAD_TIMEOUT = 1
'''
chrome headless运行配置
'''

CHROME_HEADLESS_EXE_PATH = ''

'''
phantomJS运行配置
'''

PHANTOM_JS_EXE_PATH = '/usr/local/bin/phantomjs'

'''
firefox geckodriver 配置
'''

FIREFOX_EXE_PATH = '/usr/local/Cellar/geckodriver/0.19.1/bin/geckodriver'

'''
实际使用dirver
'''

DRIVER = 'firefox'

'''
RPC服务配置
'''

RPC_HOST = 'localhost'
RPC_PORT = 8099
