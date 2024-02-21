from ...gui.main_menu.main_menu_generated import Ui_Form
from ...gui.frame.gui_frame import MyFrame

from PyQt5 import QtCore, QtWidgets, QtGui

class MainMenu(QtWidgets.QWidget, Ui_Form):
    open_disease = QtCore.pyqtSignal()
    open_storage = QtCore.pyqtSignal()
    
    def __init__(self):
        super(MainMenu, self).__init__(None)
        self.setupUi(self)
        
        self.layout  = QtWidgets.QVBoxLayout()
        self.main_frame = MyFrame(self)
        self.main_frame.title.setText("Main menu :)))")
        self.main_frame.setFixedWidth(self.width())
        self.layout.addWidget(self.main_frame)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.pushButton.clicked.connect(self.open_disease.emit)
        self.pushButton_2.clicked.connect(self.open_storage.emit)
        
        
        @QtCore.pyqtSlot()
        def open_disease_clicked(self):
            self.open_disease.emit()

        @QtCore.pyqtSlot()
        def open_storage_clicked(self):
            self.open_storage.emit()
