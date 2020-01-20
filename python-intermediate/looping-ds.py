# === Loop over dictionary ===

# definition of dictionary
europe = {'spain':'madrid', 
'france':'paris', 
'germany':'berlin', 
'norway':'oslo', 
'italy':'rome'}
# iterate over europe
for key, value in europe.items() :
    print('the capital of ' + str(key) + ' is ' + str(value))

# === Loop over numpy array ===

# import different file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Basic')
# import numpy
import numpy as np
# import csv to open csv file
import csv
# import itertools for efficient looping
import itertools as it
# open the file
f = open('baseball.csv')
# read the file
csv_f = csv.reader(f)
# let height and weight as the variables to store the results of for loop
height = []
weight = []
# for loop to get the height and weight
for row in it.islice(csv_f, 1, None) :
    height.append(row[3])
    weight.append(row[4])
# use for loop to get the [height, weight] list form zip and store it in baseball
baseball = [[i, j] for i, j in zip(height, weight)]
# conversion to numpy array
np_baseball = np.array(baseball)
np_height = np.array(height)
np_weight = np.array(weight)
# for loop over np_height
for height in np.nditer(np_height) :
    print(str (height) + ' inches')
# for loop over np_baseball
for element in np.nditer(np_baseball) :
    print(element)

# === Loop over data frame (1) ===

# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Intermediate')
# import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)

# === Loop over data frame (2) ===

# adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) + ': ' + str(row['cars_per_cap']))

# === Add column (1) ===

# code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()
# print cars
print(cars)

# === Add column (2) ===

# use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)
