# 2D numpy array

# this sample data contains the weight (lb) and the height (in) of 4 players
football = [[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]
# import numpy
import numpy as np
# create a 2D numpy array from football
np_football = np.array(football)
# print out the type of np_football
print(type(np_football))

# Baseball data in 2D form

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Basic')
# import pandas
import pandas as pd
# import baseball data
baseball = pd.read_csv('baseball.csv', usecols = ['Height', 'Weight'])
# create np_baseball
np_baseball = np.array(baseball)
# print out the shape of np_baseball
print(np_baseball.shape)

# Subsetting 2D numpy arrays

# print out the 4th row of football (regular list of lists)
print(np_baseball[3][0], np_baseball[3][1])
# print out the 4th row of np_football using numpy
print(np_baseball[3, :])
# select the entire second column of np_football
np_weight_lb = np_baseball[:, 0]
# print the result
print(np_weight_lb)
# print out the height of 3rd player
print(np_baseball[2, 1])

# 2D arithmetic (units conversion)

# import baseball data
baseball = pd.read_csv('baseball.csv', usecols = ['Height', 'Weight', 'Age'])
# create np_baseball
np_baseball = np.array(baseball)
# suppose the team's weight and height have changed
update_baseball = pd.read_csv('updated.csv')
# create 2D numpy array from update_baseball
np_update_baseball = np.array(update_baseball)
# update weight and height data
updated = np_baseball + np_update_baseball
# print out the addition of np_football and np_update_baseball
print(updated)
# convert the units
conversion = np.array([0.0254, 0.453592, 1])
# print out the result
print(np_baseball * conversion)
