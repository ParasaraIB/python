# === driving right ===

# import different file directory
import os
# get information about current directory
print(os.getcwd())
# open different directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Intermediate')
# import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# extract drives_right column as Series: dr
dr = cars['drives_right']
# use dr to subset cars: sel
sel = cars[dr]
# print sel
print(sel)

# === driving right (2) ===

# convert code to a one-liner
sel = cars[cars['drives_right']]
# print sel
print(sel)

# === cars per capita (1) ===

# create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]
# print car_maniac
print(car_maniac)

# === cars per capita (2) ===

# import numpy
import numpy as np
# create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
# print medium
print(medium)
