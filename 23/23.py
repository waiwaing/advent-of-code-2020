import collections

from itertools import chain


def part1(input):
	x = input.popleft()
	removed = [input.popleft(), input.popleft(), input.popleft()]
	input.appendleft(x)
	return x, removed


def part2(input, current_cup_value, removed):
	destination_label = current_cup_value - 1
	while destination_label in removed or destination_label == 0:
		destination_label -= 1
		if destination_label < 1:
			destination_label = max(input)

	return destination_label


def part3(input, cache, destination_label, t):
	# return input.index(destination_label)

	cc = cache[destination_label]
	for i in chain(range((cc - 1000) % t, t), range(0, (cc - 1000) % t)):
		if input[i % t] == destination_label:
			return i % t


def part4(input, destination_index, t, removed):
	r = t - destination_index - 1
	input.rotate(r)
	input.extend(removed)
	input.rotate(-r - 1)


def part5(cache, removed, destination_index):
	cache[removed[2]] = destination_index + 3
	cache[removed[1]] = destination_index + 2
	cache[removed[0]] = destination_index + 1


def execute_move(input, cache, t):
	current_cup_value, removed = part1(input)
	destination_label = part2(input, current_cup_value, removed)
	destination_index = part3(input, cache, destination_label, t)
	part4(input, destination_index, t, removed)
	part5(cache, removed, destination_index)


def main(xsd):
	orig_input = list(map(int, list(xsd)))  # 974618352

	input = collections.deque(orig_input[:])
	cache = collections.defaultdict(lambda: 0)

	for i in range(100):
		execute_move(input, cache, 9 - 3)

	print("".join([str(x) for x in input] + [str(x) for x in input]))

	cache = collections.defaultdict(lambda: 0)
	input = collections.deque(orig_input + list(range(10, 1000001)))
	for i in range(10000000):
		if i % 1000 == 0:
			recache(input, cache)
			# print(i)
		execute_move(input, cache, 1000000 - 3)

	key = input.index(1)
	print(input[key + 1] * input[key + 2])


def recache(input, cache):
	for index, val in enumerate(input):
		cache[val] = index


main("389125467")
main("974618352")
