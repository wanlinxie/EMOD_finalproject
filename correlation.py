import numpy as np
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import r2_score
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

dir = 'result'
companies = ['BA','FB','NFLX','TSLA']
sources = ['yahoo.com','businessinsider.com','marketwatch.com']
all_scores = ['content_scores','title_scores','firstP_scores']
score = all_scores[0]

def predict(s,model):
    X = None
    X2 = None
    Y = None
    X_all = None
    for c in companies:
        filename = c + "_" + s + "_prediction.csv"
        filepath = os.path.join(dir,filename)
        df = pd.read_csv(filepath)
        ss = df[all_scores]
        cur_score = df[score].iloc[1:]
        pre_score = df[score].iloc[:-1]
        if X is None:
            X = cur_score
        else:
            X = X.append(cur_score)
        if X2 is None:
            X2 = pre_score
        else:
            X2 = X2.append(pre_score)
        if X_all is None:
            X_all = ss
        else:
            X_all = X_all.append(ss)
        #y = df['diff'].iloc[1:]
        y = df['diff']
        if Y is None:
            Y = y
        else:
            Y = Y.append(y)

    #n = len(X.values)
    #total = np.concatenate ((np.reshape ( np.array ( X.values ), (n, 1) ), np.reshape ( np.array ( X2.values ), (n, 1) )), axis=1 )
    y = [1 if j > 0 else 0 for j in Y.values]
    #y = np.reshape ( y, (n, 1) )
    pred = model.predict(X_all.values)
    print('Source:',s)
    print("Score type:",score)
    print ( classification_report ( y, pred ) )
    print("Accuracy Score:", accuracy_score(y, pred))

for s in sources:
    X = None
    X2 = None
    Y = None
    X_all = None
    for c in companies:
        filename = c + "_" + s + '_results.csv'
        filepath = os.path.join(dir,filename)
        df = pd.read_csv(filepath)
        ss = df[all_scores]
        current_score = df[score].iloc[1:]
        pre_score = df[score].iloc[:-1]
        if X is None:
            X = current_score
        else:
            X = X.append(current_score)
        if X2 is None:
            X2 = pre_score
        else:
            X2 = X2.append(pre_score)
        if X_all is None:
            X_all = ss
        else:
            X_all = X_all.append(ss)
        #y = df['diff'].iloc[1:]
        y = df['diff']
        if Y is None:
            Y = y
        else:
            Y = Y.append(y)
        # corr = np.corrcoef([current_score.values, pre_score.values, y.values])
        # print(s + "_" + c)
        # print(corr)
    # corr = np.corrcoef ( [X.values, X2.values, Y.values] )
    # print ( s )
    # print ( corr )
    # X = sm.add_constant(X)
    # model = sm.OLS(Y,X).fit()
    # print(model.summary())
    # Linear Regression
    n = len(X_all.values)
    #total = np.concatenate((np.reshape(np.array(X.values),(n,1)), np.reshape(np.array(X2.values),(n,1))),axis = 1 )
    y = [1 if j > 0 else 0 for j in Y.values]
    #y = np.reshape(y, (n,1))
    clf = LinearSVC (tol=1e-5 )
    #reg = LinearRegression().fit(total,y)
    clf.fit(X_all.values,y)
    predict(s,clf)


