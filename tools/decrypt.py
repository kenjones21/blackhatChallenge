"""
This module will hold methods for decrypting texts if you know the key. It will not have methods for
breaking any of the ciphers (though you could certainly use these in doing so)
"""

import sys
import collections
import stringOps
import matchFrequencies
import numpy
from colorama import Fore
import operator

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def sortThings(masterList, slaveList, a, b):
    wasString = False
    if type(masterList) == str:
        wasString = True
        masterList = bytearray(masterList)
    if b < a:
        pivot = a
        pivVal = masterList[a]
        swap([masterList, slaveList], a, b)
        index = a
        for i in range(a, b):
            if masterList[i] >= pivVal:
                swap([masterList, slaveList], i, index)
                index += 1
        swap([masterList, slaveList], index, b)
        sortThings(masterList, slaveList, a, index - 1)
        sortThings(masterList, slaveList, index + 1, b)
    if wasString:
        masterList = str(masterList)

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
    numText = map(ord, cText)
    numText = map(lambda x: x - ord('A'), numText)
    for i in range(0,len(cText)/2):
        a = i*2
        b = a + 1
        temp = numpy.matrix([[numText[a]],[numText[b]]])
        vec = numpy.mod(decKey * temp, 26) # Mod that shit 26
        vec = numpy.asarray(vec).reshape(-1) # Reshape array
        vec = map(lambda x: chr(x + ord('A')), vec) # To characters!
        ans += vec[0] # Have to do it elementwise for reasons
        ans += vec[1] # This was way too long a for loop
    return ans

def decColumn(cText, key):
    ans = ""
    decKey = []
    for i in range(0, len(key)):
        decKey.append(-1)
    for i in range(0, len(key)):
        decKey[key[i]] = i
    numCol = len(key)
    longCol = len(cText) % numCol
    shortCol = numCol - longCol
    shortLength = len(cText) / numCol
    longLength = shortLength + 1
    cols = []
    char = 0
    for i in range(0, len(key)):
        cols.append("")
    for i in range(0, len(key)):
        if decKey[i] < longCol:
            for j in range(char,char+longLength):
                cols[decKey[i]] += cText[char]
                char += 1
        else:
            for j in range(char,char+shortLength):
                cols[decKey[i]] += cText[char]
                char += 1
    sortThings(decKey, cols, 0, len(key))
    for i in range(0, len(cText)):
        ans += cols[i % len(key)][i / len(key)]
    return ans

def matInverse(matrix):
    det = inverse((matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]))
    ans = [[0,0],[0,0]]
    ans[0][0] = (det * matrix[1][1]) % 26
    ans[1][1] = (det * matrix[0][0]) % 26
    ans[1][0] = (det * -matrix[1][0]) % 26
    ans[0][1] = (det * -matrix[0][1]) % 26
    return ans

def inverse(num, output=True):
    """Calculates the (multiplicative) inverse of a number mod 26"""
    for i in range(0,26): # I know, I know, could use EA or something, lazy. 
        if (i * num) % 26 == 1:
            return i
    if(output):
        print(Fore.RED + "No inverse for this number!" + Fore.RESET)
    return 0 # Should make things obvious for our purposes. 

def decPlayfair(cText, key):
    keyDict = collections.defaultdict(list)
    pText = ""
    for i in range (0, len(key)):
        keyDict[key[i]] = [i/5, i%5]
    for i in range(0, len(cText)/2):
        a = cText[i*2]
        b = cText[i*2+1]
        rowA = keyDict[a][0]
        rowB = keyDict[b][0]
        colA = keyDict[a][1]
        colB = keyDict[b][1]
        if rowA == rowB:
            newColA = (colA - 1) % 5
            newColB = (colB - 1) % 5
            pa = key[(rowA*5 + newColA) % 25]
            pb = key[(rowB*5 + newColB) % 25]
            if pa != 'X': pText += pa
            if pb != 'X': pText += pb
        elif colA == colB:
            newRowA = (rowA - 1) % 5
            newRowB = (rowB - 1) % 5
            pa = key[(newRowA*5 + colA) % 25]
            pb = key[(newRowB*5 + colB) % 25]
            if pa != 'X': pText += pa
            if pb != 'X': pText += pb
        else:
            pa = key[(rowA*5 + colB)]
            pb = key[(rowB*5 + colA)]
            if pa != 'X': pText += pa
            if pb != 'X': pText += pb
    return pText

key = 'PLAYFIREXMBCDGHKNOQSTUVWZ'
cText = 'BMODZBXDNABEKUDMUIXMMOUVIF'
print(decPlayfair(cText, key))
