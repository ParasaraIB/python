# === Importing sas7bdat package ===


import os

print(os.getcwd())

os.chdir(r'D:\Data Science\Data Camp\Importing Data')
# import sas7bdat package
from sas7bdat import SAS7BDAT
# save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file :
    df_sas = file.to_data_frame()
# print head of DataFrame
print(df_sas.head())
# import pandas
import pandas as pd
# import matplotlib
import matplotlib.pyplot as plt
# plot histogram of DataFrame features
pd.DataFrame.hist(df_sas[['P']])
plt.xlabel('count')
plt.show()
plt.close()

# === Importing stata files ===

# load stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')
# print the head of the DataFrame df
print(df.head())
# plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()
plt.close()
