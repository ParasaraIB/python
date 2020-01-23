# === Nested functions I ===

# define three_shouts
def three_shouts(word1, word2, word3) :
    """Returns a tuple of strings concatenated with '!!!'."""
    # define inner
    def inner(word) :
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'
    # return a tuple of strings
    return(inner(word1), inner(word2), inner(word3))
# call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

# === Nested functions II ===

# define echo
def echo(n) :
    """Return the inner_echo function."""
    # define inner_echo
    def inner_echo(word1) :
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word
    # return inner_echo
    return inner_echo
# call echo: twice
twice = echo(2)
# call echo: thrice
thrice = echo(3)
# call twice() and thrice() then print
print(twice('hello'), thrice('hello'))

# === The keyword nonlocal and nested functions ===

# define echo_shout()
def echo_shout(word) :
    """Change the value of a nonlocal variable."""
    # concatenate word with itself: echo_word
    echo_word = word + word
    # print echo_word
    print(echo_word)
    # define inner function shout()
    def shout() :
        """"Alter a variable in the enclosing scope."""
        # use echo_word in nonlocal scope
        nonlocal echo_word
        # change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    # call function shout()
    shout()
    # print echo_word
    print(echo_word)
# call function echo_shout() with argument 'hello'
echo_shout('hello')
