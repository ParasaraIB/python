# Histograms

# import different file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Intermediate')
# import numpy
import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
# load the data
import pandas as pd
gapminder = pd.read_csv('gapminder.csv')
np_gapminder = np.array(gapminder)
# separate each attribute
country = np_gapminder[:,1]
population = np_gapminder[:,3]
life_exp = np_gapminder[:,5]
gdp_cap = np_gapminder[:,6]
# build a histogram of life_exp with bins = 15
plt.hist(life_exp, bins = 15)
plt.show()
plt.clf()
# load life_exp data 1950
life_exp1950 = np.array(pd.read_csv('life_exp1950.csv'))
plt.hist(life_exp1950, bins = 15)
plt.show()
plt.clf()
