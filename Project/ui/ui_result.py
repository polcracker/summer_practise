# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ResultFrom(object):
    def setupUi(self, ResultFrom):
        ResultFrom.setObjectName(_fromUtf8("ResultFrom"))
        ResultFrom.setEnabled(True)
        ResultFrom.resize(940, 487)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResultFrom.sizePolicy().hasHeightForWidth())
        ResultFrom.setSizePolicy(sizePolicy)
        ResultFrom.setMinimumSize(QtCore.QSize(940, 487))
        ResultFrom.setMaximumSize(QtCore.QSize(940, 487))
        ResultFrom.setAutoFillBackground(True)
        self.grbMain = QtGui.QGroupBox(ResultFrom)
        self.grbMain.setGeometry(QtCore.QRect(10, 10, 921, 471))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grbMain.sizePolicy().hasHeightForWidth())
        self.grbMain.setSizePolicy(sizePolicy)
        self.grbMain.setMinimumSize(QtCore.QSize(921, 471))
        self.grbMain.setMaximumSize(QtCore.QSize(921, 471))
        self.grbMain.setTitle(_fromUtf8(""))
        self.grbMain.setObjectName(_fromUtf8("grbMain"))
        self.gridLayoutWidget = QtGui.QWidget(self.grbMain)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 901, 451))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tblResult = QtGui.QTableView(self.gridLayoutWidget)
        self.tblResult.setObjectName(_fromUtf8("tblResult"))
        self.gridLayout.addWidget(self.tblResult, 0, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.btnSave = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.gridLayout_5.addWidget(self.btnSave, 0, 0, 1, 1)
        self.btnRepeate = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnRepeate.setObjectName(_fromUtf8("btnRepeate"))
        self.gridLayout_5.addWidget(self.btnRepeate, 0, 1, 1, 1)
        self.btnClose = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.gridLayout_5.addWidget(self.btnClose, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.grbMain.raise_()

        self.retranslateUi(ResultFrom)
        QtCore.QMetaObject.connectSlotsByName(ResultFrom)

    def retranslateUi(self, ResultFrom):
        ResultFrom.setWindowTitle(_translate("ResultFrom", "[Результат] Справочная информация по объектам недвижимости", None))
        self.btnSave.setText(_translate("ResultFrom", "Сохранить", None))
        self.btnRepeate.setText(_translate("ResultFrom", "Повторить", None))
        self.btnClose.setText(_translate("ResultFrom", "Закрыть", None))

