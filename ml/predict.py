import pickle

import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB


def read_model():
    m = open(r"E:\Education\Dev\Python\Projects & Repos\Machine Learning\Seminar\ml\pretrained-model_mnb.pkl", 'rb')
    model = pickle.load(m)
    m.close()
    return model

def read_data():
    return pd.read_csv(r"E:\Education\Dev\Python\Projects & Repos\Machine Learning\Seminar\ml\manual_data\Training.csv")

def find_symptoms_col(symptoms, data):
    cols = data[data.columns[:-1]]
    features = cols

    symptoms_index = []
    for i, f in enumerate(features):
        for symptom in symptoms:
            if f == symptom:
                symptoms_index.append(i)
    
    return symptoms_index

def find_prob_disease(p, classes):
    return [(disease, p[i]) for i, disease in np.ndenumerate(classes)]

def predict_with_percent(symptoms):
    symptoms = symptoms.split(",")
    symptoms = [i.lstrip().rstrip().replace(" ", "_").lower() for i in symptoms]

    data = read_data()
    symptoms_index = find_symptoms_col(symptoms, data)
    symptoms = [0 if i not in symptoms_index else 1 for i in range(132)]
    symptoms = np.array(symptoms).reshape(1, len(symptoms))

    model = read_model()
    pred = model.predict_proba(symptoms)[0]
    pred = find_prob_disease(pred, model.classes_)

    return sorted(pred, key=lambda x:x[1], reverse=True)
