import regex
import copy

def parseInstruction(line):
    matches = regex.match(r"(\D{3}) ([+-]\d+)", line)
    return matches.group(1), int(matches.group(2))

def runInstructions(input):
    acc = 0
    visitedInstructions = set()
    currentInstruction = 0

    while True:
        visitedInstructions.add(currentInstruction)
        op, arg = input[currentInstruction]

        if op == "nop":
            currentInstruction += 1
        elif op == "acc":
            currentInstruction += 1
            acc += arg
        elif op == "jmp":
            currentInstruction += arg

        if currentInstruction in visitedInstructions:
            return -1, acc

        if currentInstruction >= len(input):
            return 0, acc


def main():
    input = []
    with open("input.txt") as f:
        input = [x.strip() for x in f if x.strip() != ""]

    instructions = [parseInstruction(x) for x in input]
    print(runInstructions(instructions))

    for i in range(0, len(instructions)):
        alternate_instructions = copy.copy(instructions)
        if alternate_instructions[i][0] == "nop":
            alternate_instructions[i] = ("jmp", alternate_instructions[i][1])
        elif alternate_instructions[i][0] == "jmp":
            alternate_instructions[i] = ("nop", alternate_instructions[i][1])
        else:
            continue

        output = runInstructions(alternate_instructions)
        if output[0] == 0:
            print(output)
            break


main()
