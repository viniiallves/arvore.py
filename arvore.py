import pandas as import pd
import numpy as np
from sklearn as tree

train = pd.read.csv ()
y_train = train ()
x_train = train.drop ([], axis=1).values
decision_tree = tree.DecisionTreeClassifier(max_depth=)
decision_tree.fit (x_train, y_train)

with open (,) as f:
  f = tree.export_graphviz(decision_tree,out_file=f,max_depth=,impurity = True, fature_names = list (train.drop([],axis=1)),class_names = [,], rounded= , filled=) 
    
