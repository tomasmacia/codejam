import sys
from datetime import datetime
startTime = datetime.now()

def swap(s, i, j):
    lst = list(s);
    lst[i], lst[j] = lst[j], lst[i]
    return [int(num) for num in lst]

# def troubleSort(arr):
#     done = False
#     while not done:
#       done = True
#       for i in xrange(0, len(arr)-2):
#         if arr[i] > arr[i+2]:
#           done = False
#           arr = swap(arr, i, i+2)
#     return arr

def bubbleSort(arr):
    n = len(arr)
    for i in xrange(0, n):
        for j in xrange(0, n-2):
            if arr[j] > arr[j+2] :
                arr[j], arr[j+2] = arr[j+2], arr[j]
    return arr

def firstSortingIndexError(arr):
    for i in xrange(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return i
    return -1

def getMessage(arr):
    idx = firstSortingIndexError(arr)
    return idx if idx > -1 else "OK"

inputCases = sys.stdin
cases = [[int(num) for num in line.strip().split(' ')] for line in inputCases][2::2]
i = 0

for case in cases:
    i += 1
    print case
    #sortAttempt = troubleSort(case)
    sortAttempt = bubbleSort(case)
    print sortAttempt
    print "Case #{}: {}".format(i, getMessage(sortAttempt))

print datetime.now() - startTime
