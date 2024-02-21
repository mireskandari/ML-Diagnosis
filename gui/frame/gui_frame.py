from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui, QtWidgets, QtCore

class Ui_Form(object):
    def setupUi(self, Form):
        self.btn_height = 42
        self.btn_width = 60
        self.font_size = 12
        Form.setObjectName("Form")
        Form.resize(970, 50)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("")
        Form.setFont(font)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 971, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout.setContentsMargins(0, 0, 2, 0)
        self.layout.setObjectName("layout")
        self.title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.title.setMaximumSize(QtCore.QSize(16777215, 48))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.title.setFixedHeight(48)
        self.title.setFont(font)
        self.layout.addWidget(self.title)
        self.min_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.min_btn.setMinimumSize(QtCore.QSize(self.btn_width, self.btn_height))
        font = QtGui.QFont()
        font.setPointSize(self.font_size)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.min_btn.setFont(font)
        self.min_btn.setFlat(False)
        self.min_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : rgb(0, 0, 0);"
"border : none;")
        self.min_btn.setObjectName("min_btn")
        self.layout.addWidget(self.min_btn)
        self.max_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.max_btn.setMinimumSize(QtCore.QSize(self.btn_width, self.btn_height))
        font = QtGui.QFont()
        font.setPointSize(self.font_size)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.max_btn.setFont(font)
        self.max_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : rgb(150, 150, 150);"
"border : none;")
        self.max_btn.setAutoDefault(False)
        self.max_btn.setDefault(False)
        self.max_btn.setFlat(False)
        self.max_btn.setObjectName("max_btn")
        self.layout.addWidget(self.max_btn)
        self.close_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.close_btn.setMinimumSize(QtCore.QSize(self.btn_width, self.btn_height))
        font = QtGui.QFont()
        font.setPointSize(self.font_size)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.close_btn.setFont(font)
        self.close_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : rgb(0, 0, 0);"
"border : none;")
        self.close_btn.setObjectName("close_btn")
        self.layout.addWidget(self.close_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.min_btn.setText(_translate("Form", "-"))
        self.max_btn.setText(_translate("Form", "\u25a0"))
        self.close_btn.setText(_translate("Form", "X"))
        
class MyFrame(QWidget, Ui_Form):

    def __init__(self, parent):
        super(MyFrame, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.title.setStyleSheet("""
        background-color : rgb(31, 31, 31);
        color : white;
        font-size : 12px;""")
        self.setLayout(self.layout)
        
        self.start = QPoint(0, 0)
        self.pressing = False
        self.close_btn.clicked.connect(self.btn_close_clicked)
        self.min_btn.clicked.connect(self.btn_min_clicked)
        self.max_btn.setEnabled(False)
        
    def resizeEvent(self, QResizeEvent):
        super(MyFrame, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.parent.close()

    def btn_max_clicked(self):
        self.parent.showMaximized()

    def btn_min_clicked(self):
        self.parent.showMinimized()
