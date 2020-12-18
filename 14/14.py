import regex
import copy
import collections
import math


def parseMask(line):
	mask = line[7:]

	ones_mask = ''.join([('1' if char == '1' else '0') for char in mask])
	zero_mask = ''.join([('0' if char == '0' else '1') for char in mask])

	return int(ones_mask, 2), int(zero_mask, 2)


def getAddressesToWrite(line, initialMemoryAddress):
	mask = line[7:]

	ones_mask = ''.join([('1' if char != '0' else '0') for char in mask])
	address = initialMemoryAddress | int(ones_mask, 2)

	initial_mask = '1' * len(mask)
	indices = [i for i, ltr in enumerate(mask) if ltr == 'X']
	for i in indices:
		initial_mask = initial_mask[:i] + "0" + initial_mask[i + 1:]
	initial_mask = int(initial_mask, 2)

	results = []

	for i in range(2 ** len(indices)):
		new_bitmask = copy.copy(initial_mask)
		for pos, j in enumerate(indices):
			if ((1 << pos) & i) > 0:
				new_bitmask = new_bitmask | (1 << (len(mask) - j - 1))

		results.append(new_bitmask & address)

	return results


def main():
	input = []
	with open("input.txt") as f:
		input = [x.strip() for x in f if x.strip() != ""]

	registers = {}

	for line in input:
		if line.startswith("mask ="):
			ones_mask, zero_mask = parseMask(line)
			last_mask = line
		else:
			matches = regex.match(r"mem\[(\d+)] = (.*)", line)
			lineNumber = matches.group(1)
			value = int(matches.group(2))

#			registers[lineNumber] = (value | ones_mask) & zero_mask

			addresses = getAddressesToWrite(last_mask, int(lineNumber))
			for address in addresses:
				registers[address] = value

	sum = 0
	for v in registers.values():
		sum += v

	print(sum)


main()
