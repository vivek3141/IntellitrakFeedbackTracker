import sys
from PyQt4 import QtCore, QtGui, uic, QtSql
import sqlite3
 
from student_auto import * 
  
class Student_Copy(QtGui.QDialog):
    def __init__(self, parent=None): 
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()  
        self.ui.setupUi(self)
        self.student()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_F1:
            self.accept()
    def student(self):
        db=QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("feedback.db")
        db.open()
        
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery('select st_id as "ID", st_full_name as "Name", st_parent_name  as "Parent' + "'s Name"+'", st_address_1 as "Address" from student;')
        print('select st_id as "ID", st_full_name as "Name", st_parent_name  as "Parent' + "'s Name"+'", st_address_1 as "Address" from student;')
        self.ui.tableView.setModel(self.model)
    def getStName(self):
        dialog = Student()
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
  myWindow = Student(None)
  myWindow.show()
  app.exec_()
