"""
Problem:

    The function 'pos_sum' takes two inputs, a word and a character.
    For every occurence of character within word, it should add up
    the position of that character.

    For example: pos_sum("hello", "l") = 2 + 3 = 5 because "l" is
    in positions 2 and 3.


Tests:

    >>> pos_sum("hello", "l")
    5
    >>> pos_sum("test", "t")
    3
    >>> pos_sum("requirements", "e")
    15

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def pos_sum(word, character):
    count = -1
    total = 0
    for char in word:
        count = count + 1
        if char == character:
            total = total + count
    print(total)

