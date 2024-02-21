print("LOADING IMPORTS...\n")
import os
import pickle

import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score, train_test_split
# from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier

print("LOADING DATA...\n")
data = pd.read_csv(r"/home/mrskndri/Documents/Dev/Python/Projects & Repos/Machine Learning/Seminar/ml/manual_data/Training.csv")
cols = data.columns
cols = cols[:-1]

x = data[cols]
y = data['prognosis']

test_data = data = pd.read_csv(r"/home/mrskndri/Documents/Dev/Python/Projects & Repos/Machine Learning/Seminar/ml/manual_data/Testing.csv")
cols = test_data.columns
cols = cols[:-1]

x_test_true = test_data[cols]
y_test_true = test_data['prognosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=100)

pd.concat([x_test, x_test_true])
pd.concat([y_test, y_test_true])

print('TRAINING MODEL...\n')
model = DecisionTreeClassifier(criterion='entropy')
model.fit(x_train, y_train)


predicted = model.predict(x_test)
print(classification_report(y_test, predicted))

print('SAVING THE MODEL...\n')
with open('ml/pretrained-model_dt.pkl', 'wb') as m:
    pickle.dump(model, m)

with open('x_train.pkl', 'wb') as f:
    pickle.dump(x_train, f)

with open('y_train.pkl', 'wb') as f:
    pickle.dump(y_train, f)




