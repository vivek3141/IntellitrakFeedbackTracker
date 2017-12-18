import sys
from PyQt4 import QtSql, QtCore, QtGui, uic
from query_courses_auto import *

class QueryCourses(QtGui.QMainWindow, Ui_MainWindow_queryCourses):
     def __init__(self, parent=None):
          QtGui.QMainWindow.__init__(self, parent)
          self.setupUi(self)
          
          db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
          db.setDatabaseName("Feedback.db")
          db.open()
          self.loadTable()

     def loadTable(self):

          self.model = QtSql.QSqlQueryModel(self)
          query = " select c.course_name as Course, f1.fb_text 'Feedback #1', f2.fb_text 'Feedback #2', \
                    f3.fb_text 'Feedback #3', f4.fb_text 'Feedback #4', f5.fb_text 'Feedback #5',\
                   f6.fb_text 'Feedback #6', oth_1 'Other #1', oth_2 'Other #2', oth_3 'Other #3', \
                   oth_4 'Other #4', oth_5 'Other #5' \
                   from courses c, feedback f1, feedback f2, feedback f3, feedback f4, feedback f5\
				   left outer join feedback f6 on f6.fb_id = c.fb_id6\
                   where c.fb_id1 = f1.fb_id and c.fb_id2 =f2.fb_id and c.fb_id3 = f3.fb_id and \
                   c.fb_id4 = f4.fb_id and c.fb_id5 = f5.fb_id;"
                   
         
                 
          self.model.setQuery(query)
          self.tv_courses.setModel(self.model)
          self.tv_courses.setColumnWidth(0,230)
          self.tv_courses.resizeColumnsToContents()
          
if (__name__ == "__main__"):
        app = QtGui.QApplication(sys.argv)
        feed = QueryCourses(None)
        feed.show()
        feed.setFixedSize(feed.size())
        app.exec_()
