#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from time import sleep

from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from lib.cmbfiller import CCmbFiller
from lib.config import VERSION, DEBUG, BASE_URL, CHROME_PATH, PHANTOMJS_PATH, SERVICE_LOG_PATH, \
    SERVICE_SCREENSHOT_PATH, SUBMIT_ATTEMPT, SLEEP_TIME, EMPTY_CMB_RECORD, RE_OBJCOUNT_PATTERN, RE_DATA_PATTERN
from lib.result import CResultForm
from ui.ui_main import Ui_MainFrom


class CGrabProject(QtGui.QDialog, Ui_MainFrom):
    def __init__(self):
        # initialize ui
        QtGui.QDialog.__init__(self)
        Ui_MainFrom.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))

        # select webdriver
        if DEBUG:
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            chrome_options.add_argument("--window-size=800,600")
            chrome_options.add_argument("--window-position=3000,0")
            self.driver = webdriver.Chrome(executable_path=CHROME_PATH, chrome_options=chrome_options)
        else:
            self.driver = webdriver.PhantomJS(executable_path=PHANTOMJS_PATH, service_log_path=SERVICE_LOG_PATH)
        # move to BASE_URL page
        self.driver.get(BASE_URL)

        # flag of disable QComboBox update
        self.disableChange = False

        # select option "Адрес"
        self.driver.find_element_by_id('adress').click()

        # initialize class for filling QComboBoxes by items from dynamic page
        self.cmbFiller = CCmbFiller(BASE_URL, soup=self.driver.page_source)

        # first initialize all QComboBoxes
        self.initAllComboBoxes()

        # create connections with some methods of ui elements
        self.btnSubmit.clicked.connect(self.submitForm)
        self.cmbSubject.currentIndexChanged.connect(self.subjectChanged)
        self.cmbRegion.currentIndexChanged.connect(self.regionChanged)
        self.cmbCity.currentIndexChanged.connect(self.cityChanged)
        self.cmbCityType.currentIndexChanged.connect(self.cityTypeChanged)
        self.cmbStreetType.currentIndexChanged.connect(self.streetTypeChanged)
        self.btnClear.clicked.connect(self.clearFields)

    def initAllComboBoxes(self):
        self.applyCmbChange('subject_id', '110000000000')

        self.applyCmbChange('subject_id', '101000000000')

        self.subjectsList = self.cmbFiller.getSubjects()
        self.fillComboBox(self.cmbSubject, self.subjectsList)

        self.subjectChanged()

        self.applyCmbChange('region_id', self.regionList[2]['id'])
        self.applyCmbChange('region_id', self.regionList[1]['id'])

    def subjectChanged(self):
        if not self.disableChange:
            self.regionList = self.cmbFiller.getRegions(self.subjectsList[self.cmbSubject.currentIndex()]['id'])
            self.fillComboBox(self.cmbRegion, self.regionList)
            # self.applyCmbChange('subject_id', self.subjectsList[self.cmbSubject.currentIndex()]['id'])

            self.regionChanged()

    def regionChanged(self):
        if not self.disableChange:
            self.cityTypeList = self.cmbFiller.getCityTypes(self.regionList[self.cmbRegion.currentIndex()]['id'])
            self.fillComboBox(self.cmbCityType, self.cityTypeList)
            # self.applyCmbChange('region_id', self.regionList[self.cmbRegion.currentIndex()]['id'])

            self.cityTypeChanged()

    def cityChanged(self):
        if not self.disableChange:
            pass
            # self.applyCmbChange('settlement_id', self.cityList[self.cmbCity.currentIndex()]['id'])

    def cityTypeChanged(self):
        if not self.disableChange:
            self.cityList = self.cmbFiller.getCities(
                self.regionList[self.cmbRegion.currentIndex()]['id'],
                self.cityTypeList[self.cmbCityType.currentIndex()]['id']
            )
            self.fillComboBox(self.cmbCity, self.cityList)
            # self.applyCmbChange('settlement_type', self.cityTypeList[self.cmbCityType.currentIndex()]['id'])

            self.streetTypeList = self.cmbFiller.getStreetType()
            self.fillComboBox(self.cmbStreetType, self.streetTypeList)
            self.streetTypeChanged()
            self.cityChanged()

    def streetTypeChanged(self):
        if not self.disableChange:
            pass
            # self.applyCmbChange('street_type', self.streetTypeList[self.cmbStreetType.currentIndex()]['id'])

    def fillComboBox(self, cmb, values):
        cmb.clear()
        self.disableChange = True
        map(lambda x: cmb.addItem(x['name']), values)
        self.disableChange = False

    def execWithSleep(self, func, name, value, time=SLEEP_TIME):
        attempt = SUBMIT_ATTEMPT
        while attempt:
            try:
                func(name, value)
                attempt = 0
                if attempt == 3:
                    sleep(time)
            except Exception as e:
                print '[GrabProject] execWithSleep error, try again. Attempt: %s | Message: "%s"' % (
                    attempt,
                    e.msg if hasattr(e, 'msg') else e.message
                )
                attempt -= 1

    def sendCmbValue(self, cmb, cmbValueList, cmbName, withSleep=True, defaultValue='-1'):
        if cmbValueList[cmb.currentIndex()]['id'] != EMPTY_CMB_RECORD['id']:
            value = cmbValueList[cmb.currentIndex()]['id']
        else:
            value = defaultValue

        self.execWithSleep(
            self.applyCmbChange,
            cmbName,
            value,
            SLEEP_TIME if withSleep else 0
        )

    def applyCmbChange(self, cmb, value):
        Select(self.driver.find_element_by_xpath("//select[@name='%s']" % cmb)).select_by_value(value)

    def applyEdtChange(self, edt, value):
        i = str(value.toUtf8())
        i = unicode(i.decode("utf8"))
        element = self.driver.find_element_by_css_selector("INPUT[name=\"%s\"]" % edt)
        element.clear()
        element.send_keys(i)
        # self.driver.find_element_by_name(edt).send_keys(value)

    def submitForm(self):
        try:
            submit = self.driver.find_element_by_id('submit-button')

            attempt = SUBMIT_ATTEMPT
            self.loadProgress.setValue(10)
            while attempt:
                try:
                    # send changes to form
                    self.sendCmbValue(self.cmbSubject, self.subjectsList, 'subject_id')
                    self.sendCmbValue(self.cmbRegion, self.regionList, 'region_id')
                    self.sendCmbValue(self.cmbCityType, self.cityTypeList, 'settlement_type')
                    self.sendCmbValue(self.cmbCity, self.cityList, 'settlement_id')
                    self.sendCmbValue(
                        self.cmbStreetType,
                        self.streetTypeList,
                        'street_type',
                        withSleep=False,
                        defaultValue='str0'
                    )

                    self.applyEdtChange('street', self.edtStreet.text())
                    self.applyEdtChange('house', self.edtHouseNumber.text())
                    self.applyEdtChange('building', self.edtBuilding.text())
                    self.applyEdtChange('structure', self.edtStructure.text())
                    self.applyEdtChange('apartment', self.edtApartment.text())

                    attempt = 0
                except Exception as e:
                    print '[GrabProject] Submit error, try again. Attempt: %s | Message: "%s"' % (
                        attempt,
                        e.msg if hasattr(e, 'msg') else e.message
                    )
                    if not DEBUG:
                        self.driver.save_screenshot(SERVICE_SCREENSHOT_PATH + 'screen_error_load.png')
                    attempt -= 1

            if not DEBUG:
                self.driver.save_screenshot(SERVICE_SCREENSHOT_PATH + 'screen_after.png')
            submit.click()

            self.parseInfo()
        except Exception as e:
            print '[GrabProject] Submit fatal error: "%s"' % (
                e.msg if hasattr(e, 'msg') else e.message
            )
            if not DEBUG:
                self.driver.save_screenshot(SERVICE_SCREENSHOT_PATH + 'screen_fatal_error.png')
        finally:
            self.driver.find_element_by_id('online_request_search_crit_img').click()

    def parseInfo(self):
        import re
        sleep(SLEEP_TIME)

        parse = re.findall(RE_OBJCOUNT_PATTERN, self.driver.page_source)
        if parse:
            objCount = int(parse[0])
            self.loadProgress.setMaximum(objCount)
            data = re.findall(RE_DATA_PATTERN, self.driver.page_source)
            if objCount > 20:
                self.driver.find_element_by_id('PC_7_015A1H40IOMCC0ACRHALLM30A1000000_js_es0').click()

            self.loadProgress.setValue(len(data))

            while objCount > len(data):
                data += re.findall(RE_DATA_PATTERN, self.driver.page_source)
                self.loadProgress.setValue(len(data))
                if not DEBUG:
                    self.driver.save_screenshot(SERVICE_SCREENSHOT_PATH + 'screen_parse_datalen%s.png' % len(data))
                d = self.driver.find_element_by_id('PC_7_015A1H40IOMCC0ACRHALLM30A1000000_js_es2')
                d.click()

            dlg = CResultForm(None, data)
            dlg.setTableBody(data)
            dlg.exec_()
            self.loadProgress.setValue(0)
            if dlg.status == 0:
                self.close()
        else:
            self.loadProgress.setValue(0)
            QtGui.QMessageBox.warning(
                self,
                u'Формирование запроса',
                u'По текущему запросу ничего не найдено. Проверьте введенные данные.',
                QtGui.QMessageBox.Ok
            )

    def clearFields(self):
        self.edtStructure.clear()
        self.edtBuilding.clear()
        self.edtApartment.clear()
        self.edtHouseNumber.clear()
        self.edtStreet.clear()

        self.cmbSubject.setCurrentIndex(0)
        self.cmbRegion.setCurrentIndex(0)
        self.cmbCityType.setCurrentIndex(0)
        self.cmbCity.setCurrentIndex(0)

        self.loadProgress.setValue(0)


def main():
    try:
        print u"[GrabProject] Current programm version: %s" % VERSION

        QtGui.qApp = QtGui.QApplication(sys.argv)
        win = CGrabProject()
        win.show()
        QtGui.qApp.exec_()
    except Exception as e:
        QtGui.QMessageBox.warning(
            None,
            u'Предупреждение',
            u'Непредвиденная ошибка:\n%s' % e.msg if hasattr(e, 'msg') else e.message,
            QtGui.QMessageBox.Ok
        )


if __name__ == '__main__':
    main()
