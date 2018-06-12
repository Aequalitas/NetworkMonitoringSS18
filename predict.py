import numpy as np 
from sklearn import svm
from sklearn.externals import joblib


DEMO = [[
    "0.4",
    "0.017",
    "0.433",
    "0.3",
    "0.1",
    "0.3"
]]


model = joblib.load("models.pkl")
pred = model[0].predict(DEMO)
print(pred)