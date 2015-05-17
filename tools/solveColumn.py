"""
My file for solving column transposition cipher.
The lack of padding at the end really fucks you over
Seriously fuck this
Can you even decrypt this given a key?
"""

import sys
import collections
import stringOps
import matchFrequencies
import math #lol

common = ['the', 'be', 'to', 'of', 'and', 'in', 'that', 'have', 'it',
          'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at']

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

cText = matchFrequencies.getString(sys.argv[1])
guessColumns(cText)
