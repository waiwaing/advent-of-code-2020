import re

def main():
	with open("input.txt") as f:
		input = [line for line in f if line.strip() != ""] 

	regex = "(\\d+)-(\\d+) (.): (.*)"

	valid = 0

	for line in input:
		match = re.match(regex, line)

		if match == None:
			print(line)

		char = match.group(3)

		index1 = int(match.group(1)) - 1
		index2 = int(match.group(2)) - 1

		match1 = match.group(4)[index1] == char
		match2 = match.group(4)[index2] == char

		if (match1 ^ match2):
			valid = valid + 1

		# num = match.group(4).count(char)
		# 	
		# if num >= int(match.group(1)) and num <= int(match.group(2)):
		# 	valid = valid + 1

	print(valid)

main()
