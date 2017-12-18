import sys
from PyQt4 import QtCore, QtGui, uic, QtSql
import sqlite3
 
from batch_auto import * 
  
class Batch(QtGui.QDialog):
    def __init__(self, parent=None): 
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()  
        self.ui.setupUi(self)
        self.student()

    def keyPressEvent(self,e):
        if e.key() == QtCore.Qt.Key_F2:
            self.accept()

    def student(self):
        db=QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("feedback.db")
        db.open()
        
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("select b.batch_id as ID, c.course_name as 'Name', b.batch_start_date as 'Start Date', b.batch_day as 'Day', b.batch_time as 'Time' from batch b, courses c where b.course_id = c.course_id")
        self.ui.tableView.setModel(self.model)
    def getBtName(self):
        dialog = Batch()
        dialog.show()
        result = dialog.exec_()
        if result == 1:
            index = dialog.ui.tableView.currentIndex()
            id_us = dialog.ui.tableView.model().data(index)
            if str(id_us).isdigit():
                return id_us
            else:
                QtGui.QMessageBox.information(self,  "Invalid Selection!",  "Please select the ID and not the name!")
                return ""
        else:
            return ""


if __name__=='__main__':

  app = QtGui.QApplication(sys.argv)
  myWindow = Batch(None)
  myWindow.show()
  app.exec_()
