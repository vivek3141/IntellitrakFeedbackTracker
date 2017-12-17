import sys
from PyQt4 import QtSql, QtCore, QtGui, uic
from query_feedback_auto import *

class QueryFeedback(QtGui.QDialog):
     def __init__(self, parent=None):
          QtGui.QMainWindow.__init__(self, parent)
          self.ui = Ui_Dialog()
          self.ui.setupUi(self)
          
          db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
          db.setDatabaseName("Feedback.db")
          db.open()
          self.loadTable()

     def loadTable(self):
          self.model = QtSql.QSqlQueryModel(self)
          query = "select fb_id as ID,fb_text as 'Feedback Text' from feedback;"
          self.model.setQuery(query)
          self.ui.tv_feedback.setModel(self.model)
          self.ui.tv_feedback.setColumnWidth(1,400)
          
     def selectFeed(self):
          while(True):
               q2 = QueryFeedback()
               res = q2.exec_()
               if res == 1:
                    index = q2.ui.tv_feedback.currentIndex()
                    id_us = q2.ui.tv_feedback.model().data(index)
                    if str(id_us).isdigit():
                         return id_us
                    else:
                         QtGui.QMessageBox.information(self,"Invalid selection","Please select the ID in column 1")
                         continue
               else:
                    return ""

if (__name__ == "__main__"):
     app = QtGui.QApplication(sys.argv)
     feed = QueryFeedback(None)
     feed.show()
     feed.setFixedSize(feed.size())
     sys.exit(app.exec_())
