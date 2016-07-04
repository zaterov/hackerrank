#!/usr/bin/env python

#  s = 'qA2'
s = raw_input()
tests = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']


def check(s, test):
    for c in s:
        if getattr(c, test)():
            return True
        return False

if 0 <= len(s) <= 1000:
    for test in tests:
        print(check(s, test))


'''
from the discussions:
    'any'!  as in print any(c.isalnum()  for c in str)

# uses all five string methods on each character in input string
# prints True if at least one character made the method return True
print "\n".join([str(i) for i in (any(i) for i in (list(zip(*[[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in raw_input()]))))])

or a little less cluttered (perhaps):

    # user input
    s = raw_input()

    # uses all 5 methods on each character and creates a list for each,
    # containing the results of each method used on the character.
    newList = [[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in s]

    # rotates lists clockwise to get lists of each method instead
    rotated = list(zip(*newList))

    # prints whether or not a True is present for each List
    print "\n".join([str(i) for i in (any(i) for i in rotated)])

