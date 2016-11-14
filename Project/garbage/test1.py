#!/usr/bin/env python
# -*- coding: utf8 -*-
from pyvirtualdisplay import Display
from selenium import webdriver
# если хотим полностью скрыть дисплей то visible=0, иначе visible=1


display = Display(visible=0, size= (1024, 768))
display.start()
driver= webdriver.Chrome()
driver.get('http://www.qaclubkiev.com')
print 'The title of current page is: ', driver.title
driver.quit()
display.stop()