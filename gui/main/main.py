import sys
from os import path

from PyQt5 import QtCore, QtGui, QtWidgets
from ..frame.gui_frame import MyFrame
from ...gui.main.gui import Ui_MainWindow
from ...ml import predict


SYMPTOMS = ('Abdominal pain', 'Abnormal menstruation', 'Acidity', 'Acute liver failure', 'Altered sensorium', 'Anxiety', 'Back pain',
            'Belly pain', 'Blackheads', 'Bladder discomfort', 'Blister', 'Blood in sputum', 'Bloody stool', 'Blurred and distorted vision',
            'Breathlessness', 'Brittle nails', 'Bruising', 'Burning micturition', 'Chest pain', 'Chills', 'Cold hands and feets', 'Coma',
            'Congestion', 'Constipation', 'Continuous feel of urine', 'Continuous sneezing', 'Cough', 'Cramps', 'Dark urine', 'Dehydration',
            'Depression', 'Diarrhoea', 'Dischromic  patches', 'Distention of abdomen', 'Dizziness', 'Drying and tingling lips',
            'Enlarged thyroid', 'Excessive hunger', 'Extra marital contacts', 'Family history', 'Fast heart rate', 'Fatigue', 
            'Fluid overload', 'Fluid overload.1', 'Foul smell of urine', 'Headache', 'High fever', 'Hip joint pain',
            'History of alcohol consumption', 'Increased appetite', 'Indigestion', 'Inflammatory nails', 'Internal itching',
            'Irregular sugar level', 'Irritability', 'Irritation in anus', 'Itching', 'Joint pain', 'Knee pain', 'Lack of concentration',
            'Lethargy', 'Loss of appetite', 'Loss of balance', 'Loss of smell', 'Malaise', 'Mild fever', 'Mood swings', 'Movement stiffness', 
            'Mucoid sputum', 'Muscle pain', 'Muscle wasting', 'Muscle weakness', 'Nausea', 'Neck pain', 'Nodal skin eruptions', 'Obesity',
            'Pain behind the eyes', 'Pain during bowel movements', 'Pain in anal region', 'Painful walking', 'Palpitations',
            'Passage of gases', 'Patches in throat', 'Phlegm', 'Polyuria', 'Prominent veins on calf', 'Puffy face and eyes',
            'Pus filled pimples', 'Receiving blood transfusion', 'Receiving unsterile injections', 'Red sore around nose',
            'Red spots over body', 'Redness of eyes', 'Restlessness', 'Runny nose', 'Rusty sputum', 'Scurring', 'Shivering',
            'Silver like dusting', 'Sinus pressure', 'Skin peeling', 'Skin rash', 'Slurred speech', 'Small dents in nails',
            'Spinning movements', 'Spotting  urination', 'Stiff neck', 'Stomach bleeding', 'Stomach pain', 'Sunken eyes', 'Sweating',
            'Swelled lymph nodes', 'Swelling joints', 'Swelling of stomach', 'Swollen blood vessels', 'Swollen extremeties', 'Swollen legs',
            'Throat irritation', 'Toxic look (typhos)', 'Ulcers on tongue', 'Unsteadiness', 'Visual disturbances', 'Vomiting',
            'Watering from eyes', 'Weakness in limbs', 'Weakness of onebody side', 'Weight gain', 'Weight loss', 'Yellow crust ooze',
            'Yellow urine', 'Yellowing of eyes', 'Yellowish skin')

#######################################################################
"""
The Main Window For Inputing Symptoms And Outputing Disease Prediction
"""
class DiseaseWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(DiseaseWindow, self).__init__(None)
        self.setupUi(self)
        self.layout  = QtWidgets.QVBoxLayout()
        self.main_frame = MyFrame(self)
        self.main_frame.title.setText("Disease Predictor :)))")
        self.layout.addWidget(self.main_frame)
        self.centralwidget.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.moreinfo_buttons = []
        self.predict_button.setCheckable(False)
        self.symptom_error.setHidden(True)
        self.symptom_error.setStyleSheet("QLabel { color : red; }")
        self.selected_symptoms_text.setStyleSheet("QTextBrowser{ border : 0;"
                                                  "background-color : transparent; }")
        self.setFixedSize(self.size())
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.symptoms.setFont(font)
        self.symptoms.addItems(SYMPTOMS)
        self.symptoms.setCurrentIndex(-1)
        header = self.prediction_table.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
##        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.symptoms.activated.connect(self.new_symptom_selected)
        self.predict_button.clicked.connect(self.predict_pushed)
        self.delete_last.clicked.connect(self.delete_last_pushed)
        self.delete_all.clicked.connect(self.delete_all_pushed)
        self.delete_table.clicked.connect(self.delete_table_pushed)
        
    
    # # overriding closeEvent to close info window before exiting main window if exists       
    # def closeEvent(self, event):
        # self.close_info_window.emit()
        
    @QtCore.pyqtSlot()
    def predict_pushed(self):
        # self.close_info_window.emit() # close open info windows first
        
        self.symptom_error.setHidden(True)
        self.prediction_table.setRowCount(0)
        query = self.selected_symptoms.toPlainText()
        
        if query != "":
            prediction = predict.predict_with_percent(query)
            
            for index, value in enumerate(prediction):
##                if round(value[1] * 100, 1) <= 2:
##                    continue
                
                percentage = str(round(value[1] * 100, 1)) + "%"
                self.prediction_table.insertRow(index)
                self.prediction_table.setItem(index, 0, QtWidgets.QTableWidgetItem(value[0].capitalize()))
                self.prediction_table.setItem(index, 1, QtWidgets.QTableWidgetItem(percentage))
                self.prediction_table.item(index, 0).setFlags(QtCore.Qt.ItemIsEnabled)
                self.prediction_table.item(index, 1).setFlags(QtCore.Qt.ItemIsSelectable)
                self.prediction_table.item(index, 1).setForeground(QtGui.QColor(0, 0, 0))
                
            #self.show_more_info_buttons()        
        else:
            self.symptom_error.setText("Select Symptoms First!")
            self.symptom_error.setHidden(False)
              
    @QtCore.pyqtSlot()
    def delete_table_pushed(self):
        self.prediction_table.setRowCount(0)
        
    @QtCore.pyqtSlot()
    def new_symptom_selected(self):
        self.prediction_table.setRowCount(0)
        current_text = self.selected_symptoms.toPlainText()
        selected = self.symptoms.currentText()
        
        if selected != '':

            if not(selected in current_text):
                self.symptom_error.setHidden(True)
                
                if current_text != "":
                    self.selected_symptoms.setPlainText(current_text + ", " + selected)
                else:
                    self.selected_symptoms.setPlainText(selected)
            
            else:
                self.symptom_error.setHidden(False)
            
    
    @QtCore.pyqtSlot()
    def delete_last_pushed(self):
        current_text = self.selected_symptoms.toPlainText()
        current_text = current_text.split(",")

        if len(current_text) <= 1:
            current_text = ""
        else:
            current_text = current_text[:-1]
            current_text = ",".join(current_text)
        
        self.selected_symptoms.setPlainText(current_text)

    @QtCore.pyqtSlot()
    def delete_all_pushed(self):
        self.selected_symptoms.setPlainText("")
        self.prediction_table.setRowCount(0)
    
    def show_more_info_buttons(self):
        # self.open_info_window.emit()
        pass
        
              
######################################################################
        
# if __name__ == "__main__":
    # app = QtWidgets.QApplication([]) 
    # c = Controller(MainWindow, InfoWindow)
    # c.show_main()

    # sys.exit(app.exec())
