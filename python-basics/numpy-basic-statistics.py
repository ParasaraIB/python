# Numpy: basic statistics

# this example is using soccer player's heights, positions, weights (list type of data)
heights = [191, 184, 185, 180, 181, 187, 170, 179, 183, 186, 185, 170]
positions = ['GK', 'D', 'M', 'A', 'GK', 'D', 'M', 'A', 'GK', 'D', 'M', 'A',]
weights = [90, 94, 82, 78, 85, 92, 63, 69, 75, 81, 88, 59]
# import numpy
import numpy as np
# convert positons and heights to numpy arrays
np_heights = np.array(heights)
np_positions = np.array(positions)
np_weights = np.array(weights)
# heights of the goalkeepers
gk_heights = np_heights[np_positions == 'GK']
# heights of the other players
other_heights = np_heights[np_positions != 'GK']
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
# print out the correlation between heights and weights
print('Correlation: ' + str(np.corrcoef((np_heights), np_weights)))

# suppose the data is in the form of lists of list (subset)
soccer = [[heights], [positions], [weights]]
# convert soccer to numpy array
np_soccer = np.array(soccer)
# convert the data to numpy arrays and float type since the types are conflicting
np_heights2 = np.array(np_soccer[0,:]).astype(np.float)
np_positions2 = np.array(np_soccer[1,:]).astype(np.str)
np_weights2 = np.array(np_soccer[2,:]).astype(np.float)
# heights of the goalkeepers
gk_heights2 = np_heights2[np_positions2 == 'GK']
# heights of the other players
other_heights2 = np_heights2[np_positions2 != 'GK']
# print out the median height of GK
print('Median 2 height of GK: ' + str(np.median(gk_heights2)))
# print out the median height of other players
print('Median 2 height of other players: ' + str(np.median(other_heights2)))
# print out the standard deviation of the players' height
print('Standard deviation 2 of GK: ' + str(np.std(gk_heights2)))
print('Standard deviation 2 of other players: ' + str(np.std(other_heights2)))
# print out the correlation between heights and weights
corr = np.corrcoef(np_heights2, np_weights2)
print('Correlation 2: ' + str(corr))
