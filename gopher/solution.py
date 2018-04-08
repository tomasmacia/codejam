from collections import Counter
import sys
import numpy as np


def getCellCoordinates(orchard, lastCoordX, lastCoordY):
    if isShaped(orchard) and diggedAroundCoordinates(orchard, lastCoordX, lastCoordY):
        lastCoordX += 3
    return [lastCoordX,lastCoordY]

def isShaped(orchard):
    rows, columns = np.where(orchard == 1)
    counterRows = Counter(rows)
    counterColumns = Counter(columns)
    return len(set(counterRows.values())) == len(set(counterColumns.values())) == 1

def diggedAroundCoordinates(orchard, x, y):
    return orchard[x-2,y-2] == orchard[x-2,y-1] == orchard[x-2,y] == orchard[x-1,y-2] == orchard[x-1,y-1] == orchard[x-1,y] == orchard[x,y-2] == orchard[x,y-1] == orchard[x,y] == 1

def updateOrchard(orchard, coordX, coordY):
    orchard[coordX-1, coordY-1] = 1

def exitCoordinates(x, y):
    return (x == 0 and y == 0) or (x == -1 and y == -1)

ORCHARD_X = ORCHARD_Y = 200
initialCoordX = initialCoordY = 3
testcases = int(raw_input())
caseNumber = 1

while caseNumber <= testcases:
    orchard = np.zeros((ORCHARD_X, ORCHARD_Y), dtype=int)
    lastCoordX = initialCoordX
    lastCoordY = initialCoordY
    done = False
    area = int(raw_input())
    while not done:
        desiredX, desiredY = getCellCoordinates(orchard, lastCoordX, lastCoordY)
        lastCoordX, lastCoordY = desiredX, desiredY
        print "{} {}".format(desiredX, desiredY)
        sys.stdout.flush()
        x, y = [int(coordinate) for coordinate in raw_input().split(" ")]
        if not exitCoordinates(x,y):
            updateOrchard(orchard, x, y)
        else:
            done = True
    caseNumber += 1
