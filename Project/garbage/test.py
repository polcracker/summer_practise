#!/usr/bin/env python
# -*- coding: utf8 -*-
from grab import Grab


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


def main1():
    g = Grab()
    g.go('http://yandex.ru')

    # Ищем слово "Новости" на странице
    print(u"На этой странице есть слово \"Новости\"? %s" % u'Да' if g.doc.text_search(u'Новости') else u'Нет')
    # выводим тайтл страницы
    print(u"Заголовок страницы: '%s'" % g.doc.select('//title').text())

    g.doc.set_input('text', 'grab python')
    g.doc.submit()
    # получаем первую ссылку из запроса яндекса) Ссылку на годную статейку
    print(u"Годная ссылочка на хабр про грабик: %s" % g.doc.select('//li[@class="serp-item"]//a').attr('href'))


def main():
    print 'Hello world!'
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select

    driver = webdriver.PhantomJS(executable_path='webdrivers/phantomjs.exe')
    # Chrome(executable_path='webdrivers/chromedriver.exe')
    # Resize the window to the screen width/height
    driver.get("https://rosreestr.ru/wps/portal/online_request")
    # assert "Python" in driver.title
    elem = driver.find_element_by_id('adress')
    elem.click()
    sel = Select(driver.find_element_by_xpath("//select[@name='subject_id']"))
    sel.select_by_value('145000000000')

    sel1 = Select(driver.find_element_by_xpath("//select[@name='region_id']"))
    sel1.select_by_value('145286000000')

    sel2 = Select(driver.find_element_by_xpath("//select[@name='settlement_id']"))
    sel2.select_by_value('145286596000')

    btn = driver.find_element_by_id('submit-button')
    driver.save_screenshot('screenshots/screen_after.png')
    btn.click()

    driver.save_screenshot('screenshots/screen_before.png')
    driver.close()


def main2():
    from splinter import Browser

    browser = Browser('chrome')
    browser.visit('http://google.com')
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    browser.find_by_name('btnG').click()

    if browser.is_text_present('splinter.readthedocs.io'):
        print "Yes, the official website was found!"
    else:
        print "No, it wasn't found... We need to improve our SEO techniques"

    browser.quit()


if __name__ == '__main__':
    main()