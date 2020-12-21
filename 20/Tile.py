normalise_edge = lambda edge: min(edge, "".join(reversed(edge)))


class Tile:

	def __init__(self, tile, tile_number):
		self.tile_number = tile_number
		self.set_orientation(tile)

	def set_orientation(self, tile):
		self.tile = tile

		self.top_edge = self.tile[0]
		self.bottom_edge = self.tile[9]
		self.left_edge = "".join([x[0] for x in self.tile])
		self.right_edge = "".join([x[9] for x in self.tile])

		self.edges = [self.top_edge, self.bottom_edge, self.left_edge, self.right_edge]
		self.normalised_edges = list(map(normalise_edge, self.edges))

	def borderless(self):
		return [row[1:len(row) - 1] for row in (self.tile[1:len(self.tile) - 1])]
