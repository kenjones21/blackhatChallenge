import datetime, urllib2
from bs4 import BeautifulSoup
import re
import collections

url = "http://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/digraphs.html"

def get_freqs():
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read())
    soup.prettify()
    something = soup.find_all("font", {"face": "Arial"})
    numPat = re.compile('\d\.\d\d')
    textPat = re.compile('>([a-z][a-z])<')
    nums = []
    texts = []
    ans = collections.defaultdict(str)
    for thing in something:
        n = numPat.search(str(thing))
        t = textPat.search(str(thing))
        if n:
            nums.append(n.group(0))
        if t and t.group(1) not in texts:
            texts.append(t.group(1))
    if len(nums) != len(texts):
        print('NOOOOOOOOO')
    else:
        for i in range(0, len(nums)):
            ans[texts[i]] = float(nums[i])
    return ans
        
    
get_freqs()
