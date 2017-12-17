import sys
from PyQt4 import QtSql, QtCore, QtGui, uic
from add_feedback_auto import *

class AddFeedback(QtGui.QMainWindow, Ui_MainWindow_addfeed):
     def __init__(self, parent=None):
          QtGui.QMainWindow.__init__(self, parent)
          self.setupUi(self)
          
          db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
          db.setDatabaseName("Feedback.db")
          db.open()
          self.loadTable()
          QtCore.QObject.connect(self.pb_retrieve,QtCore.SIGNAL('clicked()'),self.loadTable)
          QtCore.QObject.connect(self.pb_addrow,QtCore.SIGNAL('clicked()'),self.addRow)
          QtCore.QObject.connect(self.pb_save,QtCore.SIGNAL('clicked()'),self.save)

     def loadTable(self):
          self.model = QtSql.QSqlTableModel(self)
          self.model.setTable("feedback")
          self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
          self.tv_feedback.setModel(self.model)
          
          #self.tv_feedback.setColumnWidth(0,30)

          self.tv_feedback.resizeColumnsToContents()
          self.tv_feedback.setColumnWidth(1,400)
          
          self.model.select()
          self.model.setHeaderData(0,QtCore.Qt.Horizontal,"Id")
          self.model.setHeaderData(1,QtCore.Qt.Horizontal,"Text required for Feedback")
          
          
     def addRow(self):
          self.model.insertRows(self.model.rowCount(),1)

     def save(self):
          self.model.submitAll()
          self.model.select()

          QtGui.QMessageBox.information(self,"Message","Your changes have been saved")

if (__name__ == "__main__"):
     app = QtGui.QApplication(sys.argv)
     feed = AddFeedback(None)
     feed.show()
     feed.setFixedSize(feed.size())
     app.exec_()
