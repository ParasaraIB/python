# === Select tweets that begin with the string 'RT' ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Data Science Toolbox 1')
# import pandas
import pandas as pd
# import twitter DataFrame: tweets_df
tweets_df = pd.read_csv('tweets.csv')
# select retweets from the twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])
# create list from filter object result: res_list
res_list = list(result)
# print all retweets in res_list
for tweet in res_list :
    print(tweet)

# === Using user-defined functions and try-except error handling ===

# define count_entries()
def count_entries(df, col_name = 'lang') :
    """Return a dictionary with counts of occurences as value for each key."""
    # initialize an empty dictionary: cols_count
    cols_count ={}
    # add try block
    try :
        # extract column from DataFrame: col
        col = df[col_name]
        # iterate over the column in DataFrame
        for entry in col :
            # if entry is in cols_count, add 1
            if entry in cols_count.keys() :
                cols_count[entry]  += 1
            # else add the entry to cols_count, set the value to 1
            else :
                cols_count[entry] = 1
        # return the cols_count dictionary
        return cols_count
    # add except block
    except :
        print('The DataFrame does not have a ' + col_name + ' column.')
# call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')
# print result1
print(result1)

# === Using user-defined functions and raise ValueError ===

# define count_entries()
def count_entries(df, col_name = 'lang') :
    """Return a dictionary with counts of occurences as value for each key."""
    # raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns :
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')
    # initialize an empty dictionary: cols_count
    cols_count = {}
    # extract column from DataFrame: col
    col = df[col_name]
    # iterate over the column in DataFrame
    for entry in col :
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
# print result1
print(result1)
