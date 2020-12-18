import regex
import copy
import collections

def countNeighbors(initialState, x, y):
    length = len(initialState[0])
    height = len(initialState)

    occupied = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            
            x2 = x + i
            y2 = y + j
            
            if (x2 < 0) or (x2 >= length) or (y2 < 0) or (y2 >= height):
                continue

            if initialState[y2][x2] == "#":
                occupied += 1

    return occupied

def countVisible(initialState, x, y):
    length = len(initialState[0])
    height = len(initialState)

    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    occupied = 0
    for delta in deltas:
        x2, y2 = (x + delta[0], y + delta[1])
        while (x2 >= 0) and (x2 < length) and (y2 >= 0) and (y2 < height):
            if initialState[y2][x2] == '#':
                occupied += 1
                break
            elif initialState[y2][x2] == 'L':
                break
            x2, y2 = (x2 + delta[0], y2 + delta[1])

    return occupied



def applyRules(initialState):
    length = len(initialState[0])
    height = len(initialState)

    finalState = copy.deepcopy(initialState)

    for i in range(length):
        for j in range(height):
            neighbors = countVisible(initialState, i, j)
            if initialState[j][i] == 'L' and neighbors == 0:
                finalState[j][i] = '#'
            elif initialState[j][i] == '#' and neighbors >= 5:
                finalState[j][i] = 'L'
            else:
                finalState[j][i] = initialState[j][i]

    return finalState

def hasChanged(old, new):
    length = len(old[0])
    height = len(old)

    for i in range(length):
        for j in range(height):
            if old[j][i] != new[j][i]:
                return True

    return False

def countOccupied(input):
    occupied = 0
    for i in input:
        occupied += len([x for x in i if x == '#'])
    return occupied

def printState(state):
    for row in state:
        outputLine = ""
        for col in row:
            outputLine += col
        print(outputLine) 

    print("--------------------------------------------")



def main():
    input = []
    with open("input.txt") as f:
        input = [x.strip() for x in f if x.strip() != ""]

    for i in range(len(input)):
        input[i] = list(input[i])

    old = input

    while True:
        new = applyRules(old)
       # printState(new)
        if not hasChanged(old, new):
            break
        old = new

    print(countOccupied(new))


main()
