# === Twitter case study with default argument ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Data Science Toolbox 1')
# import pandas
import pandas as pd
# import twitter as DataFrame: tweets_df
tweets_df = pd.read_csv('tweets.csv')
# define count_entries()
def count_entries(df, col_name = 'lang') :
    """Return a dictionary with counts of occurences as value for each key."""
    # initialize an empty dictionary: cols_count
    cols_count = {}
    # extract column from DataFrame: col
    col = df[col_name]
    # iterate over the column in DataFrame
    for entry in col:
        # if entry is in cols_count, add 1
        if entry in cols_count.keys() :
            cols_count[entry] += 1
        # else add the entry to cols_count, set the value to 1
        else :
            cols_count[entry] = 1
    # return the cols_count dictionary
    return cols_count
# call count_entries(): result1
result1 = count_entries(tweets_df)
# call count_entries(): result2
result2 = count_entries(tweets_df, 'source')
# print results
print(result1)
print(result2)

# === Twitter case study using flexible argument ===

# define count_entries()
def count_entries(df, *args) :
    """Return a dictionary with counts of occurences as value for each key."""
    # initialize an empty dictionary: cols_count
    cols_count = {}
    # iterate over column names in args
    for col_name in args :
        # extract column from DataFrame: col
        col = df[col_name]
        # iterate over the column in DataFrame
        for entry in col:
            # if entry is in cols_count, add 1
            if entry in cols_count.keys() :
                cols_count[entry] += 1
            # else add the entry to cols_count, set the value to 1
            else :
                cols_count[entry] = 1
    # return to the cols_count dictionary
    return cols_count
# call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')
# call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')
# print results
print(result1)
print(result2)
