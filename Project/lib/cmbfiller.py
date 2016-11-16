#!/usr/bin/env python
# -*- coding: utf8 -*-
from StringIO import StringIO
import re
import urllib2
# from bs4 import BeautifulSoup
import pycurl

from lib.config import BASE_URL, CITY_TYPE_URL, REGION_URL, CITY_BY_TYPE_URL, EMPTY_CMB_RECORD


# FIXME: исправить ситуацию с разделенным парсингом.
class CCmbFiller(object):
    def __init__(self, url=BASE_URL, soup=None):
        # self.option_pattern = re.compile('\n*\s*<option value="(.*)">(.*)<\/option>\n*')
        self.url = url
        # if not soup:
            # self.soup = BeautifulSoup(self.__getHtml(self.url), "html.parser")
        # else:
        self.soup = soup

    @staticmethod
    def __getHtml(url):
        return urllib2.urlopen(url).read()

    def __parseCmb(self, cmb_name, isName=True, insertEmpty=False):
        if isName:
            self.select_pattern = re.compile('(<select name="%s".*>(\n*\s*<option .*>.*<\/option>\n*)*)' % cmb_name)
        else:
            self.select_pattern = re.compile('(<select .* id="%s".*>(\n*\s*<option .*>.*<\/option>\n*)*)' % cmb_name)

        select_struct = re.findall(self.select_pattern, self.soup)
        finded = re.findall(self.option_pattern, select_struct[0][0]) if select_struct else []

        result = map(lambda x: {'id': x[0], 'name': x[1]}, finded)
        if insertEmpty:
            result.insert(0, EMPTY_CMB_RECORD)

        return result

    @staticmethod
    def __getInfo(url):
        buf = StringIO()

        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.perform()

        result = buf.getvalue()
        buf.close()
        return result

    def __getResponse(self, url, id, insertEmpty=False):
        text = self.__getInfo(url.replace('{parent_id}', id))

        id = re.compile('(.*);')
        name = re.compile(';(.*)\n*')

        id_list = re.findall(id, text)
        name_list = re.findall(name, text)

        result = map(lambda x, y: {'id': x, 'name': y.decode('utf-8')}, id_list, name_list)
        if insertEmpty:
            result.insert(0, EMPTY_CMB_RECORD)
        return result

    def getSubjects(self, insertEmpty=False):
        self.option_pattern = re.compile('\n*\s*<option value="(.*)">(.*)<\/option>\n*')
        return self.__parseCmb('subjectId', False, insertEmpty)

    def getRegions(self, id=None, insertEmpty=True):
        # return self.__parseCmb('regionId', False)
        return self.__getResponse(REGION_URL, id, insertEmpty)

    def getStreetType(self, insertEmpty=True):
        self.option_pattern = re.compile('\n*\s*<option value="(str\d*)">(.*)<\/option>\n*')
        return self.__parseCmb('street_type', True, insertEmpty)

    def getCityTypes(self, id=None, insertEmpty=True):
        return self.__getResponse(CITY_TYPE_URL, id, insertEmpty)
        # return self.__parseCmb('settlement_type', True)

    def getCities(self, id=None, type=None, insertEmpty=True):
        #if type:
        return self.__getResponse(CITY_BY_TYPE_URL.replace('{type_id}', type), id, insertEmpty)
