# Average versus median (1)

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Basic')
# import pandas
import pandas as pd
# this example is using soccer player's heights, positions, weights (list type of data)
positions = pd.read_csv('fifa.csv', usecols = [3])
heights = pd.read_csv('fifa.csv', usecols = [4])
# import numpy
import numpy as np
# convert positons and heights to numpy arrays
np_positions = np.array(positions)
np_heights = np.array(heights)
# heights of the goalkeepers
gk_heights = np_heights[np_positions == ' GK']
# heights of the other players
other_heights = np_heights[np_positions != ' GK']
# print out the median height of GK ver. 1
med_gk = np.median(gk_heights)
print('Median height of GK: ' + str(med_gk))
# print out the median height of GK ver. 2
print('Median height of GK: ' + str(np.median(gk_heights)))
# print out the median height of other players
print('Median height of other players: ' + str(np.median(other_heights)))
# print out the standard deviation of the players' height
print('Standard deviation of GK: ' + str(np.std(gk_heights)))
print('Standard deviation of other players: ' + str(np.std(other_heights)))

# Average versus median (2)

# suppose the data is in the form of lists of list (subset)
soccer = [np_positions, np_heights]
# convert soccer to numpy array
np_soccer = np.array(soccer)
print(np_soccer)
# convert the data to numpy arrays and float type since the types are conflicting
np_heights2 = np.array(np_soccer[1,:]).astype(np.float)
np_positions2 = np.array(np_soccer[0,:]).astype(np.str)
# heights of the goalkeepers
gk_heights2 = np_heights2[np_positions2 == ' GK']
# heights of the other players
other_heights2 = np_heights2[np_positions2 != ' GK']
# print out the median height of GK
print('Median 2 height of GK: ' + str(np.median(gk_heights2)))
# print out the median height of other players
print('Median 2 height of other players: ' + str(np.median(other_heights2)))
# print out the standard deviation of the players' height
print('Standard deviation 2 of GK: ' + str(np.std(gk_heights2)))
print('Standard deviation 2 of other players: ' + str(np.std(other_heights2)))
