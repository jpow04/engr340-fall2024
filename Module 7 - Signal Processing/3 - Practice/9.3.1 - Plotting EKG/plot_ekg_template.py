
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

ekg_data = np.array(np.loadtxt(path, delimiter=',', skiprows=2))

# save each vector as own variable

elapsed_time = ekg_data[:,0]
mlii = ekg_data[:,1]
v1 = ekg_data[:,2]


# use matplot lib to generate a single

plt.title('EKG Data - MLII')
plt.xlabel('Time (s)')
plt.ylabel('MLII (mV)')
plt.plot(elapsed_time, mlii, label='MLII')
plt.legend()
plt.show()

plt.title('EKG Data - V1')
plt.xlabel('Time (s)')
plt.ylabel('V1 (mV)')
plt.plot(elapsed_time, v1, label='V1')
plt.legend()
plt.show()
