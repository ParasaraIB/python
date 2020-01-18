# Customizations

# imprt different file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r"D:\Data Science\Data Camp\Python Intermediate")
# import numpy
import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
# load the data
import pandas as pd
gapminder = pd.read_csv("gapminder.csv")
# color customizations based on continent
gapminder.replace(['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'], ['red', 'green', 'blue', 'yellow', 'black'], inplace = True)
# store gapminder as numpy array
np_gapminder = np.array(gapminder)
# define each attribute according to its data type
country = np_gapminder[:,1]
population = np_gapminder[:,3].astype(np.float)
continent = np_gapminder[:,4]
life_exp = np_gapminder[:,5].astype(np.float)
gdp_cap = np_gapminder[:,6].astype(np.float)
# set the population as the dots size of the scatter
population = population * 2 / (10 ** 6)
# plot the graph with color customizations and alpha (opacity) set at 0.8
plt.scatter(gdp_cap, life_exp, s = population, c = continent, alpha = 0.8)
# basic scatter plot using log scale at x-axis
plt.xscale('log')
# add axis label
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
# add title to the graph
plt.title('World Development in 2007')
# change the ticks on the x-axis
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])
# add India label at the corresponding coordinate
x1 = gdp_cap[country == 'India']
y1 = life_exp[country == 'India']
plt.text(x1, y1, 'India')
# add China label at the corresponding coordinate
x2 = gdp_cap[country == 'China']
y2 = life_exp[country == 'China']
plt.text(x2, y2, 'China')
# add United States label at the corresponding coordinate
x3 = gdp_cap[country == 'United States']
y3 = life_exp[country == 'United States']
plt.text(x3, y3, 'United States')
# add Indonesia label at the corresponding coordinate
x4 = gdp_cap[country == 'Indonesia']
y4 = life_exp[country == 'Indonesia']
plt.text(x4, y4, 'Indonesia')
# add grid to the plot
plt.grid(True)
# display the plot
plt.show()
