import sys
from PyQt4 import QtCore, QtGui, uic, QtSql 
import sqlite3  
from st_feedback_query_auto import * 
import st_form_mod 
  
class STQuery(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.btn_select)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'), self.btn_search)
        #QtCore.QObject.connect(self.cbx_helpme, QtCore.SIGNAL('stateChanged()'), self.checkchange)
        self.cbx_helpme.stateChanged.connect(self.checkchange)
        self.conn= sqlite3.connect("feedback.db")
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("feedback.db")
        db.open()
        self.btn_retrieveall()
        self.getCourses()
        self.passed = ""
        
    
    def checkchange(self,int):
        if self.label_2.isVisible():
            self.label_2.setVisible(False)
            self.label_3.setVisible(False)
        else:
            self.label_2.setVisible(True)
            self.label_3.setVisible(True)

    def btn_search(self):
        text = self.comboBox.currentText()
        if text == "All":
            self.btn_retrieveall()
            return False
        text.split(" : ")
        self.id = text[0]
        qls = " select st_full_name as 'Full Name', f1.fb_text as 'FB Text 1',  c.fb_rating1 as 'Rating 1',\
            f2.fb_text 'FB Text 2', c.fb_rating2 as 'Rating 2', f3.fb_text as 'FB Text 3',  c.fb_rating3 as 'Rating 3', f4.fb_text as 'FB Text 4', c.fb_rating4 as 'Rating 4',\
            f5.fb_text as 'FB Text 5', c.fb_rating5 as 'Rating 5',f6.fb_text as 'FB Text 6', c.fb_rating6 as 'Rating 6', c.course_id as cid, c.st_id as stid\
            from st_feedback c, student s, feedback f1, feedback f2, feedback f3, feedback f4, \
            feedback f5 left join feedback f6 on c.fb_id6 = f6.fb_id where c.fb_id1 = f1.fb_id and c.fb_id2 =f2.fb_id \
            and c.fb_id3 = f3.fb_id and c.fb_id4 = f4.fb_id \
            and c.fb_id5 = f5.fb_id\
			and s.st_id = c.st_id and c.course_id = "+self.id
        self.model.setQuery(qls)
        self.tableView.setModel(self.model)
           
    def btn_select(self):
        var = 0
        indexes = self.tableView.selectionModel().selectedRows()

        # if multiple selection is possible use a for loop otherwise
        # no need to use for loop
        for index in sorted(indexes):
            #print('Row %d is selected' % index.row())
            index_crs = self.tableView.model().index(index.row(), 13)

            id_cid = self.tableView.model().data(index_crs)
            print("Course ID",id_cid)
            index_crs = self.tableView.model().index(index.row(), 14)

            id_stid = self.tableView.model().data(index_crs)
            print("Student ID ID",id_stid)
        #item (self, int row, int column)
        #index_crs = self.tableView.currentIndex()
        
        
        #index_crs = self.tableView.item(1,2)
        self.passed = str(id_stid) + ',' + str(id_cid)
        #print(self.passed)

        a = st_form_mod.STForm(self)
        # passing the parameter to STForm
        a.param = self.passed
        a.show()
        a.fill()
        
    def btn_retrieveall(self):
        self.model = QtSql.QSqlQueryModel(self)
        sql = " select st_full_name as 'Full Name', f1.fb_text as 'FB Text 1',  c.fb_rating1 as 'Rating 1',\
            f2.fb_text 'FB Text 2', c.fb_rating2 as 'Rating 2', f3.fb_text as 'FB Text 3',  c.fb_rating3 as 'Rating 3', f4.fb_text as 'FB Text 4', c.fb_rating4 as 'Rating 4',\
            f5.fb_text as 'FB Text 5', c.fb_rating5 as 'Rating 5',f6.fb_text as 'FB Text 6', c.fb_rating6 as 'Rating 6', c.course_id as cid, c.st_id as stid\
            from st_feedback c, student s, feedback f1, feedback f2, feedback f3, feedback f4, \
            feedback f5 left join feedback f6 on c.fb_id6 = f6.fb_id where c.fb_id1 = f1.fb_id and c.fb_id2 =f2.fb_id \
            and c.fb_id3 = f3.fb_id and c.fb_id4 = f4.fb_id \
            and c.fb_id5 = f5.fb_id\
			and s.st_id = c.st_id"
        self.model.setQuery(sql)
        self.tableView.setModel(self.model)
#        self.model = QtSql.QSqlTableModel(self)         
#        self.model.setTable("st_feedback") 
#        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)         
#        self.model.select()         
#        self.tableView.setModel(self.model) 
    def btn_save(self):
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.model.submitAll()
        self.model.select()
    def getCourses(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("select course_id, course_name from courses")
            row = cursor.fetchall()
            for i in row:
                a = i
                for i in a:
                    if str(i).isdigit():
                        digit = i
                    else:
                        mystr = str(digit) + " : " + str(i)
                        self.comboBox.addItem(mystr)
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
            self.mode = "a"
            return False

    
    def keyPressEvent(self, e):
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        if e.key() == QtCore.Qt.Key_F1:
            self.btn_select()
        elif e.key() == QtCore.Qt.Key_F10:
            self.btn_search()
            
         
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = STQuery(None)
    myWindow.show()
    myWindow.setFixedSize(myWindow.size())
    app.exec_() 
