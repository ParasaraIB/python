# === Writing an iterator to load data in chunks (1) ===

# import file direactory
import os
# get information about current direactory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Data Science Toolbox 2')
# import pandas as package
import pandas as pd
# initialize reader object: df_reader
df_reader = pd.read_csv('world_ind_pop.csv', chunksize = 10)
# print two chunks
print(next(df_reader))
print(next(df_reader))

# === Writing an iterator to load data in chunks (2) ===

# initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('world_ind_pop.csv', chunksize = 1000)
# get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)
# check out the head of the DataFrame
print(df_urb_pop.head())
# check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
# zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])
# turn zip object into list: pop_list
pop_list = list(pops)
# print pop_list
print(pop_list)

# === Writing an iterator to load data in chunks (3) ===

# block the code to running if there is any indexing warning
pd.options.mode.chained_assignment = "raise"
# initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('world_ind_pop.csv', chunksize = 1000)
# get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)
# check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB'].copy(deep = False)
# zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])
# turn zip object into list: pop_list
pop_list = list(pops)
# import matplotlib
import matplotlib.pyplot as plt
# use list comprehensions to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(pops[0] * pops[1] * 0.01) for pops in pop_list]
# plot urban population data
df_pop_ceb.plot(kind = 'scatter', x = 'Year', y = 'Total Urban Population')
plt.show()
plt.close()

# === Writing an iterator to load data in chunks (4): working with entire data chunk by chunk ===

# initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('world_ind_pop.csv', chunksize = 1000)
# initialize empty DataFrame: data
data = pd.DataFrame()
# iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader :
    # check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB'].copy(deep = False)
    # zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])
    # turn zip object into list: pop_list
    pop_list = list(pops)
    # use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pop_list]
    # append DataFrame chunk to data: data
    data = data.append(df_pop_ceb)
# plot urban population data
data.plot(kind = 'scatter', x = 'Year', y = 'Total Urban Population')
plt.show()
plt.close()

# === Writing an iterator to load data in chunks (5) ===

# define plot_pop()
def plot_pop(filename, country_code) :
    # initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize = 1000)
    # initialize empty DataFrame: data
    data = pd.DataFrame()
    # iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader :
        # check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code].copy(deep = False)
        # zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])
        # turn zip object into list: pops_list
        pops_list = list(pops)
        # use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
        # append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)
    # plot urban population data
    data.plot(kind = 'scatter', x = 'Year', y = 'Total Urban Population')
    plt.show()
    plt.close()
# set the filename: fn
fn = 'world_ind_pop.csv'
# call plot_pop for country code 'CEB'
plot_pop(fn, 'CEB')
# call plot_pop for country code 'ARB'
plot_pop(fn, 'ARB')
