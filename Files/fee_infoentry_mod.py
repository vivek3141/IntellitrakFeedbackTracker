import sys
from PyQt4 import QtCore, QtGui, uic
from fee_infoentry_auto import *
from student_mod import *
from batch_mod import *
class FeesInfo(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.conn=sqlite3.connect("Feedback.db")
        self.conn.commit()
        QtCore.QObject.connect(self.btn_select, QtCore.SIGNAL("clicked()"), self.callST)
        QtCore.QObject.connect(self.btn_selectb, QtCore.SIGNAL("clicked()"), self.callBT)
        
        QtCore.QObject.connect(self.btn_ok, QtCore.SIGNAL("clicked()"), self.save)
        QtCore.QObject.connect(self.btn_clear, QtCore.SIGNAL("clicked()"), self.clearAll)
        
        self.retval=0
        self.stid = 0
        self.btid = 0

        self.btn_ok.setEnabled(False)
        self.btn_select.setEnabled(False)

        self.setbutton = 0
    def keyPressEvent(self,e):
        if e.key() == QtCore.Qt.Key_F1:
            self.callST()
        if e.key() == QtCore.Qt.Key_F2:
            self.callBT()

    def clearAll(self):
        self.check()
        self.btn_select.setEnabled(False)
        #clear all Line & Text edits
        print("clearing ALL")
        self.lne_fname.clear()
        self.lne_bname.clear()
        self.lne_adue.clear()
        self.lne_apaid.clear()
        self.lne_comments.clear()


    def callST(self):
        #open Table View Student
        a = Student()
        self.retval = a.getStName('B', self.btid)
        if self.retval == "":
              return False
        if self.retval !="":
          self.insertValS(self.retval)

    def callBT(self):
        #open Table View Batch
        a = Batch()
        self.retval = a.getBtName()
        if self.retval == "":
              return False
        if self.retval !="":
          self.insertValB(self.retval)
          self.btn_select.setEnabled(True)

    def insertValS(self,stid):
        #Insert student's name
        try:
          cursor=self.conn.cursor()
          self.stid=stid
          cursor.execute("SELECT st_full_name from student where st_id="+str(self.stid))
          row=cursor.fetchall()
          print(row)
          if len(row) == 0:
            QtGui.QMessageBox.information(self, "Not Found!!!", "There were no records found")
            return False
          else:
            fname = ''.join(row[0])
            self.lne_fname.setText(fname)
          self.setbutton = 1

        except sqlite3.Error as e:
          QtGui.QMessageBox.information(self, " An error occured",e)
          self.check()
        self.insertCheck()

    def insertValB(self,btid):
        #Insert Batch Name 
        try:
          cursor=self.conn.cursor()
          self.btid=btid
          cursor.execute("SELECT course_id from batch where batch_id="+str(self.btid))
          row=cursor.fetchall()
          print(row)
          if len(row) == 0:
            QtGui.QMessageBox.information(self, "Not Found!!!", "There were no records found")
            return False
          else:
            cid = str(row[0]) #making string of tuple
            cid = cid[:-2]  #removing "," and ")" of tuple
            cid = cid[::-1]  #making word opposite
            cid = cid[:-1]  #removing "("
            cid = cid[::-1] #making word back to normal
            print("CID ="+cid)
            try:
                cursor=self.conn.cursor()
                cursor.execute("SELECT course_name from courses where course_id="+cid)
                row=cursor.fetchall()
                print(row)
                if len(row) == 0:
                    QtGui.QMessageBox.information(self, "Not Found!!!", "There were no records found")
                    return False
                else:
                    cname = ''.join(row[0])
                    self.lne_bname.setText("Batch "+str(btid)+", "+cname)

            except sqlite3.Error as e:
              QtGui.QMessageBox.information(self, " An error occured",e)
            self.setbutton = 2
    
        except sqlite3.Error as e:
          QtGui.QMessageBox.information(self, " An error occured",e)
        self.check()

    def check(self):
        #To make sure Student and Batch ID were entered before saving
        if self.setbutton == 2:
            self.btn_ok.setEnabled(True)
        else:
            self.btn_ok.setEnabled(False)

    def insertCheck(self):
        try:
          cursor=self.conn.cursor()
          cursor.execute("SELECT fees_due, fees_paid, amount_comment from st_batch_link where st_id="+str(self.stid)+" and batch_id="+str(self.btid))
          row=cursor.fetchall()
          print(row)
          if len(row) == 0:
            QtGui.QMessageBox.information(self, "Information", "This is going to be a new record ")
            return False
          else:
            for i in row:
              fdue,fpaid,acomments = i

            if ( fdue == None):
                fdue = ""
            if ( fpaid == None):
                fpaid = ""

            self.lne_adue.setText(str(fdue))
            self.lne_apaid.setText(str(fpaid))
            self.lne_comments.setText(acomments)
            
        except sqlite3.Error as e:
          QtGui.QMessageBox.information(self, " An error occured",e)

    def save(self):
        #save everything to Database
        name=self.lne_fname.text()
        bname=self.lne_bname.text()
        comments = self.lne_comments.toPlainText()
        print("Saving")
        amount1=self.lne_adue.text()
        #Validating Amount Due 
        try:
            amount1=int(amount1)
            if amount1>0 :
                pass
            else:
                QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThis is not a valid amount DUE. If you do not want to give this information, do not type anything in this field')
                return False
        except ValueError:
            if str(amount1)=='':
                amount1=0
            else:
                QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThis is not a valid amount DUE.\nIf you do not want to give this information, do not type anything in the field.')
                return False

        amount2=self.lne_apaid.text()
        #Validating Amount Paid
        
        try:
            amount2=int(amount2)
        except ValueError:
            QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThis is not a valid amount PAID.')
            return False
        
        try:
            newcursor=self.conn.cursor()
            mysql='UPDATE st_batch_link SET comments = "" , active_flag ="Y" , fees_due = '+str(amount1)+' , fees_paid = '+str(amount2)+' ,amount_comment = "'+str(comments) +'" where st_id = '+str(self.stid)+' and batch_id = '+str(self.btid)
            newcursor.execute(mysql)
            self.conn.commit()
            QtGui.QMessageBox.information(self,"Record updated", "Your information was updated.")
            self.setbutton=0
            self.clearAll()
        except sqlite3.Error as e:
            QtGui.QMessageBox.information(self, "ERROR", e.args[0])
            self.conn.commit()


if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = FeesInfo(None)
    myWindow.show()
    app.exec_()
