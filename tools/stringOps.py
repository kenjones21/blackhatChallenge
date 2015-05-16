alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftString(string, shift):
    A = ord('A')
    ans = ''
    for c in string:
        ans += chr((ord(c) - A + shift) % 26 + A)
    return ans

def everyNth(string, start, n):
    ans = ''
    for i in range(start, len(string)):
        if (i - start) % n == 0:
            ans += string[i]
    return ans

def splitString(string, n):
    ans = []
    for i in range(0,n):
        start = i;
        ans.append(everyNth(string, start, n))
    return ans
