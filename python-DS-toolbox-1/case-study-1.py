# === Case study: Twitter ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Data Science Toolbox 1')
# import pandas
import pandas as pd
# import twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')
# initialize an empty dictionary: langs_count
langs_count = {}
# extract column from DataFrame: col
col = df['lang']
# iterate ove lang column in DataFrame
for entry in col :
    # if the language is in langs_count, add 1
    if entry in langs_count.keys() :
        langs_count[entry] += 1
    # else add the language to langs_count, set the value to 1
    else :
        langs_count[entry] = 1
# print the populated dictionary
print(langs_count)

# === Solve the case study using user-defined functions ===

# define count_entries()
def count_entries(df, col_name) :
    """Return a dictionary with counts of occurences as value for each key."""
    # initialize an empty dictionary: langs_count
    langs_count = {}
    # extract column from DataFrame: col
    col = df[col_name]
    # iterate over lang column in DataFrame
    for entry in col:
        # if the language is in the langs_count, add 1
        if entry in langs_count.keys() :
            langs_count[entry] += 1
        # else add the language to langs_count, set the value to 1
        else :
            langs_count[entry] = 1
    # return the langs_count dictionary
    return langs_count
# call count_entries(): result
result = count_entries(df, 'lang')
# print the result
print(result)
