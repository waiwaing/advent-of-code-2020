import collections
import operator
import re

from functools import reduce
from itertools import product

direction_mapping = {"e": (1, 0), "w": (-1, 0), "ne": (0.5, 0.5), "nw": (-0.5, 0.5), "se": (0.5, -0.5),
                     "sw": (-0.5, -0.5)}


def split_directions(line):
	return re.findall("e|se|sw|w|nw|ne", line)


def calculate_destination(directions):
	return tuple(reduce(lambda acc, d: map(operator.add, acc, direction_mapping[d]), directions, (0, 0)))


def get_neighbors(c):
	return {tuple(l) for l in [map(operator.add, c, t) for t in direction_mapping.values()]}


def conway(old_state):
	new_state = []

	xs = [t[0] for t in old_state]
	ys = [t[1] for t in old_state]
	bounds = [min(xs) - 2, max(xs) + 2, min(ys) - 2, max(ys) + 2]

	new_xs = [bounds[0] + 0.5 * i for i in range(2 * int(bounds[1] - bounds[0]))]
	new_ys = [bounds[2] + 0.5 * i for i in range(2 * int(bounds[3] - bounds[2]))]
	for x, y in product(new_xs, new_ys):
		if int(x + y) != x + y:
			continue

		black_neighbors = len(get_neighbors((x, y)).intersection(old_state))

		if (x, y) in old_state:
			if black_neighbors == 1 or black_neighbors == 2:
				new_state.append((x, y))
		else:
			if black_neighbors == 2:
				new_state.append((x, y))

	return new_state


def main():
	with open("input.txt") as f:
		input = [split_directions(x.strip()) for x in f if x.strip() != ""]

	destinations = [calculate_destination(d) for d in input]

	counter = collections.Counter(sorted(destinations))
	black_tiles = [dest for dest, ct in counter.items() if ct % 2 == 1]

	print(len(black_tiles))

	for i in range(100):
		black_tiles = conway(black_tiles)

	print(len(black_tiles))


main()
