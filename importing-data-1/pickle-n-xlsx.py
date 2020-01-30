# === Making a pickle file ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# set the directory to store the data
os.chdir(r'D:\Data Science\Data Camp\Importing Data')
# import pickle package
import pickle
# define dictionary: data to make a pickle file
data = {'June': 69.4, 'Aug': 85, 'Airline': 8, 'Mar': 84.4}
# set the filename
filename = 'data.pkl'
# open the file for writing
outfile = open(filename, 'wb')
# save the file
pickle.dump(data, outfile)
# close the file
outfile.close()

# === Loading a pickled file ===

# open pickle file and load data: d
with open('data.pkl', 'rb') as file :
    d = pickle.load(file)
# print d
print(d)
# print datatype of d
print(type(d))

# === Listing sheets in excel files ===

# import pandas
import pandas as pd
# assign spreadsheet filename: file
file = 'battledeath.xlsx'
# load spreadsheet: xls
xls = pd.ExcelFile(file)
# print sheet names
print(xls.sheet_names)

# === Importing sheets from excel files ===

# load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')
# print the head of the Data Frame df1
print(df1.head())
# load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)
# print the head of the DataFrame df2
print(df2.head())

# === Customizing spreadsheet import ===

# parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows = [0], names = ['Country', 'AAM due to War (2002)'])
# print the head of the DataFrame df1
print (df1.head())
