__author__ = 'fzj'

import utils
import numpy as np
from sklearn import linear_model
from sklearn.externals import joblib

def train(fea_file, model_file):
    X_train,Y_train = utils.get_data(fea_file)
    print "load fea file ok"
    logreg = linear_model.LogisticRegression(C=1e5)
    logreg.fit(X_train,Y_train)
    print "fit ok"
    joblib.dump(logreg, model_file)
    print "dump ok"

