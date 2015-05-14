""" This module holds several functions whose purpose is to identify ciphers from cipherText."""
import sys
import collections
import operator
import stringOps

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphFreq = [0.08167, 0.01492, 0.02782, .04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02361, 0.00150, 0.01974, 0.00074]
alphFreqDict = collections.defaultdict(float)
for i in range(0, len(alphFreq)):
    alphFreqDict[alph[i]] = alphFreq[i]

def getFreq(fileName):
    """Gets some frequencies from a file. Not really necessary."""
    return getStrFreq(getString(filename))

def getString(fileName):
    """Gets a string from a file"""
    print("getting string from file " + fileName)
    readFile = open(fileName, 'r')
    lines = []
    for line in readFile:
        lines.append(line)
    if len(lines) > 1:
        print("Your file had newlines in it, I'm not dealing with those, " \
              "do it yourself (or remove the newlines)")
        sys.exit()
    return lines[0]

def getStrFreq(string):
    """Gets the string frequencies for a given string"""
    freqs = collections.defaultdict(float)
    for c in string:
        freqs[c] += 1 # Count the characters
    for i in range(0,26):
        freqs[alph[i]] /= len(string) # Normalize that shit
    return freqs

def matchFreq(fileName):
    """Don't mind this, just for me -Ken"""
    string = getString(fileName)
    freqs = getStrFreq(string)
    englDist = englishDist(string)
    print("English distance is %.5f" % englDist)
    sortedAlphFreqs = sorted(alphFreqDict.items(), key=operator.itemgetter(1), reverse = True)
    sortedFreqs = sorted(freqs.items(), key=operator.itemgetter(1), reverse = True)
    sortedDist = 0.0
    for i in range(0,26):
        sortedDist += (sortedFreqs[i][1] - sortedAlphFreqs[i][1]) ** 2
    print("Sorted distance is %.5f" % sortedDist)
    vigDist = vigenereDist(string)
    print("Vigenere distance is %.5f" % vigDist)
    return

def vigenereDist(string):
    """Calculates and returns the vigenere distance for a given string"""
    ans = 9999.99
    for nth in range(6, 10):
        tempAns = 0.0
        strings = []
        for start in range (0, i):
            nthString = stringOps.everyNth(string, start, nth)
            strings.append(nthString)
            tempAns += shiftedDist(nthString)
        if tempAns < ans:
            ans = tempAns
            print("nth was %.0f" % nth)
    return ans

def shiftedDist(string):
    """Calculates the minimum distance for a string with any caesar shift"""
    ans = 9999.99 # Will get replaced, just needed a big number
    for shift in range(0, 26):
        shiftedStr = stringOps.shiftString(string, shift)
        dist = englishDist(shiftedStr)
        if dist < ans:
            ans = dist
    return ans

def englishDist(string):
    """Calculates the distance of a string from english letter frequencies"""
    englishDist = 0.0
    freqs = getStrFreq(string)
    for c in alph:
        englishDist += (freqs[c] - alphFreqDict[c]) ** 2
    return englishDist

def fromFile(function, fileName):
    """Performs string function on file"""
    print('fileName is ' + fileName)
    string = getString(fileName)
    return function(fileName)

matchFreq(sys.argv[1])
