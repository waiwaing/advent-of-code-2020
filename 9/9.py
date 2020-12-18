import regex
import copy
import collections

def findNonSum(bufferLength, input):
    queue = collections.deque([], bufferLength)

    while len(queue) < bufferLength:
        queue.append(input.pop(0))
 
    for x in input:
        difference = [x-m for m in queue if (x-m) in queue]
        if len(difference) == 0:
            return x

        queue.popleft()
        queue.append(x)

def findConsecutiveSum(target, input):
    buffer = []
    for i in input:
        buffer.append(i)

        if sum(buffer) < target:
            continue

        for j in range(0, len(buffer)):
            rangeOfInterest = buffer[j:]
            if sum(rangeOfInterest) == target:
                low = min(rangeOfInterest)
                hig = max(rangeOfInterest)

                return low, hig

        buffer.pop(0)


def main():
    input = []
    with open("input.txt") as f:
        input = [int(x.strip()) for x in f if x.strip() != ""]

    magicNumber = findNonSum(25, list(input)) # 26134589
    print(magicNumber)

    small, large = findConsecutiveSum(magicNumber, list(input))
    print(small + large)
      

main()
