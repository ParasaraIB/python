# Basic plot with matplotlib

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
import pandas
gapminder = pandas.read_csv('gapminder.csv')
np_gapminder = np.array(gapminder)
# separate each attribute
country = np_gapminder[:,1]
population = np_gapminder[:,3]
life_exp = np_gapminder[:,5]
gdp_cap = np_gapminder[:,6]
# make a line plot of gdp_cap on the x-axis and life_exp on the y-axis
plt.plot(gdp_cap, life_exp)
# display the plot
plt.show()
# make a scatter plot of gdp_cap on the x-axis and life_exp on the y-axis
plt.scatter(gdp_cap, life_exp)
# display the plot
plt.show()
