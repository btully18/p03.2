"""
Problem:

    In another popular word game, players are tasked with making the longest
    words possible using a set of letters.  The score for each word is given
    calculated on the following basis:

    * Each use of q, x, y or z is awarded 2 points.
    * No points are awarded for the use of vowels.
    * All other letters score 1 point.

    For example, "question" would score 5 points: 2 for q, 1 each for s, t and n.

    The function 'scorer' takes a word as input, and should print the score
    for that word.

Tests:

    >>> scorer("question")
    5
    >>> scorer("examples")
    6
    >>> scorer("xylophone")
    8
    >>> scorer("tesselate")
    5

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def scorer(word):
    count = 0
    for char in word:
        count = count + 1
        if char in "qxyz":
            count = count + 1
        elif char in "aeiou":
            count = count - 1
    print(count)
