# === Dictionaries for data science ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Data Science Toolbox 2')
# import pandas
import pandas as pd
# import the DataFrame
df = pd.read_csv('WDIDataPrepro.csv')
# get the column names
feature_names = list(df.columns)
# get the rows containing the actual values
row_vals = list(df.iloc[0])
# zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)
# create a dictionary: rs_dict
rs_dict = dict(zipped_lists)
# print the dictionary
print(rs_dict)

# === Writing a function ===

# define lists2dict()
def lists2dict(list1, list2) :
    """Return a dictionary where list1 provides the keys and list2 provides the values."""
    # zip_lists: zipped_lists
    zipped_lists = zip(list1, list2)
    # create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)
    # return the dictionary
    return rs_dict
# call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)
# print rs_fxn
print(rs_fxn)

# === Using a list comprehension ===

# define row_lists containing all the rows data
row_lists = [list(df.iloc[row]) for row in range(0,17)]
# print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])
# turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]
# print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])

# === Turning into a DataFrame ===

# turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]
# turn list of dicts into a DataFrame: dicts_df
dicts_df = pd.DataFrame(list_of_dicts)
# print the head of the DataFrame
print(df.head())
