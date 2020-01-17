# String Methods

# arbitrary string
name = "ParasarA"
# lowercase and uppercase
name_low = name.lower()
name_up = name.upper()
# results
print(name_low)
print(name_up)
# count the number of a's in name and print the results
print(name.count('a'))

# List Methods

# create list height
height = [174.00, 171.50, 172.00, 153.50]
# print out the index of the element 172.00
print(height.index(172.00))
# print out how often 171.50 appears in height
print(height.count(171.50))

# List Methods (con't)

# create list height
height = [174.00, 171.50, 172.00, 153.50]
# use append to add new heights
height.append(183.00)
height.append(176.00)
# print out height
print(height)
# reverse the orders of the elements in height
height.reverse()
# result
print(height)
# remove 176.00 from height
height.remove(176.00)
# result
print(height)
