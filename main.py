#!/usr/bin/env python3

from class_objects import House, Water, Matrix
import alg_random as random
import setup as info
import house_dictionary as hd

def main():

	matrix = Matrix(info.grid_length,info.grid_width)
	grid = matrix.grid



	# print grid
	print("start:")
	random.fill(grid, matrix)
	print(grid)

	# Water
	matrix.place(info.water_length, info.water_width, 0, 0, "~")

	print(grid)

	free = matrix.free_space(grid, hd.houses_e[1], 'E01', info.house_e_length, info.house_e_width)

	print(free)
	# export grid to csv file
	matrix.export(grid)


if __name__ == "__main__":
	main()
