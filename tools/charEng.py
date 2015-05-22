import collections

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
