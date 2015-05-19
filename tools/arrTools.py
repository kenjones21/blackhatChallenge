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

def numMatches(arr1, arr2):
    ans = 0
    for el1 in arr1:
        for el2 in arr2:
            if el1 == el2:
                ans += 1
    return ans

def modArray(arr, mod):
    newArr = []
    for i in range(0, len(arr)):
        newArr.append(arr[i] % mod)
    return newArr
