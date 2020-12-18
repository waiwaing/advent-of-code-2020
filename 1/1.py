def main():
	with open("input.txt") as f:
	    input = [int(line.strip()) for line in f if line.strip() != ""] 

	goals = [(2020 - x) for x in input]

	goalsSought = [findTwo(input, x) for x in goals]
	reduced = [t for t in goalsSought if t != None]

	x1 = reduced[0]
	x2 = findTwo(input, 2020 - x1)
	x3 = 2020 - x1 - x2

	result = x1 * x2 * x3

	print(result)


def findTwo(nums, target):
    list_a = nums
    list_b = [(target - x) for x in list_a]

    for x in list_b:
        if x in list_a:
            return x

    return None


main()