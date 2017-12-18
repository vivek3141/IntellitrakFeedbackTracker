import sys
from PyQt4 import QtCore, QtGui, uic, QtSql
import sqlite3
 
from student_auto import * 
  
class Student(QtGui.QDialog):
    def __init__(self, bid=0,mode='N', parent=None): 
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()  
        self.ui.setupUi(self)
        self.mode=mode
        self.bid=bid
        if mode=='N':
            self.student()
        else:
            self.batchStudent(bid)

        QtCore.QObject.connect(self.ui.btn_query, QtCore.SIGNAL('clicked()'), self.query)
      

    def query(self):
        db=QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("feedback.db")
        db.open()
        
        self.model = QtSql.QSqlQueryModel(self)
        if self.mode=="N":
            msql='select st_id as "ID", st_full_name as "Name", st_parent_name  as "Parent' + "'s Name"+\
                  '", st_address_1 as "Address" from student where st_full_name like "%'+self.ui.lne_fname.text()+'%";'
        else:
            msql='select s.st_id as "ID", s.st_full_name as "Name", st_parent_name  as "Parent Name", \
                 st_address_1 as "Address"  from student s, st_batch_link b where \
                 st_full_name like "%'+self.ui.lne_fname.text()+'%" and s.st_id = b.st_id \
                 and b.batch_id = '+str(self.bid)+';'
        self.model.setQuery(msql)
        self.ui.tableView.setModel(self.model)
            
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_F1:
            self.accept()
        elif e.key()==QtCore.Qt.Key_F10:
            self.query()
            
    def student(self):
        db=QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("feedback.db")
        db.open()
        
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery('select st_id as "ID", st_full_name as "Name", st_parent_name  as "Parent' + "'s Name"+'", st_address_1 as "Address" from student;')
        self.ui.tableView.setModel(self.model)
        
    def batchStudent(self, btid):
        db=QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("feedback.db")
        db.open()
        
        self.model = QtSql.QSqlQueryModel(self)

        mysql='select s.st_id as "ID", s.st_full_name as "Name", st_parent_name  as "Parent Name", \
                 st_address_1 as "Address"  from student s, st_batch_link b where s.st_id = b.st_id \
                 and b.batch_id = '+str(btid)+';'
        btid=0
        self.model.setQuery(mysql)
        self.ui.tableView.setModel(self.model)

    def getStName(self, *args):
        if len(args) >0:
            mode=args[0]
            helloid=args[1]
            dialog = Student(helloid,'B')
        else:
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
