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


