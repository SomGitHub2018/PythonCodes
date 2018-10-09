# -*- coding: utf-8 -*-

from __future__ import print_function, division
"""
Created on Tue Oct  9 21:27:59 2018

@author: Somesh
"""

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

A Caesar cypher is a weak form of encryption that involves “rotating” each 
letter bya fixed number of places. To rotate a letter means to shift it 
through the alphabet, wrapping aroundto the beginning if necessary, so ’A’
 rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.To rotate a word, rotate
 each letter by the same amount. For example, “cheer” rotated by 7 is 
 “jolly”and “melon” rotated by -10 is “cubed”.  In the movie2001: 
     A Space Odyssey, the ship computeris called HAL, which is IBM 
     rotated by -1.
     Write a function called rotate_word that takes a 
     string and an integer as parameters, and returns a new string 
     that contains the letters from the original string rotated by the given amount.
"""

def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))