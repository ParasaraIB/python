# === Loading .mat files ===

# import file dictionary
import os
# get information about current dictionary
print(os.getcwd())
# open directory in which data is stored
os.chdir(r'D:\Data Science\Data Camp\Importing Data')
# import package
import scipy.io
# load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')
# print the datatype type of mat
print(type(mat))

# === The structure of .mat in Python ===

# print the keys of the MATLAB dictionary
print(mat.keys())
# print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))
# import numpy
import numpy as np
# print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))
# subset the array and plot it
import matplotlib.pyplot as plt
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
