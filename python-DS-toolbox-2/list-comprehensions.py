# === Basic list comprehension ===

# define a list: doctor
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
# list comprehension to produce the first character of each string
listc_doctor = [ doc[0] for doc in doctor]
# print listc_doctor
print(listc_doctor)

# === Writing list comprehensions ===

# create list comprehension: squares
squares = [i ** 2 for i in range (0,10)]
print(squares)

# === Nested list comprehensions ===

# create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range (0,5)] for row in range(0,5)]
# print the matrix
for row in matrix :
    print(row)
