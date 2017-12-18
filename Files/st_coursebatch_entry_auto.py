# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'st_coursebatch_entry.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(548, 378)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 166, 57);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 511, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB Demi"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.cb_course = QtGui.QComboBox(self.centralwidget)
        self.cb_course.setGeometry(QtCore.QRect(20, 60, 511, 22))
        self.cb_course.setStyleSheet(_fromUtf8("\n"
"\n"
"background-color: rgb(255, 255, 255);"))
        self.cb_course.setObjectName(_fromUtf8("cb_course"))
        self.cb_course.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 121, 21))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Berlin Sans FB Demi\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 121, 21))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Berlin Sans FB Demi\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 121, 21))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Berlin Sans FB Demi\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 121, 21))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Berlin Sans FB Demi\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lne_date = QtGui.QLineEdit(self.centralwidget)
        self.lne_date.setGeometry(QtCore.QRect(140, 100, 121, 20))
        self.lne_date.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_date.setReadOnly(True)
        self.lne_date.setObjectName(_fromUtf8("lne_date"))
        self.lne_time = QtGui.QLineEdit(self.centralwidget)
        self.lne_time.setGeometry(QtCore.QRect(70, 220, 101, 20))
        self.lne_time.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_time.setObjectName(_fromUtf8("lne_time"))
        self.lne_instructor = QtGui.QLineEdit(self.centralwidget)
        self.lne_instructor.setGeometry(QtCore.QRect(100, 140, 191, 20))
        self.lne_instructor.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_instructor.setObjectName(_fromUtf8("lne_instructor"))
        self.btn_date = QtGui.QPushButton(self.centralwidget)
        self.btn_date.setGeometry(QtCore.QRect(270, 100, 21, 23))
        self.btn_date.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_date.setObjectName(_fromUtf8("btn_date"))
        self.btn_save = QtGui.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(120, 310, 91, 23))
        self.btn_save.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.btn_selectstudent = QtGui.QPushButton(self.centralwidget)
        self.btn_selectstudent.setGeometry(QtCore.QRect(430, 100, 101, 23))
        self.btn_selectstudent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_selectstudent.setObjectName(_fromUtf8("btn_selectstudent"))
        self.btn_cancel = QtGui.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(340, 310, 91, 23))
        self.btn_cancel.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lw_students = QtGui.QListWidget(self.centralwidget)
        self.lw_students.setGeometry(QtCore.QRect(300, 130, 231, 161))
        self.lw_students.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lw_students.setObjectName(_fromUtf8("lw_students"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 291, 21))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Berlin Sans FB Demi\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.btn_del = QtGui.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(230, 310, 91, 23))
        self.btn_del.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_del.setObjectName(_fromUtf8("btn_del"))
        self.lbl_morn = QtGui.QLabel(self.centralwidget)
        self.lbl_morn.setEnabled(False)
        self.lbl_morn.setGeometry(QtCore.QRect(200, 220, 81, 21))
        self.lbl_morn.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);\n"
"font: 75 12pt \"Berlin Sans FB Demi\";"))
        self.lbl_morn.setObjectName(_fromUtf8("lbl_morn"))
        self.cb_day = QtGui.QComboBox(self.centralwidget)
        self.cb_day.setGeometry(QtCore.QRect(70, 180, 221, 22))
        self.cb_day.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.cb_day.setEditable(True)
        self.cb_day.setObjectName(_fromUtf8("cb_day"))
        self.cb_day.addItem(_fromUtf8(""))
        self.cb_day.setItemText(0, _fromUtf8(""))
        self.cb_day.addItem(_fromUtf8(""))
        self.cb_day.addItem(_fromUtf8(""))
        self.cb_day.addItem(_fromUtf8(""))
        self.cb_day.addItem(_fromUtf8(""))
        self.cb_day.addItem(_fromUtf8(""))
        self.cb_day.addItem(_fromUtf8(""))
        self.cb_day.addItem(_fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 548, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Create Batch", None))
        self.label.setText(_translate("MainWindow", "Create Batch", None))
        self.cb_course.setItemText(0, _translate("MainWindow", "Courses", None))
        self.label_2.setText(_translate("MainWindow", "Batch start date:", None))
        self.label_3.setText(_translate("MainWindow", "Instructor:", None))
        self.label_4.setText(_translate("MainWindow", "Day:", None))
        self.label_5.setText(_translate("MainWindow", "Time:", None))
        self.btn_date.setText(_translate("MainWindow", "...", None))
        self.btn_save.setText(_translate("MainWindow", "Save", None))
        self.btn_selectstudent.setText(_translate("MainWindow", "Select students [F1]", None))
        self.btn_cancel.setText(_translate("MainWindow", "Close", None))
        self.label_6.setText(_translate("MainWindow", "Please enter desired time in 24-hour clock format", None))
        self.btn_del.setText(_translate("MainWindow", "Delete", None))
        self.lbl_morn.setText(_translate("MainWindow", "MORNING", None))
        self.cb_day.setItemText(1, _translate("MainWindow", "Monday", None))
        self.cb_day.setItemText(2, _translate("MainWindow", "Tuesday", None))
        self.cb_day.setItemText(3, _translate("MainWindow", "Wednesday", None))
        self.cb_day.setItemText(4, _translate("MainWindow", "Thursday", None))
        self.cb_day.setItemText(5, _translate("MainWindow", "Friday", None))
        self.cb_day.setItemText(6, _translate("MainWindow", "Saturday", None))
        self.cb_day.setItemText(7, _translate("MainWindow", "Sunday", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

