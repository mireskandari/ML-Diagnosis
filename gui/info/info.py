# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InfoWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.info = QtWidgets.QTabWidget(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(20, 20, 761, 561))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.info.setFont(font)
        self.info.setStyleSheet("")
        self.info.setTabPosition(QtWidgets.QTabWidget.North)
        self.info.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.info.setIconSize(QtCore.QSize(20, 20))
        self.info.setElideMode(QtCore.Qt.ElideNone)
        self.info.setUsesScrollButtons(True)
        self.info.setDocumentMode(True)
        self.info.setTabsClosable(False)
        self.info.setMovable(False)
        self.info.setTabBarAutoHide(False)
        self.info.setObjectName("info")
        self.description_tab = QtWidgets.QWidget()
        self.description_tab.setObjectName("description_tab")
        self.description_text = QtWidgets.QTextBrowser(self.description_tab)
        self.description_text.setGeometry(QtCore.QRect(0, 0, 761, 511))
        self.description_text.setObjectName("description_text")
        self.info.addTab(self.description_tab, "")
        self.symptoms_tab = QtWidgets.QWidget()
        self.symptoms_tab.setObjectName("symptoms_tab")
        self.symptoms_text = QtWidgets.QTextBrowser(self.symptoms_tab)
        self.symptoms_text.setGeometry(QtCore.QRect(0, 0, 761, 511))
        self.symptoms_text.setObjectName("symptoms_text")
        self.info.addTab(self.symptoms_tab, "")
        self.prevention_tab = QtWidgets.QWidget()
        self.prevention_tab.setObjectName("prevention_tab")
        self.prevention_text = QtWidgets.QTextBrowser(self.prevention_tab)
        self.prevention_text.setGeometry(QtCore.QRect(0, 0, 761, 511))
        self.prevention_text.setObjectName("prevention_text")
        self.info.addTab(self.prevention_tab, "")
        self.treatment_tab = QtWidgets.QWidget()
        self.treatment_tab.setObjectName("treatment_tab")
        self.treatment_text = QtWidgets.QTextBrowser(self.treatment_tab)
        self.treatment_text.setGeometry(QtCore.QRect(0, 0, 761, 511))
        self.treatment_text.setObjectName("treatment_text")
        self.info.addTab(self.treatment_tab, "")
        self.diagnosis_tab = QtWidgets.QWidget()
        self.diagnosis_tab.setObjectName("diagnosis_tab")
        self.diagnosis_text = QtWidgets.QTextBrowser(self.diagnosis_tab)
        self.diagnosis_text.setGeometry(QtCore.QRect(0, 0, 761, 511))
        self.diagnosis_text.setObjectName("diagnosis_text")
        self.info.addTab(self.diagnosis_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.info.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "InfoWindow"))
        self.info.setTabText(self.info.indexOf(self.description_tab), _translate("MainWindow", "Description"))
        self.info.setTabText(self.info.indexOf(self.symptoms_tab), _translate("MainWindow", "Symptoms"))
        self.info.setTabText(self.info.indexOf(self.prevention_tab), _translate("MainWindow", "Transmission - Prevention"))
        self.info.setTabText(self.info.indexOf(self.treatment_tab), _translate("MainWindow", "Treatment"))
        self.info.setTabText(self.info.indexOf(self.diagnosis_tab), _translate("MainWindow", "Diagnosis"))

