# === Equality ===

# comparison of booleans
print (True == False)
# comparison of integers
print (-5 * 15 != 75)
# comparison of strings
print ('pyscript' == 'PyScript')
# compare a boolean with an integer
print (True == 1)

# === Greater and less than ===

# comparison of integers
x = -3 * 6
print(x >= -10)
# comparison of strings
y = 'test'
print('test' <= y)
# comparison of booleans
print(True > False)

# === Compare arrays ===

# create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than or equal to 18
print(my_house >= 18)
# my_house less than your_house
print(my_house < your_house)

# === and, or, not (1) ===

# define variables
my_kitchen = 18.0
your_kitchen = 14.0
# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)
# double my_kitchen smaller than triple your_kitchen
print(2 * my_kitchen < 3 * your_kitchen)

# === and, or, not (2) ===

# define variables
x = 8
y = 9
# nested logic
print(not (not(x < 3) and not(y > 14 or y > 10)))

# === boolean operators with Numpy ===

# create arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))
# both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))
