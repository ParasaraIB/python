# === Processing large amount of Twitter data ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Data Science Toolbox 1')
# import pandas
import pandas as pd
# initialize an empty dictionary: counts_dict
counts_dict = {}
# iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv', chunksize = 10) :
    # iterate over the column in DataFrame
    for entry in chunk['lang'] :
        if entry in counts_dict.keys() :
            counts_dict[entry] += 1
        else :
            counts_dict[entry] = 1
# print the populated dictionary
print(counts_dict)

# === Extracting information for large amounts of Twitter data ===

# define count_entries()
def count_entries(csv_file, c_size, colname) :
    """Return a dictionary with counts of occurences as value for each key."""
    # initialize an empty dictionary: counts_dict
    counts_dict = {}
    # iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize = c_size) :
        # iterate over the column in DataFrame
        for entry in chunk[colname] :
            if entry in counts_dict.keys() :
                counts_dict[entry] += 1
            else :
                counts_dict[entry] = 1
    # return counts_dict
    return counts_dict
# call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')
# print result_counts
print(result_counts)
