def remove_three(mapping, current_cup):
	# noinspection PyListCreation
	x = mapping[current_cup]
	y = mapping[x]
	z = mapping[y]

	mapping[current_cup] = mapping[z]
	return [x, y, z]


def calculate_destination_cup(mapping, current_cup, removed):
	destination = current_cup - 1
	while destination in removed or destination == 0:
		destination -= 1
		if destination < 1:
			destination = len(mapping) - 1

	return destination


def insert(mapping, destination_cup, removed):
	mapping[removed[2]] = mapping[destination_cup]
	mapping[destination_cup] = removed[0]


def execute_move(mapping, current_cup):
	removed = remove_three(mapping, current_cup)
	destination_cup = calculate_destination_cup(mapping, current_cup, removed)
	insert(mapping, destination_cup, removed)
	return mapping[current_cup]


def pairwise(iterable):
	it = iter(iterable)
	a = next(it, None)

	for b in it:
		yield a, b
		a = b

	yield a, iterable[0]


def print_mapping(mapping):
	i = 1
	res = ""
	while mapping[i] != 1:
		res += str(mapping[i])
		i = mapping[i]

	print(res)


def print_part_2_computation(mapping):
	a = mapping[1]
	b = mapping[a]

	print(a * b)


def main(input_s):
	input = list(map(int, list(input_s)))  # 974618352

	# Part 1
	mapping = [-1] * 10
	for cur, nxt in pairwise(input):
		mapping[cur] = nxt
	current_cup = input[0]

	for i in range(100):
		current_cup = execute_move(mapping, current_cup)

	print_mapping(mapping)

	# Part 2
	mapping = [-1] * 1_000_001
	for cur, nxt in pairwise(input + list(range(10, 1_000_001))):
		mapping[cur] = nxt
	current_cup = input[0]

	for i in range(10_000_000):
		current_cup = execute_move(mapping, current_cup)

	print_part_2_computation(mapping)


main("389125467")
main("974618352")
