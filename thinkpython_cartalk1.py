# -*- coding: utf-8 -*-
from __future__ import print_function, division
"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Give me a word with three consecutive double letters.  
I’ll give you a couple of wordsthat almost qualify, but don’t. 
 For example, the word committee, c-o-m-m-i-t-t-e-e.  
 It would be great except for the ‘i’ that sneaks in there.  
 Or Mississippi:  M-i-s-s-i-s-s-i-p-p-i.  If you could take out those i’s it would work.  
 But there is a word that has threeconsecutive pairs of letters and to the best of 
 my knowledge this may be the only word.Of course there are probably 500 more but 
 I can only think of one. What is the word?

"""

def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.
    
    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('C:/SomeshFolder/Studies/PGDBM/REVA/PhytonCodes/word.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')
