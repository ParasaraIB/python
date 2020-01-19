# Dictionaries

# definition of countries and capital
countries = ['japan', 'korea', 'china', 'iran']
capitals = ['tokyo', 'seoul', 'beijing', 'teheran']
# get index of china
ind_chn = countries.index('china')
# print out the capital of china
print(capitals[ind_chn])
# create dictionaries from string in countries and capitals
asia = {'japan':'tokyo', 'korea':'seoul', 'china':'beijing', 'iran':'teheran'}
# print asia
print(asia)
# print the keys in asia
print(asia.keys())
# print out the value that belongs to key 'iran'
print(asia['iran'])
# add india to asia
asia['india'] = 'new delhi'
# print out india in asia to check it is successfully appended into the dictionary
print('india' in asia)
# add indonesia to asia
asia['indonesia'] = 'jakarta'
# print asia
print(asia)
# definition of dictionary
europe = {'hungary':'london', 
'finland':'helsinki', 
'austria':'vienna', 
'romania':'bucharest', 
'ukraine':'kiev', 
'canada':'ontario'}
# update capital of hungary
europe['hungary'] = 'budapest'
# remove canada
del(europe['canada'])
# print europe
print(europe)
# dictionary of dictionaries
europe = {'hungary': {'capital':'budapest', 'population':9.95}, 
'finland':{'capital':'helsinki', 'population':5.23},
'austria':{'capital':'vienna', 'population':8.19},
'romania':{'capital':'bucharest', 'population':22.27}}
# print out the capital of finland
print(europe['finland']['capital'])
# create sub-dictionary of new
new = {'capital':'istanbul', 'population':71.19}
# add new to europe under key 'turkey'
europe['turkey'] = new
# print europe
print(europe)
