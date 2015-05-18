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
from decrypt import decColumn
import bisect
import random
from copy import copy
from pycipher import ColTrans
from scrapeFreq import get_freqs
from encode import encColumn

words = ['THE', 'BE', 'TO', 'OF', 'AND', 'IN', 'THAT', 'HAVE', 'IT',
          'FOR', 'NOT', 'ON', 'WITH', 'HE', 'AS', 'YOU', 'DO', 'AT']

diFreq = collections.defaultdict(float)
diFile = open('bigrams.txt', 'r')
mySum = 0.0
for line in diFile:
    count = int(line[3:len(line) - 2])
    mySum += float(count)

diFile = open('bigrams.txt', 'r')
    
for line in diFile:
    digram = line[0] + line[1]
    count = int(line[3:len(line) - 2])
    diFreq[digram] = float(count)/mySum

def getFirstLetters(words):
    ans = ""
    for word in words:
        ans += word[0]
    return set(ans)

firstLetters = getFirstLetters(words)
l2w = filter(lambda x: len(x) == 2, words)
l3w = filter(lambda x: len(x) == 3, words)
l4w = filter(lambda x: len(x) == 4, words)

def checkWords(string, words, pos, wordLen):
    if string[pos:pos+wordLen] in words:
        return True
    else: return False

def findWords(string, firstLetters, len2words, len3words, len4words):
    ans = 0
    for i in range(0, len(string)):
        if chr(string[i]) in firstLetters:
            if checkWords(string, len2words, i, 2):
                ans += 1
            elif checkWords(string, len3words, i, 3):
                ans += 2
            elif checkWords(string, len4words, i, 4):
                ans += 3
    return ans

def findLetter(string, letter):
    ans = []
    for i in range(0,len(string)):
        if string[i] == letter:
            ans.append(i)
    return ans

def modArray(arr, mod):
    newArr = []
    for i in range(0, len(arr)):
        newArr.append(arr[i] % mod)
    return newArr

def numMatches(arr1, arr2):
    ans = 0
    for el1 in arr1:
        for el2 in arr2:
            if el1 == el2:
                ans += 1
    return ans

def guessColumns(cText, word):
    letterpos = []
    for c in word:
        letterpos.append(findLetter(cText, c))
    for i in range (5,11):
        for j in range(0, len(letterpos)):
            letterpos[j] = modArray(letterpos[j], len(cText)/i)
        print numMatches(letterpos[0], letterpos[1])
    return 0

def guessColumns(cText):
    word = 'BE'
    bestThes = 0
    ans = 0
    for cols in range(5,21):
        thes = 0 # number of the's
        collen = int(math.ceil(len(cText)/float(cols)))
        shortcols = cols - (len(cText) % cols)
        if shortcols > 4: shortcols = 4 # blehhhh
        if len(cText) % cols == 0: shortcols = 0
        for i in range(0, len(cText)):
            if cText[i] in word and \
               (wordSearch(cText, word, i, collen, shortcols, [])):
                thes += 1
        print("{0}: {1}, {2} short columns".format(cols, thes, shortcols))

def search(string, letter, pos, colLength, shortColLeft, found):
    """
    Performs a (recursive) search of the string starting
    from pos for letter, allowing for columns exactly 1
    character shorter than colLength
    """
    if pos >= len(string):
        return 0
    if shortColLeft != 0:
        if string[pos] == letter and pos not in found:
            found.append(pos)
            return 1 + search(string, letter, pos + colLength,
                              colLength, shortColLeft, found) \
                + search(string, letter, pos + colLength - 1,
                         colLength, shortColLeft - 1, found)
        else:
            return search(string, letter, pos + colLength,
                          colLength, shortColLeft, found) \
                + search(string, letter, pos + colLength - 1,
                         colLength, shortColLeft - 1, found)
    else:
        if string[pos] == letter and pos not in found:
            found.append(pos)
            return 1 + search(string, letter, pos + colLength,
                              colLength, shortColLeft, found)
        else:
            return search(string, letter, pos + colLength,
                          colLength, shortColLeft, found)
            
def wordSearch(string, letters, pos, colLength, shortColLeft, found):
    """
    Performs a (recursive) search of the string starting
    from pos for letters, allowing for columns exactly 1
    character shorter than colLength. Returns true if the
    word is more or less found colLength apart, otherwise
    false
    """
    if allLettersInFound(letters, found):
        return True
    if pos >= len(string):
        return False # We've gotten to end of string without finding word
    if shortColLeft != 0:
        if string[pos] in letters and string[pos] not in found:
            found.append(string[pos])
            return wordSearch(string, letters, pos + colLength,
                              colLength, shortColLeft, found) \
                or wordSearch(string, letters, pos + colLength - 1,
                         colLength, shortColLeft - 1, found)
        else:
            return wordSearch(string, letters, pos + colLength,
                          colLength, shortColLeft, found) \
                or wordSearch(string, letters, pos + colLength - 1,
                         colLength, shortColLeft - 1, found)
    else:
        if string[pos] in letters and string[pos] not in found:
            found.append(string[pos])
            return wordSearch(string, letters, pos + colLength,
                              colLength, shortColLeft, found)
        else:
            return wordSearch(string, letters, pos + colLength,
                          colLength, shortColLeft, found)

