# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_courses.ui'
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

class Ui_MainWindow_addCourses(object):
    def setupUi(self, MainWindow_addCourses):
        MainWindow_addCourses.setObjectName(_fromUtf8("MainWindow_addCourses"))
        MainWindow_addCourses.resize(963, 371)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow_addCourses.sizePolicy().hasHeightForWidth())
        MainWindow_addCourses.setSizePolicy(sizePolicy)
        MainWindow_addCourses.setStyleSheet(_fromUtf8("background-color: rgb(255, 166, 57);\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow_addCourses)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tv_courses = QtGui.QTableView(self.centralwidget)
        self.tv_courses.setGeometry(QtCore.QRect(10, 40, 941, 291))
        self.tv_courses.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tv_courses.setObjectName(_fromUtf8("tv_courses"))
        self.pb_addrow = QtGui.QPushButton(self.centralwidget)
        self.pb_addrow.setGeometry(QtCore.QRect(580, 340, 127, 23))
        self.pb_addrow.setObjectName(_fromUtf8("pb_addrow"))
        self.pb_close = QtGui.QPushButton(self.centralwidget)
        self.pb_close.setGeometry(QtCore.QRect(713, 340, 128, 23))
        self.pb_close.setObjectName(_fromUtf8("pb_close"))
        self.pb_save = QtGui.QPushButton(self.centralwidget)
        self.pb_save.setGeometry(QtCore.QRect(442, 340, 128, 23))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.pb_select = QtGui.QPushButton(self.centralwidget)
        self.pb_select.setGeometry(QtCore.QRect(300, 340, 131, 21))
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
        self.pb_retrieve = QtGui.QPushButton(self.centralwidget)
        self.pb_retrieve.setGeometry(QtCore.QRect(150, 340, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pb_retrieve.setFont(font)
        self.pb_retrieve.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_retrieve.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pb_retrieve.setObjectName(_fromUtf8("pb_retrieve"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 941, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Narkisim"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow_addCourses.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_addCourses)
        QtCore.QObject.connect(self.pb_close, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow_addCourses.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_addCourses)

    def retranslateUi(self, MainWindow_addCourses):
        MainWindow_addCourses.setWindowTitle(_translate("MainWindow_addCourses", "Add Courses", None))
        self.pb_addrow.setStyleSheet(_translate("MainWindow_addCourses", "background-color: rgb(255, 255, 255);", None))
        self.pb_addrow.setText(_translate("MainWindow_addCourses", "Add Course", None))
        self.pb_close.setStyleSheet(_translate("MainWindow_addCourses", "background-color: rgb(255, 255, 255);", None))
        self.pb_close.setText(_translate("MainWindow_addCourses", "Close", None))
        self.pb_save.setStyleSheet(_translate("MainWindow_addCourses", "background-color: rgb(255, 255, 255);", None))
        self.pb_save.setText(_translate("MainWindow_addCourses", "Save", None))
        self.pb_select.setText(_translate("MainWindow_addCourses", "Select Feedback Id [F1]", None))
        self.pb_retrieve.setText(_translate("MainWindow_addCourses", "Retrieve Rows", None))
        self.label.setText(_translate("MainWindow_addCourses", "We have a maximum of 6 feedback ids and 5 Other courses interested in. At least 5 feedback ids have to filled for every course. 6th feedback can be left blank. For other courses no such restrictions.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow_addCourses = QtGui.QMainWindow()
    ui = Ui_MainWindow_addCourses()
    ui.setupUi(MainWindow_addCourses)
    MainWindow_addCourses.show()
    sys.exit(app.exec_())

