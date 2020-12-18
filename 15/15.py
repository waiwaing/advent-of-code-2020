import regex
import copy
import collections
import math

def main():
	#input = [0, 3, 6]
	input = [16, 12, 1, 0, 15, 7, 11]

	when_said = {}

	for i in range(1, 30000001):
		if len(input) > 0:
			number_to_say = input.pop(0)
			when_said[number_to_say] = i
		else:
			last_number = number_to_say
			when_last_number_said = when_said.get(last_number, -1)
			if when_last_number_said == -1:
				number_to_say = 0
			else:
				number_to_say = (i-1) - when_last_number_said

			when_said[last_number] = i-1

		if i % 300000 == 0:
			print("{0}: {1}".format(i, number_to_say))

main()
