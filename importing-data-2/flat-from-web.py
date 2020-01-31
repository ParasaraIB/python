# === Importing flat files from the web ===

# import package
from urllib.request import urlretrieve
# import pandas
import pandas as pd
# assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# import os
import os
# change directory
os.chdir(r'D:\Data Science\Data Camp\Importing Data 2')
# save file locally
urlretrieve(url, 'winequality-red.csv')
# read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep = ';')
print(df.head())

# === Opening and reading flat files from the web ===

# import packages
import matplotlib.pyplot as plt
import pandas as pd
# assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# read file into a DataFrame: df
df = pd.read_csv(url, sep = ';')
# print the head of the DataFrame
print(df.head())
# plot first column of df
pd.DataFrame.hist(df.iloc[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$')
plt.ylabel('count')
plt.show()
plt.close()

# === Import non-flat files from the web ===

# assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
# read in all sheets of excel file: xls
xls = pd.read_excel(url, sheet_name = None)
# print the sheetnames
print(xls.keys())
# print the head of the first sheet (using its name, not its index)
print(xls['1700'].head())
