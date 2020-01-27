# Numpy array example

football = [183, 187, 192, 195, 178, 175, 180, 181]
# import numpy package as np
import numpy as np
# create a numpy aray from football
np_football = np.array(football)
# print out the type of np_football
print(type(np_football))

# BMI Calculator

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Basic')
# import pandas
import pandas as pd
# import baseball data
baseball = pd.read_csv('baseball.csv')
# get height data
height_in = baseball.iloc[:,3]
# import numpy package as np
import numpy as np
# create a numpy array from height_in
np_height_in = np.array(height_in)
# convert inches to m
np_height_m = np.array(height_in) * 0.0254
# result
print(np_height_m)
weight_lb = baseball.iloc[:,4]
# create array from weight_lb to weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592
# calculate BMI
bmi = np_weight_kg / np_height_m ** 2
# result
print(bmi)

# Determine the light weight

# create the light weight array
light_weight = bmi < 21
# print out light weight
print(light_weight)
# print out BMI below 21
print(bmi[light_weight])

# Numpy side effect

print(np.array([True, 1, 2]) + np.array([3, 4, False]))
print([True, 1, 2] + [3, 4, False])

# Subsetting numpy arrays

# print out the weight at index 9 (index start from 0)
print(np_height_in[9])
# print out sub-array of np_height_in: index 1 to 5, including index 5
print(np_height_in[1:6])
