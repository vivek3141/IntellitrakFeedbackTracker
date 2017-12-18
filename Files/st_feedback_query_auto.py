# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'st_feedback_query.ui'
#
# Created: Tue Aug  2 15:15:23 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1110, 512)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 166, 57);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 80, 1091, 371))
        self.tableView.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);"))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 241, 22))
        self.comboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1010, 20, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB Demi"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 10, 691, 61))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cbx_helpme = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.cbx_helpme.setObjectName(_fromUtf8("cbx_helpme"))
        self.verticalLayout.addWidget(self.cbx_helpme)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(301, 471, 291, 23))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(609, 471, 251, 23))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Modify Feedback", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "All", None))
        self.pushButton_5.setText(_translate("MainWindow", "Q [F10]", None))
        self.label.setText(_translate("MainWindow", "Course", None))
        self.cbx_helpme.setText(_translate("MainWindow", "Help Me with this window", None))
        self.label_2.setText(_translate("MainWindow", "First Select the row by clicking on the number at the left of the row. Next press F1 or Select to edit the Feedback in a new form.", None))
        self.label_3.setText(_translate("MainWindow", "Course Filter can be used to filter the rows in the below list by course names. Initially all courses are selected.Select the course and press F10", None))
        self.pushButton.setText(_translate("MainWindow", "Select [F1]", None))
        self.pushButton_4.setText(_translate("MainWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

