#!/usr/bin/env python
# -*- coding: utf8 -*-
VERSION = 'v0.6.1'

# get region (by xparentId of subject)
REGION_URL = 'https://rosreestr.ru/wps/PA_FCCLPGUOReqService/ru.fccland.pgu.online.request?ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=%2FChildsRegionController&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&parentId={parent_id}'
# get city type (by xparentId of region)
CITY_TYPE_URL = 'https://rosreestr.ru/wps/PA_FCCLPGUOReqService/ru.fccland.pgu.online.request?ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=%2FChildsRegionTypesController&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&parentId={parent_id}'
# get city (by xparentId of region)
# CITY_URL = 'https://rosreestr.ru/wps/PA_FCCLPGUOReqService/ru.fccland.pgu.online.request?ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=%2FChildsRegionController&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&parentId={parent_id}&settlement_type=set0&add_settlement_type=true'
# get city (by xparentId of region and settlement_type)
CITY_BY_TYPE_URL = 'https://rosreestr.ru/wps/PA_FCCLPGUOReqService/ru.fccland.pgu.online.request?ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=%2FChildsRegionController&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&parentId={parent_id}&settlement_type={type_id}&add_settlement_type=true'
# base url
BASE_URL = 'https://rosreestr.ru/wps/portal/online_request'

# Debug-mode
DEBUG = False
# Path of webdriver
PHANTOMJS_PATH = 'webdrivers/phantomjs.exe'
CHROME_PATH = 'webdrivers/chromedriver.exe'
# Path of log
SERVICE_LOG_PATH = 'log/webdriver.log'
SERVICE_SCREENSHOT_PATH = 'log/screenshots/'
# Submit attempt (when have problem)
SUBMIT_ATTEMPT = 10
# Sleep for wait between form comboboxes
SLEEP_TIME = 0.5
# Empty record
EMPTY_CMB_RECORD = {'id': 'empty', 'name': u'- не выбрано -'}

if DEBUG:
    RE_OBJCOUNT_PATTERN = '<td .*id="PC_7_015A1H40IOMCC0ACRHALLM30A1000000_pg_stats">\W+<nobr>.*\s*\:.(\d+)'
else:
    RE_OBJCOUNT_PATTERN = '<td .*id="PC_7_015A1H40IOMCC0ACRHALLM30A1000000_pg_stats">\W+<nobr>.*\s*\:&nbsp;(\d+)'

RE_DATA_PATTERN = '<td class="td" align="center">\n*\s*(.*)\n*\s*<\/td>\W*.*\W*<nobr>(.*)<\/nobr>\W*.*\W*<td class="td">(.*)\W*<\/td>.*\W*.*\W*<a .*;object_data_id=.*>\n*\s*(.*)\W*<\/a>'
