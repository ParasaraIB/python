# === Iterators vs Iterables ===

# create a list of strings
flash1 = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
# create an iterator from the list
flash2 = iter(flash1)
# print the flash1 and flash2
print(flash1)
print(flash2)
# print with next
print(next(flash2))
print(next(flash2))
print(next(flash2))
print(next(flash2))
# redifine the iterator
flash2 = iter(flash1)
# print the iterable simultaneously using iterator
print(*flash2)

# === Iterating over iterables (1) ===

# create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
# print each list item in flash using a for loop
for person in flash :
    print(person)
# create an iterator for flash: superhero
superhero = iter(flash)
# print item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

# === Iterating over iterables (2) ===

# create iterator for range(3): small_value
small_value = iter(range(3))
# print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))
# loop over range(3) and print the values
for num in range(3) :
    print(num)
# create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))
# print the first 5 values of googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

# === Iterators as function arguments ===

# create a range object: values
values = range(10,21)
# print the range object
print(values)
# create a list of integers: value_list
values_list = list(values)
# print values_list
print(values_list)
# get the sum of values: values_sum
values_sum = sum(values)
# print values_sum
print(values_sum)
