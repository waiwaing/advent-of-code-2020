import regex
import copy
import collections
import math 

def part_1(t, buses):
    mods = [(bus, t % bus) for bus in buses]

    high_mod = mods[0]
    for bus in mods:
        if bus[1] > high_mod[1]:
            high_mod = bus

    bus_number = high_mod[0]
    waiting_time = bus_number - high_mod[1]

    print(bus_number * waiting_time)

def part_2(input):
    # Wolfram Alpha:

    #  (n +  0) mod  23 == 0, (n + 17) mod  37 == 0,(n + 23) mod 431 == 0,(n + 36) mod  13 == 0,(n + 37) mod  17 == 0,(n + 42) mod  19 == 0,(n + 54) mod 409 == 0,(n + 64) mod  41 == 0,(n + 83) mod  29 == 0

    # n = 748958695773119 m + 402251700208309, m in Z
    print(402251700208309)

def main():
    input = []
    with open("input.txt") as f:
        input = [x.strip() for x in f if x.strip() != ""]

    t = int(input[0])
    buses = [int(bus) for bus in input[1].split(',') if bus.isnumeric()]

    part_1(t, buses)
    part_2(input[1])

   


main()
