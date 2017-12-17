import sys
from PyQt4 import QtCore, QtGui, uic,  QtSql 
import sqlite3 
from st_feedback_auto import *
from student_mod import * 
 
class STFeed(QtGui.QMainWindow, Ui_studentFeedback):
    def __init__(self, parent=None): 
        self.st_id = 0
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.conn= sqlite3.connect("feedback.db")
        self.retrieve()
        QtCore.QObject.connect(self.pb_getfeed, QtCore.SIGNAL('clicked()'),self.course)
        QtCore.QObject.connect(self.pb, QtCore.SIGNAL('clicked()'),self.student)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.save)
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("feedback.db")
        db.open()
        self.cb1 = ""
        self.cb2 = ""
        self.cb3 = ""
        self.cb4 = ""
        self.cb5 = ""
        self.f6 = ""
        
    def student(self):
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
            self.lineEdit.setText(str(a))
        else:
            return False
            
    def retrieve(self):
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
        self.conn.commit()
    def save(self):
        if self.st_id == 0:
            QtGui.QMessageBox.information(self,  "Please Enter",  "Please select a Student")
            return False
        if str(self.textEdit.toPlainText()) == "":
            QtGui.QMessageBox.information(self,  "Please Enter",  "Nothing has been entered for comments!")
            return False
        self.dn(self.rb_dn_1, 1)
        self.dn(self.rb_dn_2, 2)
        self.dn(self.rb_dn_3, 3)
        self.dn(self.rb_dn_4, 4)
        self.dn(self.rb_dn_5, 5)
        self.d(self.rb_d_1, 1)
        self.d(self.rb_d_2, 2)
        self.d(self.rb_d_3, 3)
        self.d(self.rb_d_4, 4)
        self.d(self.rb_d_5, 5)
        self.a(self.rb_a_1, 1)
        self.a(self.rb_a_2, 2)
        self.a(self.rb_a_3, 3)
        self.a(self.rb_a_4, 4)
        self.a(self.rb_a_5, 5)
        self.n(self.rb_n_1, 1)
        self.n(self.rb_n_2, 2)
        self.n(self.rb_n_3, 3)
        self.n(self.rb_n_4, 4)
        self.n(self.rb_n_5, 5)
        self.sa(self.rb_sa_1, 1)
        self.sa(self.rb_sa_2, 2)
        self.sa(self.rb_sa_3, 3)
        self.sa(self.rb_sa_4, 4)
        self.sa(self.rb_sa_5, 5)
        self.dn(self.rb_dn_6, 6)
        self.d(self.rb_d_6, 6)
        self.n(self.rb_n_6, 6)
        self.a(self.rb_a_6, 6)
        self.sa(self.rb_sa_6, 6)
        self.id1 = self.barn[0]
        self.id2 = self.barn[1]
        self.id3 = self.barn[2]
        self.id4 = self.barn[3]
        self.id5 = self.barn[4]
        self.id6 = self.barn[5]
        if self.checkBox.isChecked():
            self.cb1 = self.checkBox.text()
        if self.checkBox_2.isChecked():
            self.cb2 = self.checkBox_2.text()
        if self.checkBox_3.isChecked():
            self.cb3 = self.checkBox_3.text()
        if self.checkBox_4.isChecked():
            self.cb4 = self.checkBox_4.text()
        if self.checkBox_5.isChecked():
            self.cb5 = self.checkBox_5.text()
        if self.id1=="" or self.id2=="" or self.id3=="" or self.id4=="" or self.id5=="":
            QtGui.QMessageBox.information(self,  "Please Enter",  "Feedback questions 1 to 5 have to be answered")
            return False       
        
        try:
            cursor = self.conn.cursor()
            print(self.f1, self.f2, self.f3, self.f4, self.f5)
            cursor.execute("INSERT INTO st_feedback values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, ?, ?)", \
            (self.st_id, self.id, self.id1, self.id2, self.id3, self.id4, self.id5,self.id6 , self.f1, self.f2, self.f3, self.f4, self.f5,self.f6, str(self.textEdit.toPlainText()), self.cb1, self.cb2,self.cb3,self.cb4, self.cb5))
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
            self.mode = "a"
            return False
        self.conn.commit()
        QtGui.QMessageBox.information(self,  "Saved Successfully!",  "Your entry was saved!")
        self.close()
    def dn(self, rb, no):
        a = rb.isChecked()
        if a:
            if no == 1:
                self.f1 = 1
            if no == 2:
                self.f2 = 1
            if no == 3:
                self.f3 = 1
            if no == 4:
                self.f4 = 1
            if no == 5:
                self.f5 = 1
            if no == 6:
                self.f6 = 1
            return False
        else:
            return False
            
    def d(self, rb, no):
        a = rb.isChecked()
        if a:
            if no == 1:
                self.f1 = 2
            if no == 2:
                self.f2 = 2
            if no == 3:
                self.f3 = 2
            if no == 4:
                self.f4 = 2
            if no == 5:
                self.f5 = 2
            if no == 6:
                self.f6 = 2
            return False
        else:
            return False
    def n(self, rb, no):
        a = rb.isChecked()
        if a:
            if no == 1:
                self.f1 = 3
            if no == 2:
                self.f2 = 3
            if no == 3:
                self.f3 = 3
            if no == 4:
                self.f4 = 3
            if no == 5:
                self.f5 = 3
            if no == 6:
                self.f6 = 3
            return False
        else:
            return False
    def a(self, rb, no):
        a = rb.isChecked()
        if a:
            if no == 1:
                self.f1 = 4
            if no == 2:
                self.f2 = 4
            if no == 3:
                self.f3 = 4
            if no == 4:
                self.f4 = 4
            if no == 5:
                self.f5 = 4
            if no == 6:
                self.f6 = 4
            return False
        else:
            return False
    def sa(self, rb, no):
        a = rb.isChecked()
        if a:
            if no == 1:
                self.f1 = 5
            if no == 2:
                self.f2 = 5
            if no == 3:
                self.f3 = 5
            if no == 4:
                self.f4 = 5
            if no == 5:
                self.f5 = 5
            if no == 6:
                self.f6 = 5
            return False
        else:
            return False
        
    def course(self):
        print("a")
        try:
            cursor = self.conn.cursor()
            text = self.comboBox.currentText()
            text.split(" : ")
            print(text)
            self.id = text[0]
            sql = 'select c.course_name as Course, f1.fb_text Feedback1, \
            f2.fb_text Feedback2, f3.fb_text Feedback3, f4.fb_text Feedback4, \
            f5.fb_text Feedback5, f6.fb_text Feedback6, oth_1 OtherCourses, oth_2 OtherCourses, \
            oth_3 OtherCourses, oth_4 OtherCourses, oth_5 OtherCourses, fb_id1, fb_id2, fb_id3, fb_id4, fb_id5, fb_id6 \
            from courses c, feedback f1, feedback f2, feedback f3, feedback f4, \
            feedback f5 left join feedback f6 on c.fb_id6 = f6.fb_id\
            where c.fb_id1 = f1.fb_id and c.fb_id2 =f2.fb_id \
            and c.fb_id3 = f3.fb_id and c.fb_id4 = f4.fb_id \
            and c.fb_id5 = f5.fb_id  and c.course_id = '+self.id
            cursor.execute(sql)
            row = cursor.fetchall()
            row = row[0]
            print(row)
            self.lbl_1.setText(row[1])
            self.lbl_2.setText(row[2])
            self.lbl_3.setText(row[3])
            self.lbl_4.setText(row[4])
            self.lbl_5.setText(row[5])
            if row[6] == None:
                self.rb_dn_6.setVisible(False)
                self.rb_d_6.setVisible(False)
                self.rb_n_6.setVisible(False)
                self.rb_a_6.setVisible(False)
                self.rb_sa_6.setVisible(False)
            else:
                self.lbl_6.setText(row[6])
                self.rb_dn_6.setVisible(True)
                self.rb_d_6.setVisible(True)
                self.rb_n_6.setVisible(True)
                self.rb_a_6.setVisible(True)
                self.rb_sa_6.setVisible(True)
                
            self.checkBox.setText(row[7])
            self.checkBox_2.setText(row[8])
            self.checkBox_3.setText(row[9])
            self.checkBox_4.setText(row[10])
            if row[11] == None:
                self.checkBox_5.setVisible(False)
            else:
                self.checkBox_5.setVisible(True)
                self.checkBox_5.setText(row[11])
            self.barn = []
            for i in range(12, 18):
                self.barn.append(row[i])
            print(self.barn)
