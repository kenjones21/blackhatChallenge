"""
This module will hold methods for decrypting texts if you know the key. It will not have methods for
breaking any of the ciphers (though you could certainly use these in doing so)
"""

import sys
import collections
import stringOps
import matchFrequencies

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
    decKey = matInverse(key);
    numText = map(ord, cText)
    # Do matrix multiplication here
    return 0

def matInverse(matrix):
    det = inverse((matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]))
    ans = [[0,0],[0,0]]
    ans[0][0] = (det * matrix[1][1]) % 26
    ans[1][1] = (det * matrix[0][0]) % 26
    ans[1][0] = (det * -matrix[0][1]) % 26
    ans[0][1] = (det * -matrix[1][0]) % 26
    return ans

def inverse(num):
    """Calculates the (multiplicative) inverse of a number mod 26"""
    for i in range(0,26): # I know, I know, could use EA or something, lazy. 
        if (i * num) % 26 == 1:
            return i
    print("No inverse for this number!")
    return 0 # Should make things obvious for our purposes. 

print(matInverse([[3,2],[3,5]]))
