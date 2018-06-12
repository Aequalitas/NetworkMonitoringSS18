# Author: Franz Weidmann
# Info: Loads json log files and serializes them into one npy file for trainig
# SHAPE: (HOSTS, NUMBER SAMPLES, NUMBER FEATURES)

import numpy as np
import os
import json

DATAPATH = "../data/logs/"
DATASIZE = len(os.listdir(DATAPATH))
DATAFEATURES = 6
HOSTS = 3

# to reduce the range of IPPACKS to below 1.0
PACKETLIMIT = 10000000
RESETLIMIT = 10

data = np.zeros((HOSTS,DATASIZE, DATAFEATURES))

for fIndex, fileName in enumerate(os.listdir(DATAPATH)):
    with open(DATAPATH+fileName) as file:
        logJson = json.load(file)
        for h in range(HOSTS):
            #print(h, fileName, logJson[h][0]["cpu"])
            
            data[h,fIndex,0] = float(logJson[h][0]["cpu"]) if logJson[h][0]["cpu"] != "" else 0.0
            data[h,fIndex,1] = float(logJson[h][0]["mem"])
            data[h,fIndex,2] = float(logJson[h][0]["disk"])
            data[h,fIndex,3] = float(logJson[h][1]["ipPacks"])
            data[h,fIndex,4] = float(logJson[h][1]["resetsReceived"])
            data[h,fIndex,5] = float(logJson[h][1]["resetsSend"])

#sets IPPACKS values below 1.0
data[:,:,3] = data[:,:,3] / PACKETLIMIT

#sets receive values below 1.0
data[:,:,4] = data[:,:,4] / RESETLIMIT
data[:,:,5] = data[:,:,5] / RESETLIMIT

print("Data statistics:")
print(data[:,:,0].min(), data[:,:,0].max())
print(data[:,:,1].min(), data[:,:,1].max())
print(data[:,:,2].min(), data[:,:,2].max())
print(data[:,:,3].min(), data[:,:,3].max())
print(data[:,:,4].min(), data[:,:,4].max())
print(data[:,:,5].min(), data[:,:,5].max())

np.save("../data/data.npy", data)