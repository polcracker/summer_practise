#!/usr/bin/env python
# -*- coding: utf8 -*-
from PyQt4 import QtGui


class CExport(object):
    def __init__(self, filename='exported_info', content=[], extension='.csv', separator=';', parent=None):
        self.filename = filename
        self.content = content
        self.extension = extension
        self.separator = separator
        self.parent = parent

    def makeExportBody(self, filename):
        import io
        with io.open(filename, 'w+', encoding='cp1251') as file:#, encoding='utf-8')
            for row in self.content:
                for element in row:
                    s = (element if type(element) != int else unicode(element)) + self.separator
                    file.write(s)
                file.write(u'\n')

    def exposeFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self.parent, u"Сохранить выгрузку как...", "export", "*.csv")
        if len(filename):
            self.makeExportBody(u'%s' % filename)
            return True
        return False
