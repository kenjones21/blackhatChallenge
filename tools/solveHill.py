"""
My file for solving column transposition cipher.
The lack of padding at the end really fucks you over
Seriously fuck this
Can you even decrypt this given a key?
Yeah you can nevermind
"""

import sys
import collections
import stringOps
import matchFrequencies
import math #lol
from decrypt import decHill, inverse, matInverse
from copy import copy
from pycipher import ColTrans
import string
from charEng import countNGrams, score
from arrTools import sortThings, numMatches, modArray, swap, swapArr

def getAllKeys():
    nums = []
    keys = []
    for i in range(0, 26):
        nums.append(i)
    for a in nums:
        for b in nums:
            for c in nums:
                for d in nums:
                    if inverse(a*d - b*c, False):
                        mat = [[a,b],[c,d]]
                        keys.append(mat)
    print("Finished getting all {0} keys".format(len(keys)))
    return keys
    
keys = getAllKeys()

cText = matchFrequencies.getString(sys.argv[1])

for i in range(0, len(keys)):
    if i % 1000 == 0:
        print(i)
    pText = decHill(cText, keys[i])
    if (score(countNGrams(pText, 4))) > -6000:
        print(pText)
        print(keys[i])
