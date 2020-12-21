import collections
import copy
import math
import regex

from functools import reduce
from itertools import product


def main():
	input = []

	with open("input.txt") as f:
		for line in f:
			if line.strip() == "":
				continue

			match = regex.match(r"((\w+)\W*)* \(contains ((\w+)\W*)*\)", line)
			input.append((match.captures(2), match.captures(4)))

	all_ingredients = [x for sublist in input for x in sublist[0]]
	allergen_map = {x: [] for x in set(all_ingredients)}
	allergens = {x for sublist in input for x in sublist[1]}

	for allergen in allergens:
		ingredients = [set(x[0]) for x in input if allergen in x[1]]
		common_ingredients = ingredients.pop().intersection(*ingredients)
		for i in common_ingredients:
			allergen_map[i].append(allergen)

	safe_ingredients = [a for a, v in allergen_map.items() if len(v) == 0]
	print(sum([all_ingredients.count(x) for x in safe_ingredients]))

	reduced_allergen_map = {ing: allergens for ing, allergens in allergen_map.items() if len(allergens) > 0}
	definitive_allergen_map = {ing: None for ing in reduced_allergen_map.keys()}

	while None in definitive_allergen_map.values():
		to_reduce = {ing: allergens for ing, allergens in reduced_allergen_map.items() if len(allergens) == 1}
		for ing, allergens in to_reduce.items():
			definitive_allergen_map[ing] = allergens[0]
			del reduced_allergen_map[ing]

			for r_ing, r_allergens in reduced_allergen_map.items():
				if allergens[0] in r_allergens:
					r_allergens.remove(allergens[0])

	ia_pairs = [(k, v) for k, v in definitive_allergen_map.items()]
	print(",".join([y[0] for y in sorted(ia_pairs, key=lambda x: x[1])]))


main()
