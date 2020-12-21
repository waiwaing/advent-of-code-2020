import collections
import copy
import math
import regex

from functools import reduce
from itertools import product

from Tile import Tile

normalise = lambda edge: min(edge, "".join(reversed(edge)))
get_unique_edges_for_tile = lambda tile, all_edges: [e for e in tile.edges if all_edges.count(normalise(e)) == 1]
get_tiles_with_edge = lambda candidates, edge: [t for t in candidates if normalise(edge) in t.normalised_edges]


def get_corner_tiles(tiles, all_edges):
	unique_edges = [e for e in all_edges if all_edges.count(e) == 1]
	edge_tiles = [tile for tile in tiles for edge in unique_edges if edge in tile.normalised_edges]

	return list({t for t in edge_tiles if edge_tiles.count(t) == 2})


def get_all_orientations(t):
	r = lambda tile: ["".join(list(x)) for x in zip(*tile[::-1])]
	f = lambda tile: [row[::-1] for row in tile]
	return [t, r(t), r(r(t)), r(r(r(t))), f(t), r(f(t)), r(r((f(t)))), r(r(r(f(t))))]


def orient_tile(tile, top_edge_candidates, left_edge_candidates):
	for left, top, p in product(left_edge_candidates, top_edge_candidates, get_all_orientations(tile.tile)):
		if normalise(p[0]) == normalise(top) and normalise("".join(y[0] for y in p)) == normalise(left):
			tile.set_orientation(p)
			return tile


def build_grid(tiles, corner_tiles, all_edges, dim_size):
	grid = [[[] for _ in range(dim_size)] for _ in range(dim_size)]

	for i, j in product(range(dim_size), range(dim_size)):
		if i == 0 and j == 0:
			tile = corner_tiles[0]
			unique_edges = get_unique_edges_for_tile(tile, all_edges)
			left_edges = [unique_edges[0]]
			top_edges = [unique_edges[1]]
		elif i == 0:
			left_edges = [grid[i][j - 1].right_edge]
			tile = get_tiles_with_edge(tiles, left_edges[0]).pop()
			top_edges = get_unique_edges_for_tile(tile, all_edges)
		elif j == 0:
			top_edges = [grid[i - 1][j].bottom_edge]
			tile = get_tiles_with_edge(tiles, top_edges[0]).pop()
			left_edges = get_unique_edges_for_tile(tile, all_edges)
		else:
			top_edges = [grid[i - 1][j].bottom_edge]
			left_edges = [grid[i][j - 1].right_edge]
			tile = get_tiles_with_edge(get_tiles_with_edge(tiles, top_edges[0]), left_edges[0]).pop()

		grid[i][j] = orient_tile(tile, top_edges, left_edges)
		tiles.remove(grid[i][j])

	return grid


def denormalise_grid(grid, dim_size):
	denormalised_grid = [[[] for _ in range(dim_size * 8)] for _ in range(dim_size * 8)]

	for i, j, x, y in product(range(dim_size), range(dim_size), range(8), range(8)):
		denormalised_grid[i * 8 + x][j * 8 + y] = grid[i][j].borderless()[x][y]

	return denormalised_grid


def count_monsters(grid):
	grid = [[0 if x == "." else 1 for x in row] for row in grid]
	monster = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
	           [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
	           [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]

	monsters = 0
	for x, y in product(range(0, len(grid) - 3), range(0, len(grid) - len(monster[0]))):
		m0 = [monster[0][i] & grid[x + 0][y + i] for i in range(len(monster[0]))]
		m1 = [monster[1][i] & grid[x + 1][y + i] for i in range(len(monster[0]))]
		m2 = [monster[2][i] & grid[x + 2][y + i] for i in range(len(monster[0]))]

		if m0 == monster[0] and m1 == monster[1] and m2 == monster[2]:
			monsters += 1

	return monsters


def part2(tiles, corner_tiles, all_edges):
	dim_size = int(math.sqrt(len(tiles)))
	grid = build_grid(tiles, corner_tiles, all_edges, dim_size)
	reduced_grid = ["".join(row) for row in denormalise_grid(grid, dim_size)]

	sea_monsters = max(map(count_monsters, get_all_orientations(reduced_grid)))
	return sum([row.count("#") for row in reduced_grid]) - 15 * sea_monsters


def main():
	with open("input.txt") as f:
		input = [x.strip() for x in f if x.strip() != ""]

	tiles = [Tile(input[i + 1:i + 11], int(regex.search(r"\d+", input[i]).group())) for i in range(0, len(input), 11)]
	all_edges = [x for tile in tiles for x in tile.normalised_edges]
	corner_tiles = get_corner_tiles(tiles, all_edges)

	print("Part 1: {0}".format(reduce(lambda acc, tile: acc * tile.tile_number, corner_tiles, 1)))
	print("Part 2: {0}".format(part2(tiles, corner_tiles, all_edges)))


main()
