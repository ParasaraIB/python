# === Writing a lambda function ===

# define echo_word as lambda function: echo_word
echo_word = (lambda word1, echo : word1 * echo)
# call echo_word: result
result = echo_word('hey', 5)
# print result
print(result)

# === Map() and lambda functions ===

# create a list of strings: spells
spells = ['protego', 'accio', 'expecto patronum', 'legilimens']
# use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)
# convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)
# print the result
print(shout_spells_list)

# === Filter() and lambda functions ===

# create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
# use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)
# convert result to a list: result_list
result_list = list(result)
# print result
print(result_list)

# === Reduce() and lambda functions ===

# import reduce from functools
from functools import reduce
# create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon' ,'rickon']
# use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2 : item1 + item2, stark)
# print the result
print(result)
