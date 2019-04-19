import numpy as np
import os
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

dir = 'result'
companies = ['BA','FB','NFLX','TSLA']
sources = ['yahoo','businessinsider','marketwatch']
all_scores = ['content_scores','title_scores','firstP_scores']

def predict(model):
    X = None
    Y = None
    for c in companies:
        filename = c + "_final_pred.csv"
        filepath = os.path.join ( dir, filename )
        df = pd.read_csv ( filepath )
        x = df[all_scores]
        y = df['Labels']
        if X is None:
            X = x
        else:
            X = X.append ( x )
        if Y is None:
            Y = y
        else:
            Y = Y.append ( y )
    X = X.values
    Y = Y.values
    prediction = model.predict(X)
    print ( classification_report ( Y, prediction ) )
    print ( "Accuracy Score:", accuracy_score ( Y, prediction ) )
#train
X = None
Y = None
for c in companies:
    filename = c + "_final.csv"
    filepath = os.path.join(dir,filename)
    df = pd.read_csv(filepath)
    x = df[all_scores]
    y = df['Labels']
    if X is None:
        X = x
    else:
        X = X.append(x)
    if Y is None:
        Y = y
    else:
        Y = Y.append(y)
X = X.values
Y = Y.values
clf = LinearSVC (dual = False)
clf.fit(X,Y)
predict(clf)


