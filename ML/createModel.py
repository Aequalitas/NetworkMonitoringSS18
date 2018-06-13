# Author: Franz Weidmann
# Info: Creates for each hosts an SVM one class classifier to retrieve the normal
# state of the host. All models will be trained and save into a npy file

import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from sklearn.preprocessing.data import QuantileTransformer

trainData = np.load("../../data/data.npy")

# transform data for scaling and save the state of the transformer for each host
scalers = []
for h in range(trainData.shape[0]):
    _scaler = QuantileTransformer()
    trainData[h] = _scaler.fit_transform(trainData[h])
    scalers.append(_scaler)
    
# train and svm one class classifier for every host
models = []
for modelIndex in range(trainData.shape[0]):
    print("Creating model ", modelIndex)
    model = svm.OneClassSVM( kernel="rbf", verbose=True)
    model.fit(trainData[modelIndex])
    models.append(model)
    print("Trained model ", modelIndex)

joblib.dump([scalers, models], "models.pkl")
