# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_feedback.ui'
#
# Created: Tue Aug  2 15:09:44 2016
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
        Dialog.resize(576, 610)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 166, 57);"))
        self.tv_feedback = QtGui.QTableView(Dialog)
        self.tv_feedback.setGeometry(QtCore.QRect(10, 10, 551, 541))
        self.tv_feedback.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tv_feedback.setObjectName(_fromUtf8("tv_feedback"))
        self.pb_select = QtGui.QPushButton(Dialog)
        self.pb_select.setGeometry(QtCore.QRect(21, 569, 251, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pb_select.setFont(font)
        self.pb_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_select.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pb_select.setObjectName(_fromUtf8("pb_select"))
        self.pb_close = QtGui.QPushButton(Dialog)
        self.pb_close.setGeometry(QtCore.QRect(289, 569, 261, 23))
        self.pb_close.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pb_close.setObjectName(_fromUtf8("pb_close"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.pb_select, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Feedback questions", None))
        self.pb_select.setText(_translate("Dialog", "Select", None))
        self.pb_close.setText(_translate("Dialog", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

