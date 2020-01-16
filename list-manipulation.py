# Subsetting

x = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
# Print the first element of the third list in the x-list
print(x[2][0])
# Print the first two-elements of the third list in the x-list
print(x[2][:2])

# Replace elements

y = ["a", "b", "c", "d"]
print(y)
# Replace the second element
y[1] = "r"
# Replace the last two-elements
y[2:] = ["s", "t"]
# Result
print(y)

# Extend a list

z = ["a", "b", "c", "d"]
# Define z2-list which consists of z-list elements
z2 = x + ["e", "f"]
# Result
print(z2)

# Remove elements

xy = ["a", "b", "c", "d"]
print(xy)
# Delete "a" element
del(xy[1])
# Result
print(xy)

# Command

print(z2)
print (xy)
# Another way two execute command in the same line
print(z2); print(xy)

# Explicit copy

xx = [1, 2, 3, 4]
# Create copy
xx_copy = xx
xx_copy[0] = 0
# Result
print(xx)
print(xx_copy)
# Another copy to see the difference
yy = [1, 2, 3, 4]
# Create explicit copy with list() or [:]
yy_copy = yy[:]
yy_copy[0] = 0
# Result
print(yy)
print(yy_copy)
