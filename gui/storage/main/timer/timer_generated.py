# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 322)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color : white;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.hour = QtWidgets.QSpinBox(Form)
        self.hour.setGeometry(QtCore.QRect(160, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hour.setFont(font)
        self.hour.setStyleSheet("background-color: rgb(255, 199, 69);\n"
"color : rgb(0, 0, 0);")
        self.hour.setObjectName("hour")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 100, 31, 31))
        self.label_2.setObjectName("label_2")
        self.minute = QtWidgets.QSpinBox(Form)
        self.minute.setGeometry(QtCore.QRect(310, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.minute.setFont(font)
        self.minute.setStyleSheet("background-color: rgb(255, 199, 69);\n"
"color : rgb(0, 0, 0);")
        self.minute.setMaximum(60)
        self.minute.setObjectName("minute")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 105, 41, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sat = QtWidgets.QCheckBox(Form)
        self.sat.setGeometry(QtCore.QRect(50, 230, 81, 20))
        self.sat.setObjectName("sat")
        self.sun = QtWidgets.QCheckBox(Form)
        self.sun.setGeometry(QtCore.QRect(150, 230, 81, 20))
        self.sun.setObjectName("sun")
        self.mon = QtWidgets.QCheckBox(Form)
        self.mon.setGeometry(QtCore.QRect(250, 230, 81, 20))
        self.mon.setObjectName("mon")
        self.tue = QtWidgets.QCheckBox(Form)
        self.tue.setGeometry(QtCore.QRect(350, 230, 81, 20))
        self.tue.setObjectName("tue")
        self.wed = QtWidgets.QCheckBox(Form)
        self.wed.setGeometry(QtCore.QRect(450, 230, 91, 20))
        self.wed.setObjectName("wed")
        self.thu = QtWidgets.QCheckBox(Form)
        self.thu.setGeometry(QtCore.QRect(50, 260, 81, 20))
        self.thu.setObjectName("thu")
        self.fri = QtWidgets.QCheckBox(Form)
        self.fri.setGeometry(QtCore.QRect(150, 260, 81, 20))
        self.fri.setObjectName("fri")
        self.select_all = QtWidgets.QPushButton(Form)
        self.select_all.setGeometry(QtCore.QRect(420, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.select_all.setFont(font)
        self.select_all.setStyleSheet("background-color: rgb(255, 199, 69);\n"
"color : rgb(0, 0, 0);")
        self.select_all.setObjectName("select_all")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Get Every :"))
        self.label_2.setText(_translate("Form", "hour"))
        self.label_3.setText(_translate("Form", "minute"))
        self.label_4.setText(_translate("Form", "At Days :"))
        self.sat.setText(_translate("Form", "Saturday"))
        self.sun.setText(_translate("Form", "Sunday"))
        self.mon.setText(_translate("Form", "Monday"))
        self.tue.setText(_translate("Form", "Tuesday"))
        self.wed.setText(_translate("Form", "Wednesday"))
        self.thu.setText(_translate("Form", "Thursday"))
        self.fri.setText(_translate("Form", "Friday"))
        self.select_all.setText(_translate("Form", "Select All Days"))

