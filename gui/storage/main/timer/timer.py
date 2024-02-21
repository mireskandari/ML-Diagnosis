from PyQt5 import QtWidgets, QtCore, QtGui

from .....gui.storage.main.timer.timer_generated import Ui_Form
from .....gui.frame.gui_frame import MyFrame

class TimerWindow(QtWidgets.QWidget, Ui_Form):
    interval_signal = QtCore.pyqtSignal(list)
    interval = []
    
    def __init__(self):
        super(TimerWindow, self).__init__(None)
        self.setupUi(self)
        self.layout  = QtWidgets.QVBoxLayout()
        self.main_frame = MyFrame(self)
        self.main_frame.title.setText("Set Time :)))")
        self.main_frame.setFixedWidth(self.width())
        self.layout.addWidget(self.main_frame)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.select_all.clicked.connect(self.select_all_clicked)

    @QtCore.pyqtSlot()
    def select_all_clicked(self):
        self.sat.setChecked(True)
        self.sun.setChecked(True)
        self.mon.setChecked(True)
        self.tue.setChecked(True)
        self.wed.setChecked(True)
        self.thu.setChecked(True)
        self.fri.setChecked(True)

    def closeEvent(self, event):
        sat = self.sat.isChecked()
        sun = self.sun.isChecked()
        mon = self.mon.isChecked()
        tue = self.tue.isChecked()
        wed = self.wed.isChecked()
        thu = self.thu.isChecked()
        fri = self.fri.isChecked()

        hour = int(self.hour.text())
        minute = int(self.minute.text())
        total = hour*3600 + minute*60
        
        interval = [sat, sun, mon, tue, wed, thu, fri]
        for day in interval:
            if day:
                self.interval.append(total)
            else:
                self.interval.append(None)
                
        self.interval_signal.emit(self.interval)
