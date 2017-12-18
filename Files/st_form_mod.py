import sys
from PyQt4 import QtCore, QtGui, uic,  QtSql 
import sqlite3 
from st_form_auto import *
from student_mod import *
from st_feedback_query_mod import *
 
class STForm(QtGui.QMainWindow, Ui_studentFeedback):
    def __init__(self, parent=None): 
        self.st_id = 0
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.conn= sqlite3.connect("feedback.db")
#       self.retrieve()
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.save)
##        QtCore.QObject.connect(self.cbx_helpme, QtCore.SIGNAL('stateChanged()'), self.checkchange)
#       db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
#       db.setDatabaseName("feedback.db")
#       db.open()
        self.param="a"
        self.a1 = STQuery()
        self.f6 = ""
        self.checkBox_5.setEnabled(False)
    #    self.fill()

##    def checkchange(self):
##        if label_2.isVisible:
##            label_2.setVisible(False)
##            label_3.setVisible(False)
##        else:
##            label_2.setVisible(False)
##            label_3.setVisible(True)

    def hide(self):
        if self.lbl_6.text() == "":
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
            
        if self.checkBox.text() == "" or self.checkBox.text() == None :
            self.checkBox.setVisible(False)
        else:
            self.checkBox.setVisible(True)
            
        if self.checkBox_2.text() == "" or self.checkBox_2.text() == None :
            self.checkBox_2.setVisible(False)
        else:
            self.checkBox_2.setVisible(True)
            
        if self.checkBox_3.text() == "" or self.checkBox_3.text() == None :
            self.checkBox_3.setVisible(False)
        else:
            self.checkBox_3.setVisible(True)
            
        if self.checkBox_4.text() == "" or self.checkBox_4.text() == None :
            self.checkBox_4.setVisible(False)
        else:
            self.checkBox_4.setVisible(True)
            
        if self.checkBox_5.text() == "" or self.checkBox_5.text() == None :
            self.checkBox_5.setVisible(False)
        else:
            self.checkBox_5.setVisible(True)



    def fill(self):
        print("Param:",self.param)
        splitted = self.param.split(",")
        self.stid = splitted[0]
        self.courseid = splitted[1]
        print("Param:",splitted)
        print("stid:",self.stid)
        print("crseid:",self.courseid)
        try:
            cursor = self.conn.cursor()
            sql1="select  f.st_id, f.course_id, f.fb_id1, f.fb_id2, f.fb_id3	,\
            f.fb_id4, f.fb_id5, f.fb_id6, f.fb_rating1, f.fb_rating2, f.fb_rating3, f.fb_rating4, \
            f.fb_rating5, f.fb_rating6, f.comments, f.oth_1, f.oth_2, f.oth_3,f.oth_4, f.oth_5, \
            f1.fb_text as ft1, f2.fb_text as ft2,f3.fb_text as ft3,f4.fb_text as ft4,f5.fb_text as ft5,f6.fb_text as ft6\
            from st_feedback f,  feedback f1,  feedback f2,  feedback f3,  feedback f4,  feedback f5 left join feedback f6\
            on  f6.fb_id = f.fb_id6\
            where f.st_id = "+self.stid+" and f.course_id = "+self.courseid+"\
            and f1.fb_id = f.fb_id1\
            and f2.fb_id = f.fb_id2\
            and f3.fb_id = f.fb_id3\
            and f4.fb_id = f.fb_id4\
            and f5.fb_id = f.fb_id5;"
            print(sql1)
            cursor.execute(sql1)

            row = cursor.fetchall()

            row = row[0]
            self.checkBox.setText(row[15])
            self.checkBox_2.setText(row[16])
            self.checkBox_3.setText(row[17])
            self.checkBox_4.setText(row[18])
            self.checkBox_5.setText(row[19])
            if self.checkBox.text() == '':
                self.checkBox.setChecked(False)
            else:
                self.checkBox.setChecked(True)
                
            if self.checkBox_2.text() == '':
                self.checkBox_2.setChecked(False)
            else:
                self.checkBox_2.setChecked(True)
                
            if self.checkBox_3.text() == '':
                self.checkBox_3.setChecked(False)
            else:
                self.checkBox_3.setChecked(True)
                
            if self.checkBox_4.text() == '':
                self.checkBox_4.setChecked(False)
            else:
                self.checkBox_4.setChecked(True)
            if self.checkBox_5.text() == '':
                self.checkBox_5.setChecked(False)
            else:
                self.checkBox_5.setChecked(True)
            self.rb1 = row[8]
            self.rb2 = row[9]
            self.rb3 = row[10]
            self.rb4 = row[11]
            self.rb5 = row[12]
            self.rb6 = row[13]
            if self.rb1 == 1:
                self.rb_dn_1.setChecked(True)
            if self.rb1 == 2:
                self.rb_d_1.setChecked(True)
            if self.rb1 == 3:
                self.rb_n_1.setChecked(True)
            if self.rb1 == 4:
                self.rb_a_1.setChecked(True)
            if self.rb1 == 5:
                self.rb_sa_1.setChecked(True)
                
            if self.rb2 == 1:
                self.rb_dn_2.setChecked(True)
            if self.rb2 == 2:
                self.rb_d_2.setChecked(True)
            if self.rb2 == 3:
                self.rb_n_2.setChecked(True)
            if self.rb2 == 4:
                self.rb_a_2.setChecked(True)
            if self.rb2 == 5:
                self.rb_sa_2.setChecked(True)
                
            if self.rb3 == 1:
                self.rb_dn_3.setChecked(True)
            if self.rb3 == 2:
                self.rb_d_3.setChecked(True)
            if self.rb3 == 3:
                self.rb_n_3.setChecked(True)
            if self.rb3== 4:
                self.rb_a_3.setChecked(True)
            if self.rb3 == 5:
                self.rb_sa_3.setChecked(True)
                
            if self.rb4 == 1:
                self.rb_dn_4.setChecked(True)
            if self.rb4 == 2:
                self.rb_d_4.setChecked(True)
            if self.rb4 == 3:
                self.rb_n_4.setChecked(True)
            if self.rb4 == 4:
                self.rb_a_4.setChecked(True)
            if self.rb4 == 5:
                self.rb_sa_4.setChecked(True)
                
            if self.rb5 == 1:
                self.rb_dn_5.setChecked(True)
            if self.rb5 == 2:
                self.rb_d_5.setChecked(True)
            if self.rb5 == 3:
                self.rb_n_5.setChecked(True)
            if self.rb5 == 4:
                self.rb_a_5.setChecked(True)
            if self.rb5 == 5:
                self.rb_sa_5.setChecked(True)
            if self.rb6 == 1:
                self.rb_dn_6.setChecked(True)
            if self.rb6 == 2:
                self.rb_d_6.setChecked(True)
            if self.rb6 == 3:
                self.rb_n_6.setChecked(True)
            if self.rb6 == 4:
                self.rb_a_6.setChecked(True)
            if self.rb6 == 5:
                self.rb_sa_6.setChecked(True)
            self.textEdit.setText(row[14])

            
