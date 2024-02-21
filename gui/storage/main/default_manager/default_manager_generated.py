# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default_manager.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(892, 654)
        Form.setStyleSheet("\n"
"background-color: rgb(40, 40, 40);\n"
"color : white;")
        self.available_med = QtWidgets.QListWidget(Form)
        self.available_med.setGeometry(QtCore.QRect(50, 210, 591, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.available_med.setFont(font)
        self.available_med.setStyleSheet("background-color: rgb(255, 199, 69);\n"
"selection-background-color: rgb(193, 52, 28);\n"
"color : black;\n"
"")
        self.available_med.setObjectName("available_med")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 110, 271, 31))
        self.label.setObjectName("label")
        self.add_med = QtWidgets.QPushButton(Form)
        self.add_med.setGeometry(QtCore.QRect(670, 210, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add_med.setFont(font)
        self.add_med.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : black;")
        self.add_med.setObjectName("add_med")
        self.remove_med = QtWidgets.QPushButton(Form)
        self.remove_med.setGeometry(QtCore.QRect(670, 260, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.remove_med.setFont(font)
        self.remove_med.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : black;")
        self.remove_med.setObjectName("remove_med")
        self.remove_all = QtWidgets.QPushButton(Form)
        self.remove_all.setGeometry(QtCore.QRect(670, 310, 191, 41))
        self.remove_all.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : black;")
        self.remove_all.setObjectName("remove_all")
        self.get_med = QtWidgets.QPushButton(Form)
        self.get_med.setGeometry(QtCore.QRect(670, 500, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.get_med.setFont(font)
        self.get_med.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : rgb(0, 0, 0);\n"
"")
        self.get_med.setObjectName("get_med")
        self.item_count = QtWidgets.QSpinBox(Form)
        self.item_count.setGeometry(QtCore.QRect(670, 580, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_count.setFont(font)
        self.item_count.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : rgb(0, 0, 0);")
        self.item_count.setObjectName("item_count")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(670, 550, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.set_timer = QtWidgets.QPushButton(Form)
        self.set_timer.setGeometry(QtCore.QRect(670, 360, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.set_timer.setFont(font)
        self.set_timer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : black;")
        self.set_timer.setObjectName("set_timer")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">List Of Available Medicine:</span></p></body></html>"))
        self.add_med.setText(_translate("Form", "Add Medicine to Storage"))
        self.remove_med.setText(_translate("Form", "Remove Medicine From Storage"))
        self.remove_all.setText(_translate("Form", "Remove All"))
        self.get_med.setText(_translate("Form", "Get Selected Item"))
        self.label_2.setText(_translate("Form", "Item Count :"))
        self.set_timer.setText(_translate("Form", "Set Timer On Selected Item"))

