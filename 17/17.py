import collections
import copy


def countActiveNeighbours(initialState, x, y, z, w):
	active = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			for k in range(-1, 2):
				for l in range(-1, 2):
					if i == 0 and j == 0 and k == 0 and l == 0:
						continue

					if initialState[x + i][y + j][z + k][w + l] == "#":
						active += 1

	return active


def applyRules(initialState):
	finalState = copy.deepcopy(initialState)

	for i in range(initialState['bounds'][0] - 1, initialState['bounds'][1] + 2):
		for j in range(initialState['bounds'][2] - 1, initialState['bounds'][3] + 2):
			for k in range(initialState['bounds'][4] - 1, initialState['bounds'][5] + 2):
				for l in range(initialState['bounds'][6] - 1, initialState['bounds'][7] + 2):
					neighbors = countActiveNeighbours(initialState, i, j, k, l)
					if initialState[i][j][k][l] == '.' and neighbors == 3:
							setState(finalState, i, j, k, l, '#')
					elif initialState[i][j][k][l] == '#' and neighbors not in (2, 3):
							setState(finalState, i, j, k, l, '.')

	return finalState


def countActive(state):
	active = 0
	for i in range(state['bounds'][0], state['bounds'][1] + 1):
		for j in range(state['bounds'][2], state['bounds'][3] + 1):
			for k in range(state['bounds'][4], state['bounds'][5] + 1):
				for w in range(state['bounds'][6], state['bounds'][7] + 1):
					if state[i][j][k][w] == '#':
						active += 1

	return active


def printState(state):
	print(state['bounds'])
	for w in range(state['bounds'][6], state['bounds'][7] + 1):
		for k in range(state['bounds'][4], state['bounds'][5] + 1):
			print("z=" + str(k) + ", w=" + str(w))
			for i in range(state['bounds'][0], state['bounds'][1] + 1):
				print("".join([state[i][j][k][w] for j in range(state['bounds'][2], state['bounds'][3] + 1)]))

			print("")

	print("--------------------------------------------")


def setState(state, x, y, z, w, value):
	state[x][y][z][w] = value
	state['bounds'] = [
		min(state['bounds'][0], x), max(state['bounds'][1], x), min(state['bounds'][2], y), max(state['bounds'][3], y),
		min(state['bounds'][4], z), max(state['bounds'][5], z), min(state['bounds'][6], w), max(state['bounds'][7], w),
	]


def main():
	with open("testinput.txt") as f:
		input = [list(x.strip()) for x in f if x.strip() != ""]

	state = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda:collections.defaultdict(lambda: '.'))))
	state['bounds'] = [0, 0, 0, 0, 0, 0, 0, 0]

	for i in range(len(input)):
		for j in range(len(input[0])):
			setState(state, i, j, 0, 0, input[i][j])

	for i in range(6):
		state = applyRules(state)
	#	printState(state)

	print(countActive(state))

main()
