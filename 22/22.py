import collections
import copy
import math
import regex

from functools import reduce
from itertools import product


class PlayerAWin(Exception):
	pass


def rc_play_round(deck_a, deck_b, history):
	for (deck_ah, deck_bh) in history:
		if deck_a == deck_ah and deck_b == deck_bh:
			raise PlayerAWin

	history.append((deck_a[:], deck_b[:]))
	card_a = deck_a.pop(0)
	card_b = deck_b.pop(0)

	if card_a <= len(deck_a) and card_b <= len(deck_b):
		(nda, ndb, winner) = rc_play_game(deck_a[:card_a], deck_b[:card_b])
	else:
		winner = "a" if card_a > card_b else "b"

	if winner == "a":
		deck_a += [card_a, card_b]
	else:
		deck_b += [card_b, card_a]


def rc_play_game(deck_a, deck_b):
	history = []
	try:
		while len(deck_a) > 0 and len(deck_b) > 0:
			rc_play_round(deck_a, deck_b, history)

		return deck_a, deck_b, "a" if len(deck_a) > 0 else "b"
	except PlayerAWin:
		return deck_a, deck_b, "a"


def play_combat(deck_a, deck_b):
	while len(deck_a) > 0 and len(deck_b) > 0:
		card_a = deck_a.pop(0)
		card_b = deck_b.pop(0)

		list_to_append = sorted([card_a, card_b], reverse=True)
		list_to_append_to = deck_a if card_a > card_b else deck_b

		list_to_append_to += list_to_append

	return deck_a, deck_b


def print_winner(deck_a, deck_b, winner):
	print(winner)
	winner = deck_a if winner == "a" else deck_b
	points = 0
	for i, card in enumerate(winner):
		value = len(winner) - i
		points += value * card
	return points


def main():
	with open("input.txt") as f:
		input = [x.strip() for x in f if x.strip() != ""]
	mid = input.index("Player 2:")

	player_a = [int(x) for x in input[1:mid]]
	player_b = [int(x) for x in input[mid + 1:]]

	a, b = play_combat(player_a[:], player_b[:])
	winner = "a" if len(a) > 0 else "b"
	print(print_winner(a, b, winner))

	a, b, w = rc_play_game(player_a[:], player_b[:])
	print(print_winner(a, b, w))


main()
