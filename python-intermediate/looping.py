# === while: formulation with example ===

x = 1
while x < 4 :
    print(x)
    x = x + 1

# === basic while loop ===

# initialize offset
offset = 8
# code the wile loop
while offset != 0 :
    print('correcting...')
    offset = offset - 1
    print(offset)

# === add conditionals ===

# initialize offset
offset = -6
# code the wile loop
while offset != 0 :
    print('correcting...')
    if offset > 0 :
        offset = offset - 1
    else :
        offset = offset + 1
    print(offset)

# === loop over a list ===

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# code the for loop
for area in areas :
    print(area)

# === indexes and values ===

# change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print('room ' + str(index) +  ': ' + str(area))

# === indexes and values (2)

# update code for the for loop
for index, area in enumerate(areas) :
    print('room ' + str(index + 1) + ': ' + str(area))

# === loop over list of lists ===

# house list of lists
house = [['hallway', 11.25],
['kitchen', 18.0],
['living room', 20.0],
['bedroom', 10.75],
['bathroom', 9.50]]
# build for loop
for room in house :
    print('the ' + str(room[0]) + ' is ' + str(room[1]) + ' sqm')
