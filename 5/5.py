import re

def transformSeatToId(seat):
	row_info = seat[:7]
	col_info = seat[7:]

	row_as_bin = row_info.replace('F', '0').replace('B', '1')
	col_as_bin = col_info.replace('L', '0').replace('R', '1')

	row = int(row_as_bin, 2)
	col = int(col_as_bin, 2)

	seatId = row * 8 + col

	return seatId

def main():
	with open('input.txt') as f:
		input = [line.strip() for line in f if line.strip() != '']

	seatIds = [transformSeatToId(seat) for seat in input]
	largest_seat = max(seatIds)

	candidate_seats = [x for x in range(0, largest_seat + 1) if x not in seatIds]

	for i in candidate_seats:
		if ((i-1) not in candidate_seats) and ((i+1) not in candidate_seats):
			print(i)

main()
