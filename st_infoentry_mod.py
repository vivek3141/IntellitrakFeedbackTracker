import sys
import sqlite3
import datetime as dt
from PyQt4 import QtCore, QtGui, uic
from st_modify_auto import *
import selectingDate_mod 

class STInfoEntry(QtGui.QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    QtGui.QMainWindow.__init__(self, parent)
    self.setupUi(self)
    self.label_13.hide()
    self.btn_select.hide()

    self.conn= sqlite3.connect("feedback.db")
    #this is where we will bind the event handlers
    QtCore.QObject.connect(self.btn_clear, QtCore.SIGNAL('clicked()'), self.clearAll)
    QtCore.QObject.connect(self.btn_save,QtCore.SIGNAL('clicked()'), self.save)
    QtCore.QObject.connect(self.btn_date,QtCore.SIGNAL('clicked()'), self.openCalendar)
    QtCore.QObject.connect(self.btn_keep,QtCore.SIGNAL('clicked()'), self.keep)
    #This is where we will insert the functions (defs)

    self.lne_date.setText(dt.datetime.today().strftime("%b %d, %Y"))

  def keyPressEvent(self,e):
        if e.key() == QtCore.Qt.Key_F10:
            self.keep()

  def keep(self):
    self.lne_fname.clear()
    self.lne_date.setText(dt.datetime.today().strftime("%b %d, %Y"))
    self.lne_pphone.clear()
    self.lne_pemail.clear()
    self.lne_pname.clear()
    self.lne_sphone.clear()
    self.lne_semail.clear()
    self.lne_grade.clear()
    
    
  def clearAll(self):
    print("clearing ALL")
    self.lne_fname.clear()
    self.lne_date.setText(dt.datetime.today().strftime("%b %d, %Y"))
    self.lne_pphone.clear()
    self.lne_pemail.clear()
    self.lne_pname.clear()
    self.lne_sphone.clear()
    self.lne_semail.clear()
    self.lne_grade.clear()
    self.lne_address_1.clear()
    self.lne_address_2.clear()
    self.lne_zip.clear()

  def save(self):
    print("Saving")

#VALIDATION

#########full name###########################

    fname=self.lne_fname.text()
    fname=fname.capitalize()
    space=fname.find(' ')
    if space==-1:
      QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tYour full name please.')
      return False

#########date################################
    date=self.lne_date.text()
    
#############student email##########################
    semail=self.lne_semail.text()

    vari=semail.find('@')
    able=semail.find('.')

    if semail=="":
      pass
    elif vari == -1:
      QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThe email id given is not proper.\n If you do not want to give this information, do not type anything in the field.')
      return False
    elif able!=-1:
      if able<vari :
        if semail[vari:].find(".")== -1:
          QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThe email id given is not proper.\nIf you do not want to give this information, do not type anything in the field.')
          return False
        else:
          pass
      else:
        pass
    elif able==-1:
      QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThe email id given is not proper.\nIf you do not want to give this information, do not type anything in the field.')
      return False
    else:
      pass
#############student phone#######################      

    sphone=self.lne_sphone.text()
    try:
      int(sphone)
      if len(str(int(sphone)))!=10:
        QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tA valid mobile number should have 10 digits.\nIf you do not want to give this information, do not type anything in the field.')
        return False
    except ValueError:
      if sphone=="":
        pass
      else:
        QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tA valid mobile number is an integer.\nIf you do not want to give this information, do not type anything in the field.')
        return False
#############grade##########################
    grade=self.lne_grade.text()
    try:
      grade=int(grade)

      if grade>12 or grade<1 :
        QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThis is not a valid grade.\nIf you do not want to give this information, do not type anything in the field.')
        return False
      else:
        pass
    
    except ValueError:
      if str(grade)=='':
        pass
      else:
        QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThis is not a valid grade.\nIf you do not want to give this information, do not type anything in the field.')
        return False

###############parent phone#####################
    pphone=self.lne_pphone.text()
    try:
      int(pphone)
      if len(pphone)!=10:
        QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tA valid mobile number should have 10 digits.\nIf you do not want to give this information, do not type anything in the field.')
        return False
    except ValueError:
      if pphone=="":
        pass
      else:
        QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tA valid mobile number is an integer.\nIf you do not want to give this information, do not type anything in the field.')
        return False
################parent email#######################
    pemail=self.lne_pemail.text()

    vari=pemail.find('@')
    able=pemail.rfind('.')

    if pemail=="":
      pass
    elif vari == -1:
      QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThe email id given is not proper.\n If you do not want to give this information, do not type anything in the field.')
      return False
    elif able!=-1:
      if able<vari :
        QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThe email id given is not proper.\nIf you do not want to give this information, do not type anything in the field.')
        return False
      else:
        pass
    elif able==-1:
      QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThe email id given is not proper.\nIf you do not want to give this information, do not type anything in the field.')
      return False
    else:
      pass
###########parent name########################

    pname=self.lne_pname.text()

###############address lines##################
      
    al1=self.lne_address_1.toPlainText()
    al2=self.lne_address_2.toPlainText()

#############zip code###################

    zipno=self.lne_zip.text()
    try:
      int(zipno)
      if len(zipno)!=6:
        QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThe zip given is not proper.\n If you do not want to give this information, do not type anything in the field.')
        return False
    except ValueError:
      if zipno=='':
        pass
      else:
        QtGui.QMessageBox.about(self,"Wrong Input",'Sorry,\n\tThe zip given is not proper.\n If you do not want to give this information, do not type anything in the field.')
        return False


#VALIDATION OVER
#INSERTING INTO DATABASE

    try:

      cursor=self.conn.cursor()
      cursor.execute("INSERT INTO student(st_date_of_joining, st_full_name, st_grade, st_parent_name, st_parent_phone, st_parent_email, st_phone, st_email, st_address_1, st_address_2, st_zip)\
                      VALUES (?,?,?,?,?,?,?,?,?,?,?)", (date, fname, grade, pname, pphone, pemail, sphone, semail, al1, al2, zipno))
      self.conn.commit()
      QtGui.QMessageBox.information(self, "Record saved", "Your information was submitted.")
      self.clearAll()
    except sqlite3.Error as e:
      QtGui.QMessageBox.information(self, "ERROR", e.args[0])

    
  def openCalendar(self):
    #CALLING CALENDAR WINDOW
    cal=selectingDate_mod.MyForm(self)
    #getMeDate IS FUNCTION IN selectingDate_mod THAT USES accept() AND reject() SINGAL SLOTS
    retval=cal.getMeDate()
    if retval !="":
      self.lne_date.setText(retval)
    

    
        
if (__name__ == "__main__"):
        
    app = QtGui.QApplication(sys.argv)
    myWindow = STInfoEntry(None)
    myWindow.show()
    app.exec_()
