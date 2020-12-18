import regex
import copy
import collections

def calculateDifferences(input):
    input.sort()
    differences = [input[n]-input[n-1] for n in range(1,len(input))]

    ones = len([x for x in differences if x == 1])
    tres = len([x for x in differences if x == 3])

    return ones, tres

def partTwo(input):
    q = [(max(input), 1)]
    counter = 0

    while len(q) > 0:
        nextQ = []
        for (item, value) in q:
            if item == 0:
                counter += value
            else:
                t = [item-1, item-2, item-3]
                t = [(x, value) for x in t if x in input]
                nextQ.extend(t)

        uniqueKeys = set([x[0] for x in nextQ])
        newQ = []
        for key in uniqueKeys:
            total = sum([t[1] for t in nextQ if t[0] == key])
            newQ.append([key, total])

        q = newQ

    return counter


def main():
    input = []
    with open("input.txt") as f:
        input = [int(x.strip()) for x in f if x.strip() != ""]

    deviceJoltage = max(input) + 3
    input.insert(0, 0)
    input.append(deviceJoltage)

    ones, tres = calculateDifferences(input)
    print(ones*tres)

    p2 = partTwo(input)
    print(p2)
      

main()
