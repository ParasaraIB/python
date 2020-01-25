# === Processing data in chunks (1) ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Data Science Toolbox 2')
# open a connection to the file
with open('world_ind_pop.csv') as file :
    # skip the column names
    file.readline()
    # initialize an empty dictionary: counts_dict
    counts_dict = {}
    # process only the first 1000 rows
    for j in range(1000) :
        # split the current line into a list: line
        line = file.readline().split(',')
        # get the value for the first column: first_col
        first_col = line[0]
        # if the column value is in the dict, increment its value
        if first_col in counts_dict.keys() :
            counts_dict[first_col] += 1
        # else, add to the dict and set value to 1
        else :
            counts_dict[first_col] = 1
# print the resulting dictionary
print(counts_dict)

# === Writing a generator to load data in chunks (2) ===

# define read_large_file()
def read_large_file(file_object) :
    """A generator function to read a large file lazily."""
    # loop indefinitely until the end of the file
    while True :
        # read a line from the file: data
        data = file_object.readline()
        # break if this is the end of the file
        if not data :
            break
        # yield the line of data
        yield data
# open a connection to the file
with open('world_ind_pop.csv') as file :
    # create a generator object for thr file: gen_file
    gen_file = read_large_file(file)
    # print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

# === Writing a generator to load data in chunks (3) ===

# initialize an empty dictionary: counts_dict
counts_dict = {}
# open a connection to the file
with open('world_ind_pop.csv') as file :
    # skip the column names
    file.readline()
    # iterate over the generator from read_large_file
    for line in read_large_file(file) :
        row = line.split(',')
        first_col = row[0]
        if first_col in counts_dict.keys() :
            counts_dict[first_col] += 1
        else :
            counts_dict[first_col] = 1
# print
print(counts_dict)
