# === Strings in Python ===

object1 = print('data' + 'analysis')
object2 = print(1 * 3)
object3 = print('1' * 3)

# === Recapping built-in functions ===

x = 4.89
print(type(x))
y1 = print(type(str(x)))
y2 = print(type(print(x)))

# === Write a simple function ===

# define the function shout
def shout() :
    """Print a string with three exclamation marks"""
    # concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'
    # print shout_word
    print(shout_word)
# call shout
shout()

# === Single parameter functions ===

# define shout with the parameter, word
def shout(word) :
    """Print a string with three exclamation marks"""
    # concatenate the strings: shout_word
    shout_word = word + '!!!'
    # print shout_word
    print(shout_word)
# call shout with the string 'congratulations'
shout('congratulations')

# === Functions that return single values ===

# define shout with the parameter, word
def shout(word) :
    """Return a string with three exclamation marks"""
    # concatenate the strings: shout_word
    shout_word = word + '!!!'
    # replace print with return
    return(shout_word)
# pass 'congratulations' to shout: yell
yell = shout('congratulations')
# print yell
print(yell)

# === Functions with multiple parameters ===

# define shout with parameters word1 and word2
def shout(word1, word2) :
    """Concatenate strings with three exclamation marks"""
    # concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    # concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    # concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2
    # return new_shout
    return new_shout
# pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')
# print yell
print(yell)

# === A brief introduction to tuples ===

# define nums
nums = (3, 4, 6)
# unpack nums into num1, num2, and num3
num1, num2, num3 = nums
# construct even_nums
even_nums = (2, num2, num3)
# print even_nums
print(even_nums)

# === Functions that return multiple values ===

# define shout_all with parameters word1 and word2
def shout_all(word1, word2) :
    # concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    # concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    # construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)
    # return shout_words
    return shout_words
# pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')
# print yell1 and yell2
print(yell1)
print(yell2)

# === Bringing it all together(1) ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Data Science Toolbox 1')
# import pandas
import pandas as pd
# import twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')
# initialize an empty dictionary: langs_count
langs_count = {}
# extract column from DataFrame: col
col = df['lang']
# iterate ove lang column in DataFrame
for entry in col :
    # if the language is in langs_count, add 1
    if entry in langs_count.keys() :
        langs_count[entry] += 1
    # else add the language to langs_count, set the value to 1
    else :
        langs_count[entry] = 1
# print the populated dictionary
print(langs_count)

# === Bringing it all together (2) ===

# define count_entries()
def count_entries(df, col_name) :
    """Return a dictionary with counts of occurences as value for each key."""
    # initialize an empty dictionary: langs_count
    langs_count = {}
    # extract column from DataFrame: col
    col = df[col_name]
    # iterate over lang column in DataFrame
    for entry in col:
        # if the language is in the langs_count, add 1
        if entry in langs_count.keys() :
            langs_count[entry] += 1
        # else add the language to langs_count, set the value to 1
        else :
            langs_count[entry] = 1
    # return the langs_count dictionary
    return langs_count
# call count_entries(): result
result = count_entries(df, 'lang')
# print the result
print(result)
