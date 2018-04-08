import sys

def troubleSort(arr):
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
    sortAttempt = troubleSort(case)
    print "Case #{}: {}".format(i, getMessage(sortAttempt))
