#!/usr/bin/env python
# -*- coding: utf8 -*-
from PyQt4 import QtCore


class CTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, body=[]):
        QtCore.QAbstractTableModel.__init__(self)
        self.parent = parent
        self.header = [u'Источник', u'Кадастровый номер', u'Условный номер', u'Адрес']
        self.body = body

    def rowCount(self, parent):
        return len(self.body)

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole and role != QtCore.Qt.EditRole:
            return QtCore.QVariant()
        value = ''
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self.body[row][col]
        return QtCore.QVariant(value)

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.header[section])
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.QVariant(QtCore.Qt.AlignCenter)
        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant("%s" % str(section + 1))
        return QtCore.QVariant()