##            sql = 'select c.course_name as Course, f1.fb_text Feedback1, \
##            f2.fb_text Feedback2, f3.fb_text Feedback3, f4.fb_text Feedback4, \
##            f5.fb_text Feedback5, oth_1 OtherCourses, oth_2 OtherCourses, \
##            oth_3 OtherCourses, oth_4 OtherCourses, oth_5 OtherCourses, fb_id1, fb_id2, fb_id3, fb_id4, fb_id5 \
##            from courses c, feedback f1, feedback f2, feedback f3, feedback f4, \
##            feedback f5 where c.fb_id1 = f1.fb_id and c.fb_id2 =f2.fb_id \
##            and c.fb_id3 = f3.fb_id and c.fb_id4 = f4.fb_id \
##            and c.fb_id5 = f5.fb_id and c.course_id = '+self.courseid
##            cursor.execute(sql)
##            row = cursor.fetchall()
##            row = row[0]
            
            self.lbl_1.setText(row[20])
            self.lbl_2.setText(row[21])
            self.lbl_3.setText(row[22])
            self.lbl_4.setText(row[23])
            self.lbl_5.setText(row[24])
            self.lbl_6.setText(row[25])
            cursor.execute("select st_full_name from student where st_id = "+self.stid)
            row = cursor.fetchall()
            row = row[0]
            self.lineEdit.setText(row[0])
            cursor.execute("select course_name from courses where course_id = "+self.courseid)
            row = cursor.fetchall()
            row = row[0]
            self.lineEdit_2.setText(row[0])
            
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
            self.mode = "a"
            return False
        self.hide()
    
