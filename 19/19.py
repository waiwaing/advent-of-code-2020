import collections
import copy
import operator
import regex


def parse_rules(rule_strings):
	matches = [regex.match(r"(\d*): (.*)", x) for x in rule_strings]
	rules = {int(match.group(1)): [x.replace('"', "").strip().split() for x in match.group(2).split("|")]
	         for match in matches}

	changes = True
	while changes:
		changes = False

		for rule_number, options in rules.items():
			new_rules = []
			for option in options:
				for pos, elem in enumerate(option):
					if elem.isnumeric():
						r = int(int(elem))
						new_rules += [option[:pos] + t + option[pos + 1:] for t in rules[r]]
						changes = True
						break
				else:
					new_rules += [option]
				pass

			rules[rule_number] = new_rules

	for rule_number, options in rules.items():
		rules[rule_number] = ["".join(option) for option in options]

	return rules


def main():
	with open("input.txt") as f:
		input = [x.strip() for x in f if x.strip() != ""]

	rules = parse_rules([x for x in input if ":" in x])
	messages = [x for x in input if ":" not in x]

	print(sum([1 for message in messages if message in rules[0]]))

	matches = 0

	for message in messages:
		n = 8
		message_by_bytes = [message[i:i + n] for i in range(0, len(message), n)]
		for k in range(len(message_by_bytes)):
			first_half = message_by_bytes[:k]
			second_half = message_by_bytes[k:]
			second_half_a = second_half[:len(second_half) // 2]
			second_half_b = second_half[len(second_half) // 2:]

			a = all([x in rules[8] for x in first_half])
			b = all([x in rules[42] for x in second_half_a])
			c = all([x in rules[31] for x in second_half_b])

			if min(len(first_half), len(second_half_a), len(second_half_b)) == 0:
				continue

			if len(second_half_b) != len(second_half_a):
				continue

			if "".join(first_half) + "".join(second_half_a) + "".join(second_half_b) != message:
				raise RuntimeError

			if a and b and c:
				matches += 1
				break

	print(matches)


main()
