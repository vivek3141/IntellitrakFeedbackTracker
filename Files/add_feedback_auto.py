# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_feedback.ui'
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

class Ui_MainWindow_addfeed(object):
    def setupUi(self, MainWindow_addfeed):
        MainWindow_addfeed.setObjectName(_fromUtf8("MainWindow_addfeed"))
        MainWindow_addfeed.resize(619, 579)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow_addfeed.sizePolicy().hasHeightForWidth())
        MainWindow_addfeed.setSizePolicy(sizePolicy)
        MainWindow_addfeed.setStyleSheet(_fromUtf8("background-color: rgb(255, 166, 57);"))
        self.centralwidget = QtGui.QWidget(MainWindow_addfeed)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tv_feedback = QtGui.QTableView(self.centralwidget)
        self.tv_feedback.setGeometry(QtCore.QRect(10, 10, 601, 491))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tv_feedback.sizePolicy().hasHeightForWidth())
        self.tv_feedback.setSizePolicy(sizePolicy)
        self.tv_feedback.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tv_feedback.setObjectName(_fromUtf8("tv_feedback"))
        self.pb_save = QtGui.QPushButton(self.centralwidget)
        self.pb_save.setGeometry(QtCore.QRect(102, 521, 75, 23))
        self.pb_save.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.pb_addrow = QtGui.QPushButton(self.centralwidget)
        self.pb_addrow.setGeometry(QtCore.QRect(183, 521, 75, 23))
        self.pb_addrow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pb_addrow.setObjectName(_fromUtf8("pb_addrow"))
        self.pb_close = QtGui.QPushButton(self.centralwidget)
        self.pb_close.setGeometry(QtCore.QRect(264, 521, 75, 23))
        self.pb_close.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pb_close.setObjectName(_fromUtf8("pb_close"))
        self.pb_retrieve = QtGui.QPushButton(self.centralwidget)
        self.pb_retrieve.setGeometry(QtCore.QRect(21, 521, 75, 23))
        self.pb_retrieve.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pb_retrieve.setObjectName(_fromUtf8("pb_retrieve"))
        MainWindow_addfeed.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_addfeed)
        QtCore.QObject.connect(self.pb_close, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow_addfeed.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_addfeed)

    def retranslateUi(self, MainWindow_addfeed):
        MainWindow_addfeed.setWindowTitle(_translate("MainWindow_addfeed", "Feedback questions", None))
        self.pb_save.setText(_translate("MainWindow_addfeed", "Save", None))
        self.pb_addrow.setText(_translate("MainWindow_addfeed", "Add row", None))
        self.pb_close.setText(_translate("MainWindow_addfeed", "Close", None))
        self.pb_retrieve.setText(_translate("MainWindow_addfeed", "Retrieve", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow_addfeed = QtGui.QMainWindow()
    ui = Ui_MainWindow_addfeed()
    ui.setupUi(MainWindow_addfeed)
    MainWindow_addfeed.show()
    sys.exit(app.exec_())

