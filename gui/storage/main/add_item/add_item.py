from .....gui.storage.main.add_item.add_item_generated import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from .....gui.frame.gui_frame import MyFrame

class ItemAdder(QtWidgets.QWidget, Ui_Form):
    added_items = QtCore.pyqtSignal(list)
    written_items = []
    
    def __init__(self):
        super(ItemAdder, self).__init__(None)
        self.setupUi(self)
        self.layout  = QtWidgets.QVBoxLayout()
        self.main_frame = MyFrame(self)
        self.main_frame.title.setText("Add Item :)))")
        self.main_frame.setFixedWidth(self.width())
        self.layout.addWidget(self.main_frame)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.save_and_exit.clicked.connect(self.save_exit_clicked)
        self.save_and_add.clicked.connect(self.save_add_clicked)
    
    @QtCore.pyqtSlot()
    def save_add_clicked(self):
        selected_store = int(self.store_num.currentText())
        entered_drug = self.dru_name.toPlainText()
        self.written_items.append([selected_store, entered_drug])
        self.dru_name.setPlainText("")
    
    @QtCore.pyqtSlot()
    def save_exit_clicked(self):
        selected_store = int(self.store_num.currentText())
        entered_drug = self.dru_name.toPlainText()
        self.written_items.append([selected_store, entered_drug])
        self.dru_name.setPlainText("")
        self.added_items.emit(self.written_items)
        self.written_items = []
        self.close()
        
