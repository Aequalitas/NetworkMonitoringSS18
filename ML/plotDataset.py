
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')


trainData = np.load("../../data/data.npy")


# plot with various axes scales
plt.figure(1)

# CPU
plt.subplot(221)
plt.hist(trainData[2,:,0]*100, bins=50, density=False)
plt.title('CPU')
plt.grid(True)


# MEM
plt.subplot(222)
plt.hist(trainData[2,:,1]*100, bins=50, density=False)
plt.title('MEM')
plt.grid(True)


# DISK
plt.subplot(223)
plt.hist(trainData[2,:,2]*100, bins=50, density=False)
plt.title('DISK')
plt.grid(True)

# IPPACKS
plt.subplot(224)
plt.hist(trainData[2,:,3], bins=50, density=False)
plt.title('IPPACKS')
plt.grid(True)

# # RESET RECEIVED
# plt.subplot(225)
# plt.hist(trainData[2,:,4], bins=50, density=False)
# plt.title('RESET RECEIVED')
# plt.grid(True)

# # RESET SENT
# plt.subplot(226)
# plt.hist(trainData[2,:,5], bins=50, density=False)
# plt.title('RESET SENT')
# plt.grid(True)


plt.show()