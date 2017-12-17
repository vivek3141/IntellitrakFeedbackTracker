import sys
import sqlite3
import datetime as dt
from PyQt4 import QtCore, QtGui, uic, QtSql
from st_coursebatch_entry_auto import *
import selectingDate_mod
from student_mod import *

class STCourseBatch(QtGui.QMainWindow, Ui_MainWindow):
    def __init__ (self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.conn= sqlite3.connect('feedback.db')
        self.lne_date.setText(dt.datetime.today().strftime("%b %d, %Y"))
        QtCore.QObject.connect(self.btn_date,QtCore.SIGNAL('clicked()'), self.openCalendar)
        QtCore.QObject.connect(self.btn_save,QtCore.SIGNAL('clicked()'), self.save)
        QtCore.QObject.connect(self.btn_selectstudent,QtCore.SIGNAL('clicked()'), self.students)
        QtCore.QObject.connect(self.btn_del,QtCore.SIGNAL('clicked()'), self.delete)
        QtCore.QObject.connect(self.lne_time, QtCore.SIGNAL('focusOutEvent()'),self.morn)
        self.countst=0
        self.student = []
        db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('feedback.db')
        db.open()
        self.setCombo()
        self.lbl_morn.hide()
        
    def morn(self):
        print("morn, focus out")
    def keyPressEvent(self,e):
        li=[]
        time= self.lne_time.text()
        if time.find(":")>=0:
            li = time.split(":")
            print(li)
        elif time.find(".")>=0:
            li=time.split('.')
            print(li)
        try:
            if int(li[0])<12:
                self.lbl_morn.show()
            else:
                self.lbl_morn.hide()
        except Exception :
            pass
            
        if e.key() == QtCore.Qt.Key_F1:
            self.students()
        elif e.key() == QtCore.Qt.Key_Delete:
            self.delete()
        
    def delete(self):
        finalid = self.lw_students.currentItem().text()
        finalid = finalid[0]
        print(finalid)
        print(self.student)
        self.lw_students.takeItem(self.lw_students.currentRow())
        QtGui.QMessageBox.information(self, "DELETED","This Student has been deleted")
        for i in self.student:
            if str(i) == str(finalid):
                self.student.remove(i)
                print(self.student)
            else:
                print("UGHH")
        self.countst=self.countst-1
        if self.countst!=10:
            self.btn_selectstudent.setEnabled(True)
            self.btn_selectstudent.show()
        else:
            pass

    def students(self):
        a = Student()
        retval = a.getStName()
        if retval == "":
            return False
        if retval > 0:
            self.st_id = retval
            cursor = self.conn.cursor()
            cursor.execute("select st_full_name from student where st_id = " +str(retval))
            row = cursor.fetchall()
            a = row[0]
            a = a[0]
            self.lw_students.addItem(str(retval)+"   "+a)
            
            self.student.append(retval)
        else:
            return False
        self.countst=self.countst+1
        if self.countst==10:
            self.btn_selectstudent.setEnabled(False)
            self.btn_selectstudent.hide()
        else:
            pass
        
    def setCombo(self):
        self.cb_course.addItem("Select course")
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
                        self.cb_course.addItem(mystr)
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
            self.mode = "a"
            return False
        self.conn.commit()

    def save(self):
        date=self.lne_date.text()
        inst=self.lne_instructor.text()
        day=self.cb_day.currentText()
        time=self.lne_time.text()
        cr_id=self.cb_course.currentText()[:2]
     
        try:
            cr_id=int(cr_id)
            cursor=self.conn.cursor()
            cursor.execute('INSERT INTO batch (course_id, batch_start_date, batch_instructor, batch_day, batch_time)\
                            VALUES (?,?,?,?,?)', (cr_id, date, inst, day, time))
            cursor.execute("SELECT batch_id from batch where course_id ='"+str(cr_id)+"' and batch_start_date=\
                           '"+str(date)+"' and batch_instructor= '"+str(inst)+"' and batch_day='"+str(day)+"' and batch_time='"+str(time)+"'")
            row=cursor.fetchall()
            self.bid=row[0]
            self.bid=self.bid[0]
            for i in self.student:
                cursor.execute('INSERT INTO st_batch_link (st_id,batch_id) VALUES (?,?)', (i,self.bid))
            self.conn.commit()
            
            QtGui.QMessageBox.information(self, "Saved succesfully","Your information has been saved")
            self.close()
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self, "ERROR", e.args[0])
            self.conn.rollback()
        except ValueError:
            QtGui.QMessageBox.information(self, "ERROR", "Incorrect Id")
            
    def openCalendar(self):
        #CALLING CALENDAR WINDOW
        cal=selectingDate_mod.MyForm(self)
        #getMeDate IS FUNCTION IN selectingDate_mod THAT USES accept() AND reject() SINGAL SLOTS
        retval=cal.getMeDate()
        if retval !="":
          self.lne_date.setText(retval)

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = STCourseBatch(None)
    myWindow.show()
    app.exec_()
