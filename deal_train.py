# kaggle


import numpy as np
from sklearn import linear_model
import sys

def read_file(src_file):
    in_src = open(src_file)
    first = True
    X_arr = []
    Y_arr = []
    for line in in_src:
        if first == True: first = False; continue
        line = line[:-1]
        arr = line.split(",")
        x_in_arr = []
        for index in range(0,len(arr)-1):
            if index == 0: continue
            va = arr[index]
            x_in_arr.append(float(va))
            
        X_arr.append(x_in_arr)
        last_v = arr[len(arr)-1]
        if last_v.find("Class_") != 0: print "err:",line; sys.exit(0)
        Y_arr.append(int(last_v[6:]))
    in_src.close()
    X = np.array(X_arr)
    Y = np.array(Y_arr)
    return X,Y

src_file = "../data/train.csv"
X, Y = read_file(src_file)
logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(X, Y)
Z = logreg.predict_log_proba(X)
print X.shape
print Z
Z = logreg.predict_proba(X)
print Z.shape
