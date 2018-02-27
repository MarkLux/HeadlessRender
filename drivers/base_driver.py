# -*- coding:utf-8

from abc import abstractmethod


class BaseDriver(object):
    @abstractmethod
    def get_html(self, url):
        pass

    @abstractmethod
    def setting(self, settings={}):
        pass
