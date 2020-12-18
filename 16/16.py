import regex
import copy
import collections
import math


def parse_field_notes(field_notes):
	result = {}
	for line in field_notes:
		match = regex.match(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", line)

		field_name = match.group(1)
		result[field_name] = [(int(match.group(2)), int(match.group(3))), (int(match.group(4)), int(match.group(5)))]

	return result

def get_invalid_values(ranges, ticket):
	values = [int(v) for v in ticket.split(",")]
	invalid_values = []
	for value in values:
		if len([1 for range in ranges if range[0] <= value <= range[1]]) == 0:
			invalid_values.append(value)

	return invalid_values

def part_1(fields, tickets):
	ranges = [item for sublist in fields.values() for item in sublist]
	validity = [get_invalid_values(ranges, ticket) for ticket in tickets]

	invalid_sum = 0
	for ticket in validity:
		invalid_sum += sum(ticket)

	print("Part 1 Answer: " + str(invalid_sum))

def reduce_candidates(potential_columns):
	final_assignments = {}

	while len(potential_columns) > 0:
		all_unassigned = [x for sublist in potential_columns.values() for x in sublist]
		single_options = [x for x in all_unassigned if all_unassigned.count(x) == 1]
		for option in single_options:
			key = [k for k, v in potential_columns.items() if option in v][0]
			final_assignments[key] = option
			del potential_columns[key]

		if len(single_options) == 0:
			print("ono")

	return final_assignments

def part_2(fields, tickets):
	ranges = [item for sublist in fields.values() for item in sublist]
	valid_tickets = [list(map(int, ticket.split(","))) for ticket in tickets if len(get_invalid_values(ranges, ticket)) == 0]

	potential_columns = {}
	for field, allowed_range in fields.items():
		candidates = []
		for i in range(len(valid_tickets[0])):
			values_from_tickets = [int(x[i]) for x in valid_tickets]
			not_allowed = [x for x in values_from_tickets if x < allowed_range[0][0] or allowed_range[0][1] < x < allowed_range[1][0] or allowed_range[1][1] < x]
			if len(not_allowed) == 0:
				candidates.append(i)

		potential_columns[field] = candidates

	assignments = reduce_candidates(potential_columns)

	my_ticket = valid_tickets[0]
	answer = 1
	for k, v in assignments.items():
		if k.startswith("departure"):
			answer *= my_ticket[v]


	print("Part 2 Answer: " + str(answer))


def main():
	with open("input.txt") as f:
		input = [x.strip() for x in f if x.strip() != ""]

	field_notes = parse_field_notes([line for line in input if regex.match(r".*: .*", line)])
	tickets = [line for line in input if regex.match(r"^[\d,]*$", line)]

	part_1(field_notes, tickets)
	part_2(field_notes, tickets)

main()
