import re


def main():
    input = []
    buffer = []
    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip()

            if line == "":
                input.append(buffer)
                buffer = []
            else:
                buffer.append(line)
    input.append(buffer)

    input = [x for x in input if x != []]

    common = 0
    for group in input:
        intersection = set(group[0]).intersection(*group)
        common = common + len(intersection)

    print(common)


main()
