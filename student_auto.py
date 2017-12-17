# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created: Thu Aug  4 13:44:04 2016
#      by: PyQt4 UI code generator 4.11.3
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
        Dialog.resize(450, 386)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 166, 57);"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 350, 181, 23))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 350, 171, 23))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 431, 281))
        self.tableView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.lne_fname = QtGui.QLineEdit(Dialog)
        self.lne_fname.setGeometry(QtCore.QRect(10, 20, 231, 20))
        self.lne_fname.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_fname.setText(_fromUtf8(""))
        self.lne_fname.setObjectName(_fromUtf8("lne_fname"))
        self.btn_query = QtGui.QPushButton(Dialog)
        self.btn_query.setEnabled(True)
        self.btn_query.setGeometry(QtCore.QRect(260, 20, 75, 23))
        self.btn_query.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_query.setObjectName(_fromUtf8("btn_query"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lne_fname, self.btn_query)
        Dialog.setTabOrder(self.btn_query, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)
        Dialog.setTabOrder(self.pushButton_2, self.tableView)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Select Student", None))
        self.pushButton.setText(_translate("Dialog", "Select [F1]", None))
        self.pushButton_2.setText(_translate("Dialog", "Close", None))
        self.btn_query.setText(_translate("Dialog", "Query [F10]", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

