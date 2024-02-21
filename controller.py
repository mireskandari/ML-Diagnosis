import sys
import threading
from .gui.main.main import DiseaseWindow
from .gui.main_menu.main_menu import MainMenu
from .gui.storage.main.default_manager.default_manager import StorageWindow
from .gui.storage.main.add_item.add_item import ItemAdder
from .arduino import send_string, stepPerRevolution
from .gui.storage.main.timer.timer import TimerWindow
from PyQt5 import QtWidgets, QtGui, QtCore
"""
A Class For Handeling Multiple Windows In PyQt5 Using pyqtSignal
"""
class Controller:
    def __init__(self, DiseaseWindow, MainMenu, StorageWindow, ItemAdder, TimerWindow):
        self.TimerWindow = TimerWindow
        self.DiseaseWindow = DiseaseWindow
        self.MainMenu = MainMenu
        self.StorageWindow = StorageWindow
        self.ItemAdder = ItemAdder
    
    def connect_arduino(self, count_motor : list):
        print(str(count_motor[0] * stepPerRevolution) + str(count_motor[1]))
        send_string(str(count_motor[0] * stepPerRevolution) + str(count_motor[1])) 
    
    def show_disease(self):
        self.disease_win = self.DiseaseWindow()
        self.disease_win.show()
        
    def show_main_menu(self):
        self.main_menu = self.MainMenu()
        self.main_menu.open_disease.connect(self.show_disease)
        self.main_menu.open_storage.connect(self.show_storage)
        self.main_menu.show()
    
    def show_storage(self):
        self.storage_win = self.StorageWindow()
        self.storage_win.open_item_add.connect(self.show_item_adder)
        self.storage_win.degree_signal.connect(self.connect_arduino)
        self.storage_win.open_set_timer.connect(self.show_timer_window)
        self.storage_win.show()
    
    def add_item_to_storage(self, items):
        self.storage_win.available_med.clear()
        for i in range(len(items)):
            if items[i] not in self.storage_win.medicine:
                self.storage_win.medicine.append(items[i])
                
        names = [item[1] for item in self.storage_win.medicine]
        self.storage_win.available_med.addItems(names)

    def show_timer_window(self):
        self.timer_win = self.TimerWindow()
        self.timer_win.show()
        
    def show_item_adder(self):
        self.item_adder = self.ItemAdder()
        self.item_adder.added_items.connect(self.add_item_to_storage)
        self.item_adder.show()
    
##    def add_med_timer(self,med_storage, med_count, med_interval):
##        timers.append(threading.Timer(med_interval, connect_arduino,
##                                      args=([med_count * stepPerRevolution,
##                                             med_storage],)))
##        timers[-1].start()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    c = Controller(DiseaseWindow, MainMenu, StorageWindow, ItemAdder, TimerWindow)
    c.show_main_menu()
    sys.exit(app.exec())
