import sys
import sqlite3
import datetime as dt
from PyQt4 import QtCore, QtGui, uic, QtSql
from st_coursebatch_modify_auto import *
import selectingDate_mod
from student_mod import *
from batch_mod import *

class STCourseBatch(QtGui.QMainWindow, Ui_MainWindow):
    def __init__ (self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.conn= sqlite3.connect('feedback.db')
        self.lne_date.setText(dt.datetime.today().strftime("%b %d, %Y"))
        QtCore.QObject.connect(self.btn_date,QtCore.SIGNAL('clicked()'), self.openCalendar)
        QtCore.QObject.connect(self.btn_save,QtCore.SIGNAL('clicked()'), self.update)
        QtCore.QObject.connect(self.btn_selectstudent,QtCore.SIGNAL('clicked()'), self.students)
        QtCore.QObject.connect(self.btn_del,QtCore.SIGNAL('clicked()'), self.delete)
        QtCore.QObject.connect(self.btn_select,QtCore.SIGNAL('clicked()'), self.getBack)
        QtCore.QObject.connect(self.lne_time, QtCore.SIGNAL('focusOutEvent()'),self.morn)
        self.countst=0
        self.student = []
        self.bt_id =0
        db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('feedback.db')
        db.open()
        self.setCombo()
        self.lbl_morn.hide()
        self.lne_date.setEnabled(False)
        self.btn_selectstudent.setEnabled(False)
        self.lne_instructor.setEnabled(False)
        self.lne_time.setEnabled(False)
        self.lne_day.setEnabled(False)
        
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
        elif e.key() == QtCore.Qt.Key_F2:
            self.getBack()

    def getBack(self):
        a = Batch()
        self.retval = a.getBtName()
        self.bt_id = self.retval
        if self.retval == "":
            return False
        elif self.retval !="":
          self.insertVal(self.retval)

    def insertVal(self,bid):
        self.btn_selectstudent.setEnabled(True)
        self.lw_students.clear()
        self.cb_course.setEnabled(True)
        self.lne_date.setEnabled(True)
        self.lne_instructor.setEnabled(True)
        self.lne_time.setEnabled(True)
        self.lne_day.setEnabled(True)
        try:
          cursor=self.conn.cursor()
          cursor.execute("SELECT batch_start_date, batch_instructor, batch_time, batch_day,course_id from batch where batch_id="+str(bid))
          row=cursor.fetchall()
          print(row)
          if len(row) == 0:
            QtGui.QMessageBox.information(self, "Not Found!!!", "There were no records found")
            return False
          else:
            for i in row:
              doj,iname,time,day,cid = i

              
            self.lne_date.setText(doj)
            self.lne_instructor.setText(iname)
            self.lne_time.setText(time)
            self.lne_day.setText(day)

            

            cursor=self.conn.cursor()
            cursor.execute("SELECT course_name from courses where course_id="+str(cid))
            course=cursor.fetchall()
            course = str(course[0])
            course = course[:-3]  #removing "'"  "," and ")" of tuple
            course = course[::-1]  #making word opposite
            course = course[:-2]  #removing "(" and "'"
            course = course[::-1] #making word back to normal
            course = str(cid)+" : "+ course
            print(course)
            index = self.cb_course.findText(course , QtCore.Qt.MatchFixedString)
            if index >= 0:
                 self.cb_course.setCurrentIndex(index)
            else:
                print("Oh No!!")

            hello = []
            cursor=self.conn.cursor()
            cursor.execute("SELECT st_id from st_batch_link where batch_id="+str(bid))
            students=cursor.fetchall()
            print(students)
            for i in students:
                sid = str(i)
                sid = sid[:-2]  #removing "," and ")" of tuple
                sid = sid[::-1]  #making word opposite
                sid = sid[:-1]  #removing "("
                sid = sid[::-1] #making word back to normal
                
                print("SID ="+sid)
                cursor=self.conn.cursor()
                cursor.execute("SELECT st_full_name from student where st_id= "+str(sid))
                row=cursor.fetchall()
                a = row[0]
                a = a[0]
                self.lw_students.addItem(str(sid)+"   "+a)                   

        except sqlite3.Error as e:
          QtGui.QMessageBox.information(self, " An error occured",e)

        
    def delete(self):
        finalid = self.lw_students.currentItem().text()
        finalid = finalid[0]
        print("STID "+finalid)
        print(self.bt_id)
        try:
            cursor=self.conn.cursor()
            cursor.execute("DELETE from st_batch_link where st_id= "+str(finalid)+" and batch_id = "+str(self.bt_id))
            self.conn.commit()
            self.lw_students.takeItem(self.lw_students.currentRow())
            QtGui.QMessageBox.information(self, "DELETED","This Student has been deleted")
            self.countst=self.countst-1
            if self.countst!=10:
                self.btn_selectstudent.setEnabled(True)
                self.btn_selectstudent.show()
            else:
                pass
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self, "ERROR", e.args[0])
            self.conn.rollback()

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
            self.lw_students.addItem(str(retval)+"    "+a)
            self.student.append(retval)
        else:
            return False
        self.countst=self.countst+1
        if self.countst==10:
            self.btn_selectstudent.setEnabled(False)
            self.btn_selectstudent.hide()
        else:
            pass
        try:
            self.conn.cursor()
            cursor.execute('INSERT INTO st_batch_link (st_id,batch_id) VALUES (?,?)', (retval,self.bt_id))
            self.conn.commit()
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self, "ERROR", e.args[0])
            self.conn.rollback()
            
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
            self.cb_course.setEnabled(False)
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
            return False
        self.conn.commit()
        

    def update(self):
        
        date=self.lne_date.text()
        inst=self.lne_instructor.text()
        day=self.lne_day.text()
        time=self.lne_time.text()
        cr_id=self.cb_course.currentText()[:2]
        
        try:
            cursor=self.conn.cursor()
            cursor.execute('UPDATE batch SET course_id = '+str(cr_id)+' , batch_start_date = "'+date+'" , batch_instructor = "'+str(inst)+'" ,batch_day = "'+str(day) +'" , batch_time = "'+str(time)+'" where batch_id = '+str(self.retval))
            self.conn.commit()
            QtGui.QMessageBox.information(self, "Update succesful","Your information has been updated")
            self.close()
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self, "ERROR", e.args[0])
            self.conn.rollback()
            
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
