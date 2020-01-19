# === Dictionary to DataFrame(1) ===

# pre-defined lists
names = ['Unites States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
# import pandas
import pandas as pd
# create dictionary my_dict with three key:value pairs:my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
# build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
# print cars
print(cars)

# === Dictionary to DataFrame(2) ===

# definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
# specify row labels of cars
cars.index = row_labels
# print cars again
print(cars)

# === CSV to DataFrame(1) ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Intermediate')
# import the cars.csv data: cars
cars = pd.read_csv('cars.csv')
# print out cars
print(cars)

# === CSV to DataFrame(2) ===

# fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)
# print out cars
print(cars)

# === Square Brackets(1) ===

# print out country column as pandas series
print(cars['country'])
# print out country column as pandas DataFrame
print(cars[['country']])
# print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# === Square Brackets(2) ===

# print out first 3 observations
print(cars[0:3])
# print out forth, fifth, and sixth observations
print(cars[3:6])

# === loc and iloc (1) ===

# print out observation for Japan as pandas Series
print(cars.iloc[2])
print(cars.loc['JAP'])
# print out observations for Australia and Egypt as pandas DataFrame
print(cars.loc[['AUS', 'EG']])

# === loc and iloc (2) ===

# print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])
# print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# === loc and iloc (3) ===

# print out drives_right column as DataFrame
print(cars.iloc[:,[2]])
# print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
