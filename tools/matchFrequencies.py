# This file will hold several functions whose purpose is to match frequencies to english
# letter frequency.
import sys
import collections
import operator

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphFreq = [0.08167, 0.01492, 0.02782, .04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02361, 0.00150, 0.01974, 0.00074]
alphFreqDict = collections.defaultdict(float)
for i in range(0, len(alphFreq)):
    alphFreqDict[alph[i]] = alphFreq[i]

def getFreq(fileName):
    print("getting frequencies for ciphertext in " + fileName)
    readFile = open(fileName, 'r')
    lines = []
    for line in readFile:
        lines.append(line)
    if len(lines) > 1:
        print("Your file had newlines in it, I'm not dealing with those, " \
              "do it yourself (or remove the newlines)")
        sys.exit()
    freqs = collections.defaultdict(float)
    for c in lines[0]:
        freqs[c] += 1 #Count the characters
    for i in range(0,26):
        freqs[alph[i]] /= len(lines[0])
    return freqs

def matchFreq(fileName):
    freqs = getFreq(fileName)
    print(freqs)
    print(sum(freqs.values()))
    englishDist = 0.0
    for c in alph:
        englishDist += (freqs[c] - alphFreqDict[c]) ** 2
    print("English distance is %.5f" % englishDist)
    sortedAlphFreqs = sorted(alphFreqDict.items(), key=operator.itemgetter(1), reverse = True)
    sortedFreqs = sorted(freqs.items(), key=operator.itemgetter(1), reverse = True)
    print(type(sortedFreqs[0]))
    sortedDist = 0.0
    for i in range(0,26):
        sortedDist += (sortedFreqs[i][1] - sortedAlphFreqs[i][1]) ** 2
    print("Sorted distance is %.5f" % sortedDist)
    
matchFreq(sys.argv[1])
