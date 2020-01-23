# === Error handling with try-except ===

# define shout_echo
def shout_echo(word1, echo = 1) :
    """Concatenate echo copies of word1 and three exclamation marks at the end of the string."""
    # initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''
    # add exception handling with try-except
    try :
        # concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo
        # concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except :
        # print error massage
        print('word1 must be a string and echo must be an integer.')
    # return shout_words
    return shout_words
# call and print shout_echo
print(shout_echo('particle', echo = 'accelerator'))

# === Error handling by raising an error ===

# define shout_echo
def shout_echo(word1, echo = 1) :
    """Concatenate echo copies of word1 and three exclamation marks at the end of the string."""
    # raise an error with raise
    if echo < 0 :
        raise ValueError('echo must be greater than or equal to 0')
    # concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # return shout_word
    return shout_word
# call and print shout_echo
print(shout_echo('particle', echo = 5))
