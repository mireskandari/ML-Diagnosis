print("LOADING IMPORTS...\n")
import os
import pickle

import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
# from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB

print("LOADING DATA...\n")
data = pd.read_csv(r"/home/mrskndri/Documents/Dev/Python/Projects & Repos/Machine Learning/Seminar/ml/manual_data/Training.csv")
cols = data.columns
cols = cols[:-1]

x = data[cols]
x = np.array(x)
y = data['prognosis']

print('TRAINING MODEL...\n')
model = MultinomialNB()
model.fit(x, y)

print('SAVING THE MODEL...\n')
with open('pretrained-model_mnb.pkl', 'wb') as m:
    pickle.dump(model, m)




