import numpy as np
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from scipy.stats import pearsonr

dir = 'result'
companies = ['FB','NFLX','BA','TSLA']
sources = ['marketwatch.com']#['yahoo.com','businessinsider.com','marketwatch.com']
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
        
        y = df['diff'].iloc[1:]
        #y = df['diff']
        if Y is None:
            Y = y
        else:
            Y = Y.append(y)

    n = len(X.values)
    total = np.concatenate ((np.reshape ( np.array ( X.values ), (n, 1) ), np.reshape ( np.array ( X2.values ), (n, 1) )), axis=1 )
    #y = [1 if j > 0 else 0 for j in Y.values]
    y = np.array(Y)
    pred = model.predict(total)
    r = r2_score(y,pred)
    e = mean_squared_error(y, pred)
    print(s + ":")
    print("R2 score:",r)
    print("mean square error:",e)

    # pred = model.predict(X_all.values)
    # print('Source:',s)
    # print("Score type:",score)
    # print ( classification_report ( y, pred ) )
    # print("Accuracy Score:", accuracy_score(y, pred))


def correlation():
    X = None
    X2 = None
    Y = None
    for s in sources:
        X_all = None
        for c in companies:
            filename = c + "_" + s + '_results.csv'
            filepath = os.path.join(dir,filename)
            df = pd.read_csv(filepath)
            ss = df[all_scores]


            
            for i in range(0,len(all_scores)):
                current_score = df[all_scores[i]].iloc[1:]
                pre_score = df[all_scores[i]].iloc[:-1]

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
                
                y = df['diff'].iloc[1:]
                
                if Y is None:
                    Y = y
                else:
                    Y = Y.append(y)
                
                corr = np.corrcoef([current_score.values, pre_score.values, y.values])
                print(s + "_" + c)
                print(all_scores[i])
                #print(corr)
                #print("prev: ",corr[1][2])
                #print("curr: ",corr[0][2])
                print()
                #print("-----------------------------")
                corr_prev = pearsonr(pre_score.values,y.values)
                print("corr_prev: ", corr_prev)
                corr_curr = pearsonr(current_score.values,y.values)
                print("corr_curr: ", corr_curr)
                print("-----------------------------")
        # corr = np.corrcoef ( [X.values, X2.values, Y.values] )
        # print ( s )
        # print ( corr )
        # X = sm.add_constant(X)
        # model = sm.OLS(Y,X).fit()
        # print(model.summary())

        # Linear Regression
        #n = len(X_all.values)
    

    #n = len(X)
    #total = np.concatenate((np.reshape(np.array(X.values),(n,1)), np.reshape(np.array(X2.values),(n,1))),axis = 1 )
    ###y = [1 if j > 0 else 0 for j in Y.values]
    #y = np.reshape(np.array(Y), (n,1))
    ###clf = LinearSVC (tol=1e-5 )
    #reg = LinearRegression().fit(total,y)
    ###clf.fit(X_all.values,y)
    ###predict(s,clf)
    #predict(s, reg)

if __name__ == '__main__':

    correlation()
