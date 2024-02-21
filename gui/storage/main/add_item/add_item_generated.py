# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_item.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(467, 292)
        Form.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color : white;")
        self.dru_name = QtWidgets.QTextEdit(Form)
        self.dru_name.setGeometry(QtCore.QRect(40, 170, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dru_name.setFont(font)
        self.dru_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : rgb(0, 0, 0);")
        self.dru_name.setAcceptRichText(False)
        self.dru_name.setObjectName("dru_name")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.store_num = QtWidgets.QComboBox(Form)
        self.store_num.setGeometry(QtCore.QRect(40, 100, 91, 31))
        self.store_num.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : rgb(0, 0, 0);")
        self.store_num.setObjectName("store_num")
        self.store_num.addItem("")
        self.store_num.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.save_and_exit = QtWidgets.QPushButton(Form)
        self.save_and_exit.setGeometry(QtCore.QRect(40, 240, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.save_and_exit.setFont(font)
        self.save_and_exit.setStyleSheet("background-color: rgb(255, 199, 69);\n"
"color : rgb(0, 0, 0);")
        self.save_and_exit.setObjectName("save_and_exit")
        self.save_and_add = QtWidgets.QPushButton(Form)
        self.save_and_add.setGeometry(QtCore.QRect(240, 240, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.save_and_add.setFont(font)
        self.save_and_add.setStyleSheet("background-color: rgb(255, 199, 69);\n"
"color : rgb(0, 0, 0);")
        self.save_and_add.setObjectName("save_and_add")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Drug Name"))
        self.store_num.setItemText(0, _translate("Form", "1"))
        self.store_num.setItemText(1, _translate("Form", "2"))
        self.label_2.setText(_translate("Form", "Storage Number"))
        self.save_and_exit.setText(_translate("Form", "Save And Exit"))
        self.save_and_add.setText(_translate("Form", "Save And Add New"))

