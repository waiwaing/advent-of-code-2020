import collections
import copy
import operator
import regex

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}


def calculateExpression(expression: str):
	tokens = [x for x in expression.split(" ") if x != ""]
	value = int(tokens.pop(0))

	while len(tokens) > 0:
		op = tokens.pop(0)
		next_val = int(tokens.pop(0))

		value = ops[op](value, next_val)

	return value


def calculateExpression2(expression: str):
	tokens = [x for x in expression.split(" ") if x != ""]

	while "+" in tokens:
		pos = tokens.index("+")

		replacement_value = int(tokens[pos - 1]) + int(tokens[pos + 1])
		tokens = tokens[:pos - 1] + [str(replacement_value)] + tokens[pos + 2:]

	expression = " ".join(tokens)
	return calculateExpression(expression)


def calculateFullExpression(expression: str):
	while "(" in expression:
		match = regex.search(r"\([^\(\)]*\)", expression)
		result = calculateExpression2(match.group()[1:len(match.group()) - 1])

		expression = (expression[:match.start()] + " " + str(result) + " " + expression[match.end():]) \
			.replace("  ", " ")

	return calculateExpression2(expression)


def main():
	with open("input.txt") as f:
		input = [x.strip() for x in f if x.strip() != ""]

	results = [calculateFullExpression(line) for line in input]
	print(sum(results))


main()
