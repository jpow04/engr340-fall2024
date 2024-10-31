import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = np.array(np.loadtxt(signal_filepath, delimiter=',', skiprows=2))

# Extract variables
elapsed_time = signal[:,0]
mlii = signal[:,1]
v1 = signal[:,2]
# Plot raw signal
plt.title('Raw Signal')
plt.xlabel('Time (s)')
plt.ylabel('MLII and V1 (mV)')
plt.plot(elapsed_time, mlii, label='MLII')
plt.plot(elapsed_time, v1, label='V1')
plt.legend()
plt.show()

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""

mlii_diff = np.diff(mlii, prepend=mlii[0])
v1_diff = np.diff(v1, prepend=v1[0])
# Plot differentiated signal
plt.title('Differentiated Signal')
plt.xlabel('Time (s)')
plt.ylabel('MLII and V1 (mV)')
plt.plot(elapsed_time, mlii_diff, label='MLII')
plt.plot(elapsed_time, v1_diff, label='V1')
plt.legend()
plt.show()

"""
Step 4: Square the results of the previous step
"""

mlii_squared = np.square(mlii)
v1_squared = np.square(v1)
# Plot squared signal
plt.title('Squared Signal')
plt.xlabel('Time (s)')
plt.ylabel('MLII and V1 (mV)')
plt.plot(elapsed_time, mlii_squared, label='MLII')
plt.plot(elapsed_time, v1_squared, label='V1')
plt.legend()
plt.show()

"""
Step 5: Pass a moving filter over your data
"""

window_size = 100
moving_avg_mlii = np.convolve(mlii_squared, np.ones(window_size)/window_size, mode='same')
moving_avg_v1 = np.convolve(v1_squared, np.ones(window_size)/window_size, mode='same')
# Plot average signal
plt.title('Average Signal')
plt.xlabel('Time (s)')
plt.ylabel('MLII and V1 (mV)')
plt.plot(elapsed_time, moving_avg_mlii, label='MLII')
plt.plot(elapsed_time, moving_avg_v1, label='V1')
plt.legend()
plt.show()

# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name)
plt.plot(signal)
plt.show()