# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_courses.ui'
#
# Created: Thu Jul 28 20:53:06 2016
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

class Ui_MainWindow_queryCourses(object):
    def setupUi(self, MainWindow_queryCourses):
        MainWindow_queryCourses.setObjectName(_fromUtf8("MainWindow_queryCourses"))
        MainWindow_queryCourses.resize(1280, 375)
        MainWindow_queryCourses.setStyleSheet(_fromUtf8("background-color: rgb(255, 166, 57);"))
        self.centralwidget = QtGui.QWidget(MainWindow_queryCourses)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(580, 334, 261, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pb_close = QtGui.QPushButton(self.layoutWidget)
        self.pb_close.setObjectName(_fromUtf8("pb_close"))
        self.horizontalLayout.addWidget(self.pb_close)
        self.tv_courses = QtGui.QTableView(self.centralwidget)
        self.tv_courses.setGeometry(QtCore.QRect(10, 10, 1261, 321))
        self.tv_courses.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tv_courses.setObjectName(_fromUtf8("tv_courses"))
        MainWindow_queryCourses.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_queryCourses)
        QtCore.QObject.connect(self.pb_close, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow_queryCourses.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_queryCourses)

    def retranslateUi(self, MainWindow_queryCourses):
        MainWindow_queryCourses.setWindowTitle(_translate("MainWindow_queryCourses", "Query Courses", None))
        self.pb_close.setStyleSheet(_translate("MainWindow_queryCourses", "background-color: rgb(255, 255, 255);", None))
        self.pb_close.setText(_translate("MainWindow_queryCourses", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow_queryCourses = QtGui.QMainWindow()
    ui = Ui_MainWindow_queryCourses()
    ui.setupUi(MainWindow_queryCourses)
    MainWindow_queryCourses.show()
    sys.exit(app.exec_())

