import collections
import math

quadFreq = collections.defaultdict(float)
quadFile = open('quadgrams.txt', 'r')
mySum = 0.0
for line in quadFile:
    count = int(line[5:len(line) - 1])
    mySum += float(count)

quadFile = open('quadgrams.txt', 'r')
    
for line in quadFile:
    quadGram = line[0:4]
    count = int(line[5:len(line) - 1])
    quadFreq[quadGram] = float(count)/mySum

diFreq = collections.defaultdict(float)
diFile = open('bigrams.txt', 'r')
mySum = 0.0
for line in diFile:
    count = int(line[3:len(line) - 2])
    mySum += float(count)

diFile = open('bigrams.txt', 'r')
    
for line in diFile:
    diGram = line[0:2]
    count = int(line[3:len(line) - 2])
    diFreq[diGram] = float(count)/mySum

def countDigrams(string):
    digrams = collections.defaultdict(float)
    for i in range(0, len(string) - 1):
        c1 = string[i]
        c2 = string[i+1]
        digrams[c1+c2] += 1.0/len(string)
    return digrams

def score(quadgrams):
    ans = 0.0
    for quadgram in quadgrams:
        if quadgram not in quadFreq:
            ans += -23
        else: 
            ans += math.log(quadFreq[quadgram])
    return ans

def countNGrams(string, n):
    ngrams = collections.defaultdict(float)
    for i in range(0, len(string) - n):
        c1 = string[i:i+n]
        ngrams[c1] += 1.0/len(string)
    return ngrams

def diScore(digrams):
    ans = 0.0
    for digram in digrams:
        if digram not in diFreq:
            ans += -23
        else: 
            ans += math.log(diFreq[digram])
    return ans

def countDigramsPF(string):
    digrams = collections.defaultdict(float)
    for i in range(0, len(string)/2):
        c1 = string[2*i]
        c2 = string[2*i+1]
        digrams[c1+c2] += 1.0/len(string)
    return digrams
