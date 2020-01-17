# 2D numpy array

# this sample data contains the weight (lb) and the height (in) of 4 players
football = [[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]
# import numpy
import numpy as np
# create a 2D numpy array from football
np_football = np.array(football)
# print out the type of np_football
print(type(np_football))
# print out the shape of np_football
print(np_football.shape)

# Subsetting 2D numpy arrays

# print out the 4th row of football (regular list of lists)
print(football[3][0], football[3][1])
# print out the 4th row of np_football using numpy
print(np_football[3, :])
# select the entire second column of np_football
np_weight_lb = np_football[:, 0]
# print the result
print(np_weight_lb)
# print out the height of 3rd player
print(np_football[2, 1])

# 2D arithmetic (units conversion)

# suppose the team's weight and height have changed
update_football = [[-11.16, 1.23], [16.09, 1.02], [5.08, 1.15], [4.23, 1.09]]
# create 2D numpy array from update_football
np_update_football = np.array(update_football)
# update weight and height data
updated = np_football + np_update_football
# print out the addition of np_football and np_update_football
print(updated)
# the diffrence without using numpy array
print(football + update_football)
# convert the units
conversion = np.array([0.453592, 0.0254])
# print out the result
print(updated * conversion)