#    def retrieve(self):
#        try:
#            cursor = self.conn.cursor()
#            cursor.execute("select course_id, course_name from courses")
#            row = cursor.fetchall()
#            for i in row:
#                a = i
#                for i in a:
#                    if str(i).isdigit():
#                        digit = i
#                    else:
#                        mystr = str(digit) + " : " + str(i)
#                        self.comboBox.addItem(mystr)
#        except sqlite3.Error as e:
#            QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
#            self.mode = "a"
#            return False
#        self.conn.commit()

    def save(self):
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
        
        
        try:
            cursor = self.conn.cursor()
            #print(self.f1, self.f2, self.f3, self.f4, self.f5, self.f6)
            if len(str(self.f6)) > 0:
                upd1="UPDATE st_feedback set fb_rating1 = "+str(self.f1)+", fb_rating2 = "+str(self.f2)+\
                ", fb_rating3 = "+str(self.f3)+", fb_rating4 = "+str(self.f4)+", fb_rating5 = "+str(self.f5)+ \
                ", fb_rating6 = "+str(self.f6)+", comments = '"+str(self.textEdit.toPlainText())+\
                "' where course_id = "+str(self.courseid)+" and st_id ="+str(self.stid)
            else:
                upd1="UPDATE st_feedback set fb_rating1 = "+str(self.f1)+", fb_rating2 = "+str(self.f2)+\
                ", fb_rating3 = "+str(self.f3)+", fb_rating4 = "+str(self.f4)+", fb_rating5 = "+str(self.f5)+ \
                ", comments = '"+str(self.textEdit.toPlainText())+"' where course_id = "+str(self.courseid)+" and st_id ="+str(self.stid)
                
            cursor.execute(upd1)
            #upd2="UPDATE st_feedback set comments = '"+str(self.textEdit.toPlainText())+"' where course_id = "+str(self.courseid)+" and st_id ="+str(self.stid)
            #cursor.execute(upd2)
            self.conn.commit()
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self,  "An Error occurred:",  e.args[0])
            self.mode = "a"
            return False
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
        try:
            cursor = self.conn.cursor()
            text = self.comboBox.currentText()
            text.split(" : ")
            print("Text",text)
            self.id = text[0]
            sql = 'select c.course_name as Course, f1.fb_text Feedback1, \
            f2.fb_text Feedback2, f3.fb_text Feedback3, f4.fb_text Feedback4, \
            f5.fb_text Feedback5, oth_1 OtherCourses, oth_2 OtherCourses, \
            oth_3 OtherCourses, oth_4 OtherCourses, oth_5 OtherCourses, fb_id1, fb_id2, fb_id3, fb_id4, fb_id5 \
            from courses c, feedback f1, feedback f2, feedback f3, feedback f4, \
            feedback f5 where c.fb_id1 = f1.fb_id and c.fb_id2 =f2.fb_id \
            and c.fb_id3 = f3.fb_id and c.fb_id4 = f4.fb_id \
            and c.fb_id5 = f5.fb_id and c.course_id = '+self.id
            cursor.execute(sql)
            row = cursor.fetchall()
            row = row[0]

            self.lbl_1.setText(row[1])
            self.lbl_2.setText(row[2])
            self.lbl_3.setText(row[3])
            self.lbl_4.setText(row[4])
            self.lbl_5.setText(row[5])
            self.checkBox.setText(row[6])
            self.checkBox_2.setText(row[7])
            self.checkBox_3.setText(row[8])
            self.checkBox_4.setText(row[9])
            self.barn = []
            for i in range(11, 16):
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
    myWindow = STForm(None)
    myWindow.show()
    myWindow.setFixedSize(myWindow.size())
    app.exec_() 
