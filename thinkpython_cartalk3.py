# -*- coding: utf-8 -*-

from __future__ import print_function, division

"""
Created on Tue Oct  9 20:11:50 2018

@author: Somesh
"""

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

“Recently I had a visit with my mom and we realized that the two digits that 
makeup my age when reversed resulted in her age.  For example, if she’s 73, 
I’m 37.  We wondered how often this has happened over the years but we got 
side tracked with other topics and we never came up with an answer.

“When I got home I figured out that the digits of our ages have been reversible
 six times so far.  I also figured out that if we’re lucky it would happen again
 in a few years, and if we’re really lucky it would happen one more time after 
 that. In other words, it wouldhave happened 8 times over all. So the question is,
 how old am I now?”

"""

def str_fill(i, n):
    """Returns i as a string with at least n digits.

    i: int
    n: int length

    returns: string
    """
    return str(i).zfill(n)


def are_reversed(i, j):
    """Checks if i and j are the reverse of each other.

    i: int
    j: int

    returns:bool
    """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):
    """Counts the number of palindromic ages.

    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given the difference in age.

    diff: int difference in ages
    flag: bool, if True, prints the details
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff

        # assuming that mother and daughter don't have the same birthday,
        # they have two chances per year to have palindromic ages.
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """Finds age differences that satisfy the problem.

    Enumerates the possible differences in age between mother
    and daughter, and for each difference, counts the number of times
    over their lives they will have ages that are the reverse of
    each other.
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1

print('diff  #instances')
check_diffs()

print()
print('daughter  mother')
num_instances(18, True)