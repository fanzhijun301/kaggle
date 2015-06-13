__author__ = 'fzj'

import train
import predict

train_file = "D:/program/kaggle/crime/data/train_fea.txt"
model_file = "D:/program/kaggle/crime/data/model.txt"

train.train(train_file, model_file)
print "train ok"