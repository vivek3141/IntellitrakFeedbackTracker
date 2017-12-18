import sys
from PyQt4 import QtSql, QtCore, QtGui, uic
from main_feedback_auto import * 
import add_feedback_mod 
import query_feedback_mod 
import add_courses_mod 
import query_courses_mod 
import st_feedback_mod 
import st_form_mod 
import st_feedback_query_mod
import st_infoentry_mod
import st_modify_mod
import fee_infoentry_mod
import st_coursebatch_entry_mod
import st_coursebatch_modify_mod

class MainFeedback(QtGui.QMainWindow, Ui_MainWindow):
     def __init__(self, parent=None):
          QtGui.QMainWindow.__init__(self, parent)
          self.setupUi(self)

          QtCore.QObject.connect(self.actionAddFeedback,QtCore.SIGNAL('triggered()'),self.AddFeedback)
          QtCore.QObject.connect(self.actionQueryFeedback,QtCore.SIGNAL('triggered()'),self.QueryFeedback)
          QtCore.QObject.connect(self.actionAddCourse,QtCore.SIGNAL('triggered()'),self.AddCourses)
          QtCore.QObject.connect(self.actionQueryCourse,QtCore.SIGNAL('triggered()'),self.QueryCourses)
          QtCore.QObject.connect(self.actionModify_Feedback,QtCore.SIGNAL('triggered()'),self.StudentFeedQuery)
          QtCore.QObject.connect(self.actionStudent_feedback,QtCore.SIGNAL('triggered()'),self.StudentFeedback)
          QtCore.QObject.connect(self.actionSt_Add,QtCore.SIGNAL('triggered()'),self.AddStudent)
          QtCore.QObject.connect(self.actionSt_Modify,QtCore.SIGNAL('triggered()'),self.ModStudent)
          QtCore.QObject.connect(self.actionAddBatch,QtCore.SIGNAL('triggered()'),self.AddBatch)
          QtCore.QObject.connect(self.actionModify_3,QtCore.SIGNAL('triggered()'),self.ModBatch)
          QtCore.QObject.connect(self.actionStudent_Fees,QtCore.SIGNAL('triggered()'),self.Fees)
          QtCore.QObject.connect(self.actionAdd_Student,QtCore.SIGNAL('triggered()'),self.AddStudent)
          QtCore.QObject.connect(self.actionCreate_Batch,QtCore.SIGNAL('triggered()'),self.AddBatch)
          QtCore.QObject.connect(self.actionFees,QtCore.SIGNAL('triggered()'),self.Fees)                    
     def AddFeedback(self):
          add = add_feedback_mod.AddFeedback(self)
          add.setFixedSize(add.size())
          add.show()

     def QueryFeedback(self):
          query = query_feedback_mod.QueryFeedback(self)
          query.setFixedSize(query.size())
          query.show()
          query.ui.pb_select.setEnabled(False)

     def AddCourses(self):
          add1 = add_courses_mod.AddCourses(self)
          add1.setFixedSize(add1.size())
          add1.show()

     def QueryCourses(self):
          query1 = query_courses_mod.QueryCourses(self)
          query1.setFixedSize(query1.size())
          query1.show()

     def StudentFeedback(self):
          st1 = st_feedback_mod.STFeed(self)
          st1.setFixedSize(st1.size())
          st1.show()

     def StudentFeedQuery(self):
          st2 = st_feedback_query_mod.STQuery(self)
          st2.setFixedSize(st2.size())
          st2.show()

     def AddStudent(self):
          #addst=st_infoentry_mod.STInfoEntry(self)
          addst=st_modify_mod.STModify('A',self)
          #addst.mode="A"
          addst.setFixedSize(addst.size())
          addst.show()

     def ModStudent(self):
          modst=st_modify_mod.STModify("C",self)
          #modst.mode="C"
          modst.setFixedSize(modst.size())
          modst.show()

     def AddBatch(self):
          addb=st_coursebatch_entry_mod.STCourseBatch(self)
          addb.setFixedSize(addb.size())
          addb.show()

     def ModBatch(self):
          modb=st_coursebatch_modify_mod.STCourseBatch(self)
          modb.setFixedSize(modb.size())
          modb.show()

     def Fees(self):
          stfees=fee_infoentry_mod.FeesInfo(self)
          stfees.setFixedSize(stfees.size())
          stfees.show()
          
if (__name__ == "__main__"):                
     app = QtGui.QApplication(sys.argv)
     feed = MainFeedback(None)
     feed.show()
     feed.setFixedSize(feed.size())
     app.exec_()