def allLettersInFound(letters, found):
    for letter in letters:
        if letter not in found:
            return False
    return True

def genRandKey(numCol):
    ans = []
    for i in range(0, numCol):
        ans.append(i)
    random.shuffle(ans)
    return ans

def breed(key1, key2, mutFact):
    ans = []
    for i in range(0, len(key1)):
        randbit = random.randrange(0,2)
        if randbit:
            ans.append(key1[i])
        else:
            ans.append(key2[i])
        if random.randrange(0, 100) < mutFact:
            swap(ans, random.randrange(0, i), i)
    return ans

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

def genSolve(cText, words, numCol):
    random.seed()
    firstLetters = getFirstLetters(words)
    l2w = filter(lambda x: len(x) == 2, words)
    l3w = filter(lambda x: len(x) == 3, words)
    l4w = filter(lambda x: len(x) == 4, words)
    generation = 0
    keys = []
    for i in range(0, 10):
        key = genRandKey(numCol)
        print(key)
        keys.append(key)
    wordsFound = [0]*len(keys)
    print(wordsFound[0])
    while generation < 2000:
        if (generation % 1000) == 0:
            print("Generation: {0}, words: {1}".format(generation,
                                                    wordsFound[0]))
        wordsFound = [0]*len(keys)
        for i in range(0, len(keys)):
            key = keys[i]
            pText = decColumn(cText, key)
            numWords = findWords(pText, firstLetters, l2w, l3w, l4w)
            if numWords > 2:
                print(pText)
                print(keys[i])
                print(numWords)
            wordsFound[i] = numWords
        sortThings(wordsFound, keys, 0, len(wordsFound) - 1)
        newKeys = []
        for i in range(0, 10):
            par1 = random.randrange(0, 5) * 2
            par2 = random.randrange(0, 5) * 2 + 1
            newKeys.append(breed(keys[par1], keys[par2], 0))
        keys = newKeys
        print(keys)
        generation += 1

def countDigrams(string):
    digrams = collections.defaultdict(float)
    for i in range(0, len(string) - 1):
        c1 = string[i]
        c2 = string[i+1]
        digrams[c1+c2] += 1.0/len(string)
    return digrams

def score(digrams):
    ans = 0.0
    for digram in digrams.keys():
        ans += (digrams[digram] - diFreq[digram])**2
    return ans

def newKey(cText, key, temp, oldScore):
    randint1 = random.randrange(0, len(key))
    randint2 = random.randrange(0, len(key))
    newKey = copy(key)
    swap([newKey], randint1, randint2)
    newPText = decColumn(cText, newKey)
    newScore = score(countDigrams(newPText))
    dif = newScore - oldScore
    if dif < 0:
        return newKey
    else:
        if shouldJump(dif, temp):
            return newKey
        else:
            return key

def shouldJump(dif, temp):
    fact = math.exp(-1000 * float(dif) / temp)
    if random.random() < fact:
        return True
    else:
        return False
    
def swap(arrs, ind1, ind2):
    for arr in arrs:
        temp = arr[ind1]
        arr[ind1] = arr[ind2]
        arr[ind2] = temp

def saSolve(cText, numCol):
    random.seed()
    key = genRandKey(numCol)
    pText = decColumn(cText, key)
    newScore = score(countDigrams(pText))
    bestScore = score
    temp = 100.0
    while temp > 0:
        key = newKey(cText, key, temp, newScore)
        pText = decColumn(cText, key)
        newScore = score(countDigrams(pText))
        if newScore < bestScore:
            print(pText)
            print(key)
            print(newScore)
            bestScore = newScore
        temp -= 0.01
    return pText


pText = 'IfplaintextisstoredinacomputerfileandthesituationofautomaticallymadebackupfilesgeneratedduringprogramexecutionmustbeincludedhereevenifinvisibletotheuserthestoragemediaalongwiththeentirecomputeranditscomponentsmustbesecureSensitivedataissometimesprocessedoncomputerswhosemassstorageisremovableinwhichcasephysicalsecurityoftheremoveddiskisseparatelyvitalInthecaseofsecuringacomputerusefulasopposedtohandwavingsecuritymustbephysicalegagainstburglarybrazenremovalundercoverofsupposedrepairinstallationofcovertmonitoringdevicesetcaswellasvirtualegoperatingsystemmodificationillicitnetworkaccessTrojanprogramsThewideavailabilityofkeydriveswhichcanplugintomostmoderncomputersandstorelargequantitiesofdataposesanotherseveresecurityheadacheAspyperhapsposingasacleaningpersoncouldeasilyconcealoneandevenswallowitifnecessary'.upper()

myKey = "ABCDEFGHIJKLMNOP"
myKey2 = [0,1,2,3]
cText = encColumn(pText,myKey2)
cText2 = ColTrans(myKey).encipher(pText)

pText2 = decColumn(cText,myKey2)

print(cText)
print(cText2)
print("===========")
print(pText)
print(pText2)
print("===========")

sortThings(myKey, myKey2, 0, len(myKey)-1)
print(score(countDigrams(saSolve(cText2, 16))))
