# Author: Franz Weidmann
# Info: Takes a log as input and predicts wether it is an outlier or not
# Input example:
# [[
#     "0.31", #cpu
#     "0.0175", #mem
#     "0.33", #disk
#     "2222223", # ippacks
#     "1.0", # reset received
#     "2.0" # reset sent
# ]]

import numpy as np 
from sklearn import svm
from sklearn.externals import joblib


DEMO = [[
    "0.31",
    "0.0175",
    "0.33",
    "2222223",
    "1.0",
    "2.0"
]]


model = joblib.load("models.pkl")
DEMO1 = model[0][0].transform(DEMO)
pred = model[1][0].predict(DEMO1)
print(pred)
DEMO2 = model[0][0].transform(DEMO)
pred = model[1][1].predict(DEMO2)
print(pred)
DEMO3 = model[0][0].transform(DEMO)
pred = model[1][2].predict(DEMO3)
print(pred)