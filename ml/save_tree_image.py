import pickle

import pandas as pd
import pydotplus
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz

with open(r'/home/mrskndri/Documents/Dev/Python/Projects & Repos/Machine Learning/Seminar/pretrained-model_dt.pkl', 'rb') as f:
    model = pickle.load(f)

data = pd.read_csv(r'/home/mrskndri/Documents/Dev/Python/Projects & Repos/Machine Learning/Seminar/ml/manual_data/Testing.csv')
features = data.columns[:-1]

dot_file = StringIO()
export_graphviz(model, dot_file, filled=True, 
                rounded=True, feature_names=features, class_names=model.classes_)
graph = pydotplus.graph_from_dot_data(dot_file.getvalue())
graph.write_png('dt_visual_.png')

