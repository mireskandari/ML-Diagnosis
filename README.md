# ML-Diagnosis

**A Python GUI App Predicting Medical Diagnosis Based on User Symptoms Using Naive Bayes Classifier**

## Overview

ML-Diagnosis is a Python-based graphical user interface (GUI) application designed to predict medical diagnoses based on user-provided symptoms. This application leverages a Naive Bayes classifier trained on real medical data to provide the most probable diagnosis.

## Motivation

My dual interest in biology and programming culminated in the development of the Mini Medical Center project, which includes ML-Diagnosis and a pill dispenser device with my team.

## Project Components

### 1. AI Diagnosis Application

The AI diagnosis application is the core component of the Mini Medical Center project. It includes the following features:

- **Symptom Input:** Users can input their symptoms through a user-friendly GUI.
- **Prediction Algorithm:** The application utilizes a Naive Bayes classifier to predict the most likely medical diagnosis based on the input symptoms.
- **Training Data:** The classifier is trained on a dataset collected from hospitals, ensuring the predictions are based on real-world medical data.

### 2. Pill Dispenser Device

The pill dispenser is a hardware component designed to dispense pills based on a timer set by the user. Key features include:

- **Timer Functionality:** Users can set a timer for pill dispensing, ensuring timely medication management.
- **Integration with AI Application:** The dispenser can work in conjunction with the AI diagnosis application to suggest medication based on the diagnosis.

## Technical Details

### AI Model

- **Algorithm:** Naive Bayes classifier from the scikit-learn library
- **Training Data:** Real medical data from hospitals
- **Data Processing:** Utilized the pandas library for data processing and preparation
- **Features:** Symptoms input by users
- **Labels:** Medical diagnoses
- **Implementation Steps:**
  1. **Data Cleaning:** Cleaned and preprocessed the dataset using pandas.
  2. **Feature Extraction:** Extracted relevant features from the symptoms data.
  3. **Model Training:** Trained the Naive Bayes classifier using the processed data.
  4. **Evaluation:** Evaluated the model's performance using standard metrics (e.g., accuracy, precision, recall).

### GUI

- **Framework:** PyQt
- **Design:** An event-based basic window with minimal components, implemented in Python. The GUI allows users to enter symptoms and receive a diagnosis prediction and also allows the user to set 2 timers for each of the pill present in the device's storage.

### Pill Dispenser

- **Hardware:** Arduino UNO R3
- **Programming:** Arduino programming language
- **Communication:** The Arduino communicates with the GUI application using the PySignal framework and a USB connection.
- **Functionality:** The dispenser releases pills based on a timer set by the user through the GUI.
