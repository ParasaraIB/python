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
