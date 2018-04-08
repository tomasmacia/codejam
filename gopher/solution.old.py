from collections import Counter
import sys
import numpy as np

ORCHARD_X = ORCHARD_Y = 1000
initialCoordX = initialCoordY = 2
logs = open('./log.txt', 'w')

def getCellCoordinates(orchard, lastCoordX, lastCoordY, desiredArea):
    #coordX = coordY = 2
    if isShaped(orchard) and diggedAroundCoordinates(orchard, lastCoordX, lastCoordY):
        lastCoordX += 3
    return [lastCoordX,lastCoordY]

def isShaped(orchard):
    rows, columns = np.where(orchard == 1)
    counterRows = Counter(rows)
    counterColumns = Counter(columns)
    print >>logs, "Rows: {}".format(list(counterRows))
    print >>logs, "Columns: {}".format(list(counterColumns))
    return len(set(counterRows.values())) == len(set(counterColumns.values())) == 1

def getShapeArea(orchard):
    # to be called when is shaped
    rows, columns = np.where(orchard == 1)
    listRows = list(Counter(rows))
    listColumns = list(Counter(columns))
    if sorted(listRows) == range(min(listRows), max(listRows)+1):
        rowsNumber = len(listRows)
    else:
        rowsNumber = 0
    if sorted(listColumns) == range(min(listColumns), max(listColumns)+1):
        columnsNumber = len(listColumns)
    else:
        columnsNumber = 0
    print >>logs, rowsNumber*columnsNumber
    return rowsNumber * columnsNumber

def diggedAroundCoordinates(orchard, x, y):
    return orchard[x-2,y-2] == orchard[x-2,y-1] == orchard[x-2,y] == orchard[x-1,y-2] == orchard[x-1,y-1] == orchard[x-1,y] == orchard[x,y-2] == orchard[x,y-1] == orchard[x,y] == 1

def updateOrchard(orchard, coordX, coordY):
    orchard[coordX-1, coordY-1] = 1

def exitCoordinates(x, y):
    return (x == 0 and y == 0) or (x == -1 and y == -1)

testcases = int(sys.stdin.readline().strip())
caseNumber = 0
orchard = np.zeros((ORCHARD_X, ORCHARD_Y))

while caseNumber < testcases:
    caseNumber += 1
    orchard = np.zeros((ORCHARD_X, ORCHARD_Y), dtype=int)
    lastCoordX = initialCoordX
    lastCoordY = initialCoordY
    done = False
    deploy = 1
    area = int(sys.stdin.readline().strip())
    while not done:
        desiredX, desiredY = getCellCoordinates(orchard, lastCoordX, lastCoordY, area)
        lastCoordX, lastCoordY = desiredX, desiredY
        print "{} {}".format(desiredX, desiredY)
        sys.stdout.flush()
        x, y = [int(coordinate) for coordinate in sys.stdin.readline().strip().split(" ")]
        if not exitCoordinates(x,y):
            updateOrchard(orchard, x, y)
        else:
            done = True
        print >>logs, "Intento nro {}".format(deploy)
        deploy += 1
