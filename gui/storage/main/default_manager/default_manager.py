from PyQt5 import QtCore, QtGui, QtWidgets
import time

from .....gui.storage.main.default_manager.default_manager_generated import Ui_Form
from .....gui.frame.gui_frame import MyFrame

class StorageWindow(QtWidgets.QWidget, Ui_Form):
    open_item_add = QtCore.pyqtSignal()
    open_set_timer = QtCore.pyqtSignal()
    degree_signal = QtCore.pyqtSignal(list)
    medicine = []
    
    def __init__(self):
        super(StorageWindow, self).__init__(None)
        self.setupUi(self)
        self.layout  = QtWidgets.QVBoxLayout()
        self.main_frame = MyFrame(self)
        self.main_frame.title.setText("Storage Manager :)))")
        self.main_frame.setFixedWidth(self.width())
        self.layout.addWidget(self.main_frame)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.add_med.clicked.connect(self.add_med_clicked)
        self.remove_med.clicked.connect(self.remove_med_clicked)
        self.remove_all.clicked.connect(self.remove_all_clicked)
        self.get_med.clicked.connect(self.get_med_clicked)
        self.set_timer.clicked.connect(self.set_timer_clicked)

    def closeEvent(self, event):
        self.medicine = []
        self.available_med.clear()
        
    @QtCore.pyqtSlot()
    def add_med_clicked(self):
        self.open_item_add.emit()
        
    @QtCore.pyqtSlot()
    def set_timer_clicked(self):
        self.open_set_timer.emit()
        
    @QtCore.pyqtSlot()
    def remove_med_clicked(self):
        # self.selected_item = self.available_med.item(self.available_med.currentItem())
        selected = self.available_med.currentRow()
        self.available_med.takeItem(selected)
        self.medicine.pop(selected)
        
    @QtCore.pyqtSlot()
    def remove_all_clicked(self):
        self.available_med.clear()
        self.medicine = []

    @QtCore.pyqtSlot()
    def get_med_clicked(self):
        selected = self.available_med.currentRow()
        motor = self.medicine[selected][0]
        self.degree_signal.emit([int(self.item_count.text()), motor])
