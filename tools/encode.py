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
    key
    if len(pText) % 2 == 1:
        pText += "X"
    ans = []
    for i in range(0, len(pText)/2):
        print("I'm bored now")
