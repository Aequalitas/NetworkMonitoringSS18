# Author: Franz Weidmann
# Info: Creates for each hosts an SVM one class classifier to retrieve the normal
# state of the host. All models will be trained and save into a npy file

import numpy as np
from sklearn import svm
from sklearn.externals import joblib

trainData = np.load("../data/data.npy")

models = []

for modelIndex in range(trainData.shape[0]):
    print("Creating model ", modelIndex)
    model = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1, tol=1.0, verbose=True)
    model.fit(trainData[modelIndex])
    models.append(model)
    print("Trained model ", modelIndex)

joblib.dump(models, "models.pkl")
