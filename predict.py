__author__ = 'fzj'

import utils
from sklearn import linear_model
from sklearn.externals import joblib

def predict(fea_file, model_file, predict_file):
    Y_test,X_test = utils.get_data(fea_file)
    log_reg = joblib.load(model_file)
    Y_predict = log_reg.predict(X_test)
    ou_predict = open(predict_file, "w")
    for y in Y_predict:
        ou_predict.write(str(y) + "\n")
    ou_predict.close()



