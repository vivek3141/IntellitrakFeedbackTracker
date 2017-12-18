# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fee_infoentry.ui'
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
        MainWindow.resize(415, 355)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 166, 57);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, -20, 651, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB Demi"))
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_select = QtGui.QPushButton(self.centralwidget)
        self.btn_select.setGeometry(QtCore.QRect(20, 100, 121, 21))
        self.btn_select.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_select.setObjectName(_fromUtf8("btn_select"))
        self.lne_fname = QtGui.QLineEdit(self.centralwidget)
        self.lne_fname.setGeometry(QtCore.QRect(150, 100, 211, 20))
        self.lne_fname.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_fname.setText(_fromUtf8(""))
        self.lne_fname.setReadOnly(True)
        self.lne_fname.setObjectName(_fromUtf8("lne_fname"))
        self.btn_selectb = QtGui.QPushButton(self.centralwidget)
        self.btn_selectb.setGeometry(QtCore.QRect(20, 70, 121, 21))
        self.btn_selectb.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_selectb.setObjectName(_fromUtf8("btn_selectb"))
        self.lne_adue = QtGui.QLineEdit(self.centralwidget)
        self.lne_adue.setGeometry(QtCore.QRect(150, 140, 211, 20))
        self.lne_adue.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_adue.setObjectName(_fromUtf8("lne_adue"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB Demi"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 121, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB Demi"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lne_apaid = QtGui.QLineEdit(self.centralwidget)
        self.lne_apaid.setGeometry(QtCore.QRect(150, 170, 211, 20))
        self.lne_apaid.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_apaid.setObjectName(_fromUtf8("lne_apaid"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 121, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB Demi"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lne_comments = QtGui.QTextEdit(self.centralwidget)
        self.lne_comments.setGeometry(QtCore.QRect(150, 210, 211, 51))
        self.lne_comments.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_comments.setObjectName(_fromUtf8("lne_comments"))
        self.btn_select_3 = QtGui.QPushButton(self.centralwidget)
        self.btn_select_3.setGeometry(QtCore.QRect(280, 290, 121, 21))
        self.btn_select_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_select_3.setObjectName(_fromUtf8("btn_select_3"))
        self.btn_clear = QtGui.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(150, 290, 121, 21))
        self.btn_clear.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_clear.setObjectName(_fromUtf8("btn_clear"))
        self.btn_ok = QtGui.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(20, 290, 121, 21))
        self.btn_ok.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.lne_bname = QtGui.QLineEdit(self.centralwidget)
        self.lne_bname.setGeometry(QtCore.QRect(150, 70, 211, 20))
        self.lne_bname.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lne_bname.setText(_fromUtf8(""))
        self.lne_bname.setReadOnly(True)
        self.lne_bname.setObjectName(_fromUtf8("lne_bname"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_select_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Fee Information", None))
        self.label.setText(_translate("MainWindow", "Fee Information Entry", None))
        self.btn_select.setText(_translate("MainWindow", "Select Student [F1]", None))
        self.btn_selectb.setText(_translate("MainWindow", "Select Batch [F2]", None))
        self.label_3.setText(_translate("MainWindow", "Amount Due:", None))
        self.label_4.setText(_translate("MainWindow", "Amount Paid:", None))
        self.label_5.setText(_translate("MainWindow", "Comments:", None))
        self.lne_comments.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.btn_select_3.setText(_translate("MainWindow", "Close", None))
        self.btn_clear.setText(_translate("MainWindow", "Clear All", None))
        self.btn_ok.setText(_translate("MainWindow", "Save", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

