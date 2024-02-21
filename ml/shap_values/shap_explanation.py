import pickle

import pandas as pd
import numpy as np
import shap
from matplotlib import pyplot as plt
from shap import KernelExplainer
from sklearn.naive_bayes import MultinomialNB

shap.initjs()

with open(r'/home/mrskndri/Documents/Dev/Python/Projects & Repos/Machine Learning/Seminar/ml/pretrained-model_mnb.pkl', 'rb') as file:
    model = pickle.load(file)

train_data = pd.read_csv(r'/home/mrskndri/Documents/Dev/Python/Projects & Repos/Machine Learning/Seminar/ml/manual_data/Training.csv')
x_train = train_data[train_data.columns[:-1]]

# test_data = pd.read_csv(r'/home/mrskndri/Documents/Dev/Python/Projects & Repos/Machine Learning/Seminar/ml/manual_data/Testing.csv')
# x_test = test_data[test_data.columns[:-1]]

# explainer = KernelExplainer(model.predict_proba, x_train)
with open('/home/mrskndri/Documents/Dev/Python/Projects & Repos/Machine Learning/Seminar/ml/shap_values.pkl', 'rb') as val:
    shap_vals = pickle.load(val)

fig = shap.summary_plot(shap_vals, x_train, plot_type='bar', class_names=model.classes_, max_display=150, show=False)
plt.savefig('shapplt.png', bbox_inches='tight', pad_inches=2)
