import sys
import collections
import stringOps
import matchFrequencies
import math #lol
import bisect
import random
from copy import copy
import string
from encode import encPlayfair
from decrypt import decPlayfair
from charEng import countDigrams, countNGrams, score, countDigramsPF
from arrTools import sortThings, numMatches, modArray, swap, swapArr

letters = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

def genRandKey():
    letters = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    ans = []
    for i in range(0, 25):
        ans.append(letters[i])
    random.shuffle(ans)
    return ans

def randSwap(key):
    randint1 = random.randrange(0, len(key))
    randint2 = random.randrange(0, len(key))
    swap([key], randint1, randint2)

def swapRow(key):
    randint1 = random.randrange(0, 5)
    randint2 = random.randrange(0, 5)
    
def newKey(cText, key, temp, oldScore):
    newKey = copy(key)
    randSwap(newKey)
    newPText = decPlayfair(cText, newKey)
    newScore = score(countNGrams(newPText, 4))
    dif = newScore - oldScore
    if dif > 0:
        return newKey
    else:
        if shouldJump(dif, temp):
            return newKey
        else:
            return key

def shouldJump(dif, temp):
    if temp == 0:
        return False
    fact = math.exp(.15 * float(dif) / temp)
    if random.random() < fact:
        return True
    else:
        return False

def saSolve(cText):
    message1 = "Starting Simulated Anneaing Run"
    print("{0:-^70}".format(message1))
    random.seed()
    key = genRandKey()
    pText = decPlayfair(cText, key)
    newScore = score(countNGrams(pText, 4))
    bestScore = newScore
    bestKey = key
    temp = 60.0
    steps = 75000
    stepsize = temp/steps
    step = 0
    noMove = 0
    while temp > 0:
        if step % (steps / 10) == 0:
            print("Current temperature: {0: .1f}".format(temp))
        oldKey = key
        key = newKey(cText, key, temp, newScore)
        if oldKey == key:
            noMove += 1
            temp -= stepsize
            step += 1
            continue
        pText = decPlayfair(cText, key)
        newScore = score(countNGrams(pText, 4))
        if newScore > bestScore:
            print(newScore)
            bestScore = newScore
            bestKey = key
        temp -= stepsize
        step += 1
    temp = 0 # Only necessary if increment doesn't divide demp
    print('Beginning hill climbing stage')
    hillCount = 0
    while hillCount < 3000:
        key = newKey(cText, key, temp, newScore)
        pText = decPlayfair(cText, key)
        newScore = score(countNGrams(pText, 4))
        if newScore > bestScore:
            print(newScore)
            bestScore = newScore
            bestKey = key
            hillCount = 0
        hillCount += 1
    print("During regular stage, didn't move {0} times".format(noMove))
    print(bestKey)
    print(bestScore)
    return pText

test = 'THEREISNOROYALROADTOLEARNINGNOSHORTCUTTOTHEACQUIREMENTOFANYARTYOUCANNOTMAKEAMANBYSTANDINGASHEEPONITSHINDLEGSBUTBYSTANDINGAFLOCKOFSHEEPINTHATPOSITIONYOUCANMAKEACROWDOFMENITSMATTERWASNOTNEWTOMEBUTWASPRESENTEDINANEWASPECTITSHOOKMEINMYHABITTHEHABITOFNINETENTHSOFTHEWORLDOFBELIEVINGTHATALLWASRIGHTABOUTMEBECAUSEIWASUSEDTOITTISMISFORTUNETHATAWAKENSINGENUITYORFORTITUDEORENDURANCEINHEARTSWHERETHESEQUALITIESHADNEVERCOMETOLIFEBUTFORTHECIRCUMSTANCEWHICHGAVETHEMABEINGMISFORTUNESONECANENDURETHEYCOMEFROMOUTSIDETHEYAREACCIDENTSBUTTOSUFFERFORONESOWNFAULTSAHTHEREISTHESTINGOFLIFEALLAMANCANBETRAYISHISCONSCIENCE'
    
print(score(countDigramsPF(test)))
cText = matchFrequencies.getString(sys.argv[1])
pText = cText
while score(countNGrams(pText, 4)) < -3800:
    pText = saSolve(cText)
    print(pText)
    print(score(countNGrams(pText, 4)))

print(pText)
