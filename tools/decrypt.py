"""
This module will hold methods for decrypting texts if you know the key. It will not have methods for
breaking any of the ciphers (though you could certainly use these in doing so)
"""

import sys
import collections
import stringOps
import matchFrequencies
import numpy

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decSubs(cText, key):
    ans = ""
    subsDict = collections.defaultdict(str)
    for i in range(0,26):
        subsDict[alph[i]] = key[i]
    for i in range(0, len(cText)):
        ans += subsDict[cText[i]]
    return ans

def decVigenere(cText, key):
    ans = ""
    shifts = []
    A = ord('A')
    for i in range(0, len(key)):
        shifts.append(ord(key[i]) - A)
        shifts[i] = (26 - shifts[i]) % 26 # Key used to encrypt, not decrypt
    for c in range(0, len(cText)):
        ans += chr((ord(cText[c]) - A + shifts[c % len(key)]) % 26 + A)
    return ans

def decHill(cText, key):
    ans = ""
    decKey = numpy.matrix(matInverse(key));
    print(decKey)
    numText = map(ord, cText)
    numText = map(lambda x: x - ord('A'), numText)
    for i in range(0,len(cText)/2):
        a = i*2
        b = a + 1
        temp = numpy.matrix([[numText[a]],[numText[b]]])
        vec = numpy.mod(decKey * temp, 26)
        vec = numpy.asarray(vec).reshape(-1)
        vec = map(lambda x: chr(x + ord('A')), vec)
        ans += vec[0]
        ans += vec[1] # This was way too long a for loop
    return ans

def matInverse(matrix):
    det = inverse((matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]))
    ans = [[0,0],[0,0]]
    ans[0][0] = (det * matrix[1][1]) % 26
    ans[1][1] = (det * matrix[0][0]) % 26
    ans[1][0] = (det * -matrix[1][0]) % 26
    ans[0][1] = (det * -matrix[0][1]) % 26
    return ans

def inverse(num):
    """Calculates the (multiplicative) inverse of a number mod 26"""
    for i in range(0,26): # I know, I know, could use EA or something, lazy. 
        if (i * num) % 26 == 1:
            return i
    print("No inverse for this number!")
    return 0 # Should make things obvious for our purposes. 
