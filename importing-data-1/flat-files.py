# === Importing entire text files ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Importing Data')
# open a file :file
file = open('moby_dick.txt', mode = 'r')
# print it
print(file.read())
# check whether file is closed
print(file.closed)
# close file
file.close()
# check whether file closed
print(file.closed)

# === Importing text files line by line ===

# read & print the first 3 lines
with open('moby_dick.txt') as file :
    print(file.readline())
    print(file.readline())
    print(file.readline())

# === Using NumPy to import flat files ===

# import package
import numpy as np
# assign file name to variable: file
file = 'digits.csv'
# load file as array: digits
digits = np.loadtxt(file, delimiter = ',')
# print datatype of digits
print(type(digits))
# select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))
# import matplotlib
import matplotlib.pyplot as plt
# plot reshaped data
plt.imshow(im_sq, cmap = 'Greys', interpolation = 'nearest')
plt.show()
plt.close()

# === Customizing import ===

# import numpy
import numpy as np
# assign the filename: file
file = 'digits_header.txt'
# load the data: data
data = np.loadtxt(file, delimiter = '\t', skiprows = 1, usecols = [0,2])
# print data
print(data)

# === Importing different datatypes ===

# assign filename: file
file = 'seaslug.txt'
# import file: data
data = np.loadtxt(file, delimiter = '\t', dtype = str)
# print the first element of data
print(data[0])
# import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter = '\t', dtype = float, skiprows = 1)
# print the 10th element of data_float
print(data_float[9])
# ploat a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
plt.close()

# === Working with mixed datatypes (1) ===

# use np.genfromtxt instead of np.loadtxt to import data in which the datasets contains different type of data
data = np.genfromtxt('titanic.csv', delimiter = ',', names = True, dtype = None, encoding = None, usecols = 'Survived')
# print the last four values
print(data[887:891])

# === Working with mized datatypes (2) ===

# assign the filename: file
file = 'titanic.csv'
# import file using np.recfromcsv: d
d = np.recfromcsv(file, encoding = None)
# print out first three entries of d
print(d[:3])

# === Using pandas to import flat files as DataFrames(1) ===

# import pandas as pd
import pandas as pd
# assign the filename: file
file = 'titanic.csv'
# read the file into a DataFrame: df
df = pd.read_csv(file)
# view the head of the DataFrame
print(df.head())

# === Using pandas to import flat files as DataFrames(2) ===

# assign the filename: file
file = 'digits.csv'
# read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows = 5, header = None)
# build a numpy array from the DataFrame: data_array
data_array = data.values
# print the datatype of data_array
print(type(data_array))

# === Customizing pandas import ===

# import matplotlib.pyplot
import matplotlib.pyplot as plt
# assign filename: file
file = 'titanic_corrupt.txt'
# import file: data
data = pd.read_csv(file, sep = '\t', comment = '#', na_values = ['Nothing'])
# print the head of the DataFrame
print(data.head())
# plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
plt.close()
