# Author: Franz Weidmann
# Info: Creates demo data to be usable for the machine learning model
# Data structure in one time frame:
# 
# {
#     "host":<Hostname>,
#     "hostData":
#     {
#         "cpu":<float CPU usage>,
#         "mem":<float MEM usage>,
#         "disk":<float DISK usage>
#     },
#     "networkData":
#     {
#         "ipPacks":<int number of sent/recieved ip packages>,
#         "resetsReceived":<int number of >
#         "resetsSent":<int number of >
#     }
# }

import numpy as np


# MIN and MIN Values
minMaxValues = [
    [0.0, 0.1], # CPU
    [0.0, 0.1], # MEM
    [0.1, 0.4], # DISK
    [10000, 100000], # IPPACKS
    [0, 4], # RESET RECEIVED
    [0, 4] # RESET SENT
]
# Numbers of entries aka how many seconds
NUMBERS = 10000
# Number of hosts
HOSTS = 3
# Number of features
FNUMBERS = 6 



# creating random values 

data = np.zeros((HOSTS, NUMBERS, FNUMBERS))

for h in range(HOSTS):
    for fn in range(FNUMBERS):
        r = np.random.uniform(minMaxValues[fn][0], minMaxValues[fn][1], NUMBERS*HOSTS)
        for i in range(NUMBERS):
            data[h,i,fn] = r[i]

print(data.shape)

np.save("data.npy", data)