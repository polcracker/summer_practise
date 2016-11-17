#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PyQt4 import QtGui, QtCore

from lib.export import CExport
from lib.tablemodel import CTableModel
from ui.ui_result import Ui_ResultFrom


class CResultForm(QtGui.QDialog, Ui_ResultFrom):
    def __init__(self, parent=None, body=[]):
        # initialize ui
        QtGui.QDialog.__init__(self, parent)
        Ui_ResultFrom.__init__(self)
        self.setupUi(self)
        # self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))

        self.parent = parent

        self.tblModel = CTableModel(self.tblResult, body)

        self.tblProxyModel = QtGui.QSortFilterProxyModel(self)
        self.tblProxyModel.setSourceModel(self.tblModel)

        self.tblResult.setModel(self.tblProxyModel)

        self.tblResult.verticalHeader().setVisible(True)

        # self.tblResult.setSortingEnabled(True)
        # self.tblResult.sortByColumn(0, QtCore.Qt.AscendingOrder)

        self.tblResult.resizeColumnsToContents()
        self.tblResult.autoFillBackground()
        self.tblResult.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblResult.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.tblResult.setAlternatingRowColors(True)

        for col in xrange(self.tblResult.model().columnCount()):
            if col in [0, 1, 2]:
                self.tblResult.horizontalHeader().resizeSection(col, 60)
                self.tblResult.horizontalHeader().setResizeMode(col, QtGui.QHeaderView.ResizeToContents)
            elif col == 3:
                self.tblResult.horizontalHeader().resizeSection(col, 500)
                self.tblResult.horizontalHeader().setResizeMode(col, QtGui.QHeaderView.Stretch)

        self.btnClose.clicked.connect(self.closing)
        self.btnRepeate.clicked.connect(self.repeat)
        self.btnSave.clicked.connect(self.save)

        self.tblResult.model().body = body

        self.status = 0

    def setTableBody(self, data):
        self.tblResult.model().body = data

    def closing(self):
        self.status = 0
        self.close()

    def repeat(self):
        self.status = 1
        self.close()

    def save(self):
        try:
            if CExport(content=[self.tblModel.header] + self.tblResult.model().body, parent=self).exposeFile():
                QtGui.QMessageBox.information(
                    self,
                    u'Выгрузка из реестра',
                    u'Выгрузка в файл успешно завершена!',
                    QtGui.QMessageBox.Ok
                )
        except Exception as e:
            QtGui.QMessageBox.warning(
                self,
                u'Выгрузка из реестра',
                u'Выгрузка произошла с ошибкой:\n%s' % e.msg if hasattr(e, 'msg') else e.message,
                QtGui.QMessageBox.Ok
            )


def main():
    app = QtGui.QApplication(sys.argv)
    win = CResultForm(body=
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
    )
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()
