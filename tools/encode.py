import sys
import collections
import stringOps
import matchFrequencies
import numpy
from colorama import Fore
import operator

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

def encColumn(pText, key):
    ans = ""
    cols = []
    for i in range(0, len(key)):
        cols.append("")
    for i in range(0, len(pText)):
        cols[key[i % len(key)]] += pText[i]
    sortThings(key, cols, 0, len(key))
    for col in cols:
        ans += col
    return ans

def encPlayfair(pText, key):
    keyDict = collections.defaultdict(list)
    cText = ""
    for i in range (0, len(key)):
        keyDict[key[i]] = [i/5, i%5]
    if len(pText) % 2 == 1:
        pText += "X"
    ans = []
    for i in range(0, len(pText)/2):
        a = pText[i*2]
        b = pText[i*2+1]
        if a == b:
            b = 'X'
            pText = pText[:2*i+1] + 'X' + pText[2*i+1:]
        rowA = keyDict[a][0]
        rowB = keyDict[b][0]
        colA = keyDict[a][1]
        colB = keyDict[b][1]
        if rowA == rowB:
            newColA = (colA + 1) % 5
            newColB = (colB + 1) % 5
            ca = key[(rowA*5 + newColA) % 25]
            cb = key[(rowB*5 + newColB) % 25]
            cText += ca
            cText += cb
        elif colA == colB:
            newRowA = (rowA + 1) % 5
            newRowB = (rowB + 1) % 5
            ca = key[(newRowA*5 + colA) % 25]
            cb = key[(newRowB*5 + colB) % 25]
            cText += ca
            cText += cb
        else:
            ca = key[(rowA*5 + colB)]
            cb = key[(rowB*5 + colA)]
            cText += ca
            cText += cb
    return cText