#            a = ""
#            for i in row:
#                if i == 5:
#                    a = a + str(i)
#                else:
#                    a = a + str(i) + " or "
#            print(a)
#            cursor.execute("select fb_text from feedback where fb_id = "+a)
#            row = cursor.fetchall()
#            
#            for i in row[0]:
#                self.lbl_1.setText(i)
#            for i in row[1]:
#                self.lbl_2.setText(i)
#            for i in row[2]:
#                self.lbl_3.setText(i)
#            for i in row[3]:
#                self.lbl_4.setText(i)
#            for i in row[4]:
#                self.lbl_5.setText(i)
#            try: 
#                for i in row[5]:
#                    self.lbl_6.setText(i)
#            except IndexError:
#                pass
#            cursor.execute("select oth_1,oth_2,oth_3,oth_4 from courses where course_id = "+str(self.id))
#            row = cursor.fetchall()
#            print(row)
#            a = []
#            for i in row:
#                a = i
#            print(a[0])
#            self.checkBox.setText(a[0])
#            self.checkBox_2.setText(a[1])
#            self.checkBox_3.setText(a[2])
#            self.checkBox_4.setText(a[3])
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self,  "An Error occurred:",  str(e.args[0]))
            return False
        self.conn.commit()
        
        
         
if __name__ == "__main__": 
    app = QtGui.QApplication(sys.argv)
    myWindow = STFeed(None)
    myWindow.show()
    myWindow.setFixedSize(myWindow.size())
    app.exec_() 
