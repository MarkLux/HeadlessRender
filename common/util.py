# -*-coding:utf-8
import re
import logging
from urlparse import urljoin, urlparse

from bs4 import BeautifulSoup

from common.word_filter import FILTERS

CONTENT_MIN_LENGTH = 10


def invalid_html(html, url):
    if not html:
        print 'empty html'
        return True
    content, imgs = format_text(html, url)
    # 最终长度是有效中文内容长度
    content = sieve_content(content)
    # print content, imgs
    return len(content) < CONTENT_MIN_LENGTH and len(imgs) < 1


def format_text(html, url):
    html = re.sub(r"<!--.*-->", "", html, flags=re.UNICODE)
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.find_all('img')
    target_imgs = []
    for img in imgs:
        src = img.get('src', '')
        if src:
            if src.startswith('http'):
                target_imgs.append(src)
            else:
                try:
                    target_imgs.append(urljoin(url, src))
                except Exception as e:
                    logging.exception('append url failed. url: %s %s', url, e)
    # kill all script and style elements
    for script in soup(["script", "style", "img", 'head', 'title', '[document]']):
        script.extract()  # rip it out
    content = re.sub(r'</?\w+[^>]*>', '', soup.get_text())
    content = re.sub(r"\s+", "", content, flags=re.UNICODE)
    content = filter_content(content)
    return content, target_imgs


def filter_content(content):
    for i in FILTERS:
        content = content.replace(i, '')
    return content


def filter_toutiao_url(url):
    hostname = urlparse(url).hostname
    if hostname in (
            'ad.toutiao.com',
            'slide.toutiao.com',
            'www.chengzijianzhan.com',
            'chengzijianzhan.com',
            'toutiao.com',
            'www.toutiaopage.com',
            'toutiaopage.com'
    ):
        return True
    return False

def sieve_content(content):
    # 筛掉中文
    if not content:
        return ''
    p = re.compile("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%\-\"\']")
    content = p.sub("", content)
    return content