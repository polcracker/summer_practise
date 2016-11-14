#!/usr/bin/env python
# -*- coding: utf8 -*-
import re
import urllib2

import sys
from PyQt4 import QtGui

from grab import Grab
from bs4 import BeautifulSoup

from ui.Ui_main import Ui_MainFrom
from lib.config import VERSION

# get region (by xparentId of subject)
REGION_URL = 'https://rosreestr.ru/wps/PA_FCCLPGUOReqService/ru.fccland.pgu.online.request?ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=%2FChildsRegionController&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&parentId={parent_id}'
# get city type (by xparentId of region)
CITY_TYPE_URL = 'https://rosreestr.ru/wps/PA_FCCLPGUOReqService/ru.fccland.pgu.online.request?ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=%2FChildsRegionTypesController&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&parentId={parent_id}'
# get city (by xparentId of region)
CITY_URL = 'https://rosreestr.ru/wps/PA_FCCLPGUOReqService/ru.fccland.pgu.online.request?ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=%2FChildsRegionController&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&parentId={parent_id}&settlement_type=set0&add_settlement_type=true'
# base url
BASE_URL = 'https://rosreestr.ru/wps/portal/online_request'


class CCmbParser(object):
    def __init__(self, url=BASE_URL):
        self.option_pattern = re.compile('\n*\s*<option value="(.*)">(.*)<\/option>\n*')
        self.url = url
        self.soup = BeautifulSoup(self.__get_html(self.url), "html.parser")

    @staticmethod
    def __get_html(url):
        return urllib2.urlopen(url).read()

    def __parse_cmb(self, cmb_name, isName=True):
        if isName:
            self.select_pattern = re.compile('(<select name="%s".*>(\n*\s*<option .*>.*<\/option>\n*)*)' % cmb_name)
        else:
            self.select_pattern = re.compile('(<select .* id="%s".*>(\n*\s*<option .*>.*<\/option>\n*)*)' % cmb_name)

        select_struct = re.findall(self.select_pattern, str(self.soup))
        result = re.findall(self.option_pattern, select_struct[0][0]) if select_struct else []
        return map(lambda x: {'id': x[0], 'name': x[1].decode('utf-8')}, result)

    def get_subjects(self):
        return self.__parse_cmb('subjectId', False)

    def get_regions(self):
        return self.__parse_cmb('rSubjectId', False)

    def get_street_type(self):
        return self.__parse_cmb('street_type', True)

    def get_city_types(self):
        return self.__parse_cmb('settlement_type', True)

    def get_cities(self):
        return self.__parse_cmb('settlement_id', True)


class CGrabProject(QtGui.QDialog, Ui_MainFrom):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        Ui_MainFrom.__init__(self)
        self.setupUi(self)

        self.grab = Grab()
        self.grab.go(BASE_URL)
        self.grab.doc.set_input('search_type', 'ADDRESS')

        cmbSubject = CCmbParser()
        cmbSubject.soup = self.grab.doc.body
        self.subjectsList = cmbSubject.get_subjects()
        self.fillComboBox(self.cmbSubject, self.subjectsList)

        self.btnSubmit.clicked.connect(self.f)

    @staticmethod
    def get_info(url):
        import pycurl
        import cStringIO

        buf = cStringIO.StringIO()

        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.perform()

        result = buf.getvalue()
        buf.close()
        return result

    @staticmethod
    def fillComboBox(cmb, values):
        map(lambda x: cmb.addItem(x['name']), values)

    def f(self):
        g = Grab(log_file='out.log')
        g.go(BASE_URL)

        c = CCmbParser()
        c.soup = g.doc.body
        g.doc.set_input('search_type', 'ADDRESS')
        c.soup = g.doc.body
        a = c.get_subjects()
        self.fillComboBox(self.cmbSubject, a)
        g.doc.set_input('subject_id', '130000000000')
        g.doc.set_input('region_id', '145286000000')
        g.doc.set_input('settlement_id', '145298578000')
        #g.doc.set_input('subject_id', '130000000000')
        #g.doc.set_input('124000000000', 'checked="true"')
        c.soup = g.doc.body
        b = c.get_regions()
        c1 = c.get_street_type()
        d = c.get_city_types()
        e = c.get_cities()
        # Ищем слово "Новости" на странице
        # print(u"На этой странице есть слово \"Новости\"? %s" % u'Да' if g.doc.text_search(u'Новости') else u'Нет')
        # выводим тайтл страницы
        print(u"Заголовок страницы: '%s'" % g.doc.select('//title').text())

        g.doc.set_input('search_type', 'ADDRESS')

        f = g.doc.submit()
        print 'zi'
        pass
        # получаем первую ссылку из запроса яндекса) Ссылку на годную статейку
        # print(u"Годная ссылочка на хабр про грабик: %s" % g.doc.select('//li[@class="serp-item"]//a').attr('href'))




def main():
    print u"[GrabProject] Текущая версия программы: %s" % VERSION
    app = QtGui.QApplication(sys.argv)
    win = CGrabProject()
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()
