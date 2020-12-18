import re

def main(dx, dy):
	with open("input.txt") as f:
		input = [line.strip() for line in f if line.strip() != ""] 

	rows = len(input)
	x = 0
	y = 0
	trees = 0

	while y + dy < rows:
		x = x + dx
		y = y + dy

		row = input[y]
		row_length = len(row)
		x_mod = x % row_length

		value = row[x_mod]
		if value == '#':
			trees = trees + 1

	return(trees)

a = main(1, 1)
b = main(3, 1)
c = main(5, 1)
d = main(7, 1)
e = main(1, 2)

f = a*b*c*d*e
print(f)
