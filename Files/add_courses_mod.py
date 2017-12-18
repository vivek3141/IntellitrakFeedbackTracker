import sys
from PyQt4 import QtSql, QtCore, QtGui, uic
from add_courses_auto import *
from query_feedback_mod import *

class AddCourses(QtGui.QMainWindow, Ui_MainWindow_addCourses):
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
          QtCore.QObject.connect(self.pb_select,QtCore.SIGNAL('clicked()'),self.selectCourse)

     def loadTable(self):
          self.model = QtSql.QSqlTableModel(self)
          self.model.setTable("courses")
          self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
          self.tv_courses.setModel(self.model)
          self.tv_courses.setColumnWidth(1,230)
          self.model.select()
          self.model.setHeaderData(0,QtCore.Qt.Horizontal,"ID")
          self.model.setHeaderData(1,QtCore.Qt.Horizontal,"Course")
          self.model.setHeaderData(2,QtCore.Qt.Horizontal,"Feedback #1")
          self.model.setHeaderData(3,QtCore.Qt.Horizontal,"Feedback #2")
          self.model.setHeaderData(4,QtCore.Qt.Horizontal,"Feedback #3")
          self.model.setHeaderData(5,QtCore.Qt.Horizontal,"Feedback #4")
          self.model.setHeaderData(6,QtCore.Qt.Horizontal,"Feedback #5")
          self.model.setHeaderData(7,QtCore.Qt.Horizontal,"Feedback #6")
          self.model.setHeaderData(8,QtCore.Qt.Horizontal,"Other #1")
          self.model.setHeaderData(9,QtCore.Qt.Horizontal,"Other #2")
          self.model.setHeaderData(10,QtCore.Qt.Horizontal,"Other #3")
          self.model.setHeaderData(11,QtCore.Qt.Horizontal,"Other #4")
          self.model.setHeaderData(12,QtCore.Qt.Horizontal,"Other #5")
                                   
     def addRow(self):
          self.model.insertRows(self.model.rowCount(),1)

     def save(self):
          self.model.submitAll()
          self.model.select()

          QtGui.QMessageBox.information(self,"Message","Your changes have been saved")

     def selectCourse(self):
          var = 0

          #index_crs = self.tv_courses.model().index(index.row(), 0)

          #id_crs = self.tv_courses.model().data(index_crs)
          #print("kdkdkd",id_crs)

          index_crs = self.tv_courses.currentIndex()
          print("index ",str(index_crs))
          id_crs = self.tv_courses.model().data(index_crs)
          print("BBB",str(id_crs))
          if str(id_crs).isdigit() or str(id_crs).find("Null") >0:
               q1 = QueryFeedback()
               a = q1.selectFeed()
               if(str(a).isdigit()):
                    self.model.setData(index_crs,a)
          else:
               QtGui.QMessageBox.information(self,"Invalid selection","Please select the ID's anywhere from column 3-7")

     
     def keyPressEvent(self, e):
          if e.key() == QtCore.Qt.Key_F1:
            self.selectCourse()

if (__name__ == "__main__"):
        app = QtGui.QApplication(sys.argv)
        feed = AddCourses(None)
        feed.show()
        feed.setFixedSize(feed.size())
        app.exec_()
