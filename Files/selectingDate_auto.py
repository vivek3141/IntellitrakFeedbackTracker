# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectingDate.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(296, 273)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 166, 57);"))
        self.cal = QtGui.QCalendarWidget(Dialog)
        self.cal.setGeometry(QtCore.QRect(20, 20, 256, 161))
        self.cal.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 173);"))
        self.cal.setObjectName(_fromUtf8("cal"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(62, 200, 32, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lbl_date = QtGui.QLabel(Dialog)
        self.lbl_date.setGeometry(QtCore.QRect(125, 200, 121, 20))
        self.lbl_date.setText(_fromUtf8(""))
        self.lbl_date.setObjectName(_fromUtf8("lbl_date"))
        self.btn_ok = QtGui.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(164, 240, 91, 23))
        self.btn_ok.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_ok_2 = QtGui.QPushButton(Dialog)
        self.btn_ok_2.setGeometry(QtCore.QRect(50, 240, 91, 23))
        self.btn_ok_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_ok_2.setObjectName(_fromUtf8("btn_ok_2"))
        self.label_2.raise_()
        self.lbl_date.raise_()
        self.cal.raise_()
        self.btn_ok.raise_()
        self.btn_ok_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btn_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.btn_ok_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.cal, self.btn_ok_2)
        Dialog.setTabOrder(self.btn_ok_2, self.btn_ok)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Select Date", None))
        self.label_2.setText(_translate("Dialog", "DATE: ", None))
        self.btn_ok.setText(_translate("Dialog", "OK", None))
        self.btn_ok_2.setText(_translate("Dialog", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

