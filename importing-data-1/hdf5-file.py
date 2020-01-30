# === Using h5py to import HDF5 files ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Importing Data')
# import packages
import numpy as np
import h5py
# assign filename: file
file = 'LIGO_data.hdf5'
# load file: data
data = h5py.File(file, 'r')
# print the datatype of the loaded file
print(type(data))
# print the keys of the file
for key in data.keys() :
    print(key)

# === Extracting data from HDF5 file ===

# get the HDF5 group: group
group = data['strain']
# check out keys pf group
for key in group.keys() :
    print(key)
# set variable equal to time series data: strain use [()] rather than .values to avoid warning
strain = data['strain']['Strain'][()]
print(strain)
# set number of time points to sample: num_samples
num_samples = 10000
# set time vector
time = np.arange(0, 1, 1/num_samples)
# plot data
import matplotlib.pyplot as plt
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
plt.close()
