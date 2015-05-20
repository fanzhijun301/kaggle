# kaggle

import math
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

def evaluate(Y_test, Y_predict):
    logloss = 0
    line_count = 0
    for test, pre in zip(Y_test, Y_predict):
        line_count += 1
        value = pre[test-1]
        logloss += math.log(value)
    logloss /= -(line_count * 1.0)
    print logloss
    

train_file = "../../kaggle/ottogroup/train1/train"
test_file = "../../kaggle/ottogroup/train1/test"
X_train, Y_train = read_file(train_file)
X_test, Y_test = read_file(test_file)
print "read ok"
logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(X_train, Y_train)
print "train ok"
#Y_predict = logreg.predict_log_proba(X_test)
Y_predict = logreg.predict_proba(X_test)
#print Y_predict
#print Y_predict.shape
evaluate(Y_test, Y_predict)

