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
