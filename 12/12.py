import regex
import copy
import collections
import math 

# (x, y, facing)

def applyInstruction(initialState, action, value):
    if action == "N":
        return (initialState[0], initialState[1] + value, initialState[2])
    elif action == "S":
        return (initialState[0], initialState[1] - value, initialState[2])
    elif action == "E": 
        return (initialState[0] + value, initialState[1], initialState[2])
    elif action == "W":
        return (initialState[0] - value, initialState[1], initialState[2])
    elif action == "L":
        return (initialState[0], initialState[1], initialState[2] + value)
    elif action == "R":
        return (initialState[0], initialState[1], initialState[2] - value)
    elif action == "F":
        angle = initialState[2] % 360
        y = int(value * math.sin(math.radians(angle)))
        x = int(value * math.cos(math.radians(angle)))
        return (initialState[0] + x, initialState[1] + y, initialState[2])
    else:
        raise RuntimeError()

# (x, y, facing, waypointDX, waypointDY)

def applyInstruction2(initialState, action, value):
    if action == "N":
        return (initialState[0], initialState[1], initialState[2], initialState[3], initialState[4] + value)
    elif action == "S":
        return (initialState[0], initialState[1], initialState[2], initialState[3], initialState[4] - value)
    elif action == "E": 
        return (initialState[0], initialState[1], initialState[2], initialState[3] + value, initialState[4])
    elif action == "W":
        return (initialState[0], initialState[1], initialState[2], initialState[3] - value, initialState[4])
    elif action == "L":
        x = int(round(initialState[3] * math.cos(math.radians(value)) - initialState[4] * math.sin(math.radians(value))))
        y = int(round(initialState[4] * math.cos(math.radians(value)) + initialState[3] * math.sin(math.radians(value))))
        return (initialState[0], initialState[1], initialState[2], x, y)
    elif action == "F":
        x = value * initialState[3]
        y = value * initialState[4]

        return (initialState[0] + x, initialState[1] + y, initialState[2], initialState[3], initialState[4])
    else:
        raise RuntimeError()

def main():
    input = []
    with open("input.txt") as f:
        input = [x.strip() for x in f if x.strip() != ""]

    state = (0, 0, 0, 10, 1)
    for line in input:
        #print(line)
        action = line[0]
        value = int(line[1:])
        if action == "R":
            action = "L"
            value = 0 - value

        state = applyInstruction2(state, action, value)
        print(state)

    print(abs(state[0]) + abs(state[1]))


main()
