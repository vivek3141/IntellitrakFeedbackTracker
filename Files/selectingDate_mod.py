import sys
import datetime
from selectingDate_auto import *
class MyForm(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.val=''
        #self.ui.cal.clicked[QtCore.QDate].connect(self.showDate)
        QtCore.QObject.connect(self.ui.cal, QtCore.SIGNAL('selectionChanged()'), self.showDate)
        QtCore.QObject.connect(self.ui.btn_ok, QtCore.SIGNAL('clicked()'), self.returning)         
    def showDate(self):
        date = self.ui.cal.selectedDate()

        #setting date into a label
        self.ui.val=date.toString()[3:]
        self.ui.lbl_date.setText(self.ui.val)

    def returning(self):
        self.close()

    def getMeDate(self):
        dialog=MyForm()
        result=dialog.exec_()
        if result==1:
            return dialog.ui.val
        else:
            return ""


#this is where we will bind the event handlers
#This is where we will insert the functions (defs)
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())
