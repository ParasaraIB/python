# === Functions with one default argument ===

# define shout_echo
def shout_echo(word1, echo = 1) :
    """Concatenate echo copies of word1 and three exclamation marks at the end of the string."""
    # concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # return shout_word
    return shout_word
# call shout_echo() with 'Hey': no_echo
no_echo = shout_echo('Hey')
# call shout_echo() with 'Hey' and echo = 5: with_echo
with_echo = shout_echo('Hey', echo = 5)
# print no_echo dan with_echo
print(no_echo)
print(with_echo)

# === Functions with multiple default arguments ===

# define shout_echo
def shout_echo(word1, echo = 1, intense = False) :
    """Concatenate echo copies of word1 and three exclamation marks at the end of the string."""
    # concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # make echo_word uppercase if intense is True
    if intense is True :
        # make uppercase and concatenate '!!!' : echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else :
        # concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'
    # return echo_word_new
    return echo_word_new
# call shout_echo() with 'Hey', echo = 5 and intense = True: with_big_echo
with_big_echo = shout_echo('Hey', echo = 5, intense = True)
# call shout_echo() with 'Hey' and intense = True: big_no_echo
big_no_echo = shout_echo('Hey', intense = True)
# print values
print(with_big_echo)
print(big_no_echo)

# === Functions with variable-length arguments (*args) ===

# define gibberish
def gibberish(*args) :
    """Concatenate strings in *args together."""
    # initialize an empty string: hodgepodge
    hodgepodge = ''
    # concatenate the strings in args
    for word in args :
        hodgepodge += word
    # return hodgepodge
    return hodgepodge
# call gibberish() with one string: one_word
one_word = gibberish('luke')
# call gibberish() with five strings: many_words
many_words = gibberish('luke', 'leia', 'han', 'obi', 'darth')
# print one_word and many_words
print(one_word)
print(many_words)

# === Functions with variable-length keyword arguments (**kwargs) ===

# define report_status
def report_status(**kwargs) :
    """Print out the status of a movie character."""
    print('\nBEGIN: REPORT\n')
    # iterate over the key-value pairs of kwargs
    for keys, values in kwargs.items() :
        # print out the keys and values, separated by a colon ':'
        print(keys + ': ' + values)
    print('\nEND REPORT')
# first call to report_status()
report_status(name = 'luke', affiliation = 'jedi', status = 'missing')
# second call to report_status()
report_status(name = 'anakin', affiliation = 'sith lord', status = 'deceased')
