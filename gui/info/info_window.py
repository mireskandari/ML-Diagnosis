import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.info import Ui_InfoWindow

###########################################################
"""
The Window For Displaying Diseases Information Including Treatment And ...
"""
class InfoWindow(QtWidgets.QMainWindow, Ui_InfoWindow):
    
    def __init__(self, disease):
        super(InfoWindow, self).__init__(None)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setStyleSheet("QTextBrowser{ border: 0; }")
        self.texts = (self.description_text,
                      self.symptoms_text,
                      self.prevention_text,
                      self.treatment_text,
                      self.diagnosis_text)
        
        self.disease = disease
        self.show_info()
    
    def show_info(self):
        for text in self.texts:
            text.setText("")
    
    def get_info(self):
        pass
    
    
#############################################################
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = InfoWindow("")
    win.show()
    sys.exit(app.exec())

