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

	print(grid)

	free = matrix.free_space(grid, hd.houses_e[1], 'E01', info.house_e_length, info.house_e_width)

	print("free:")
	print(free)

	print("Original value:")
	print(hd.houses_e[1].value)

	matrix.score(hd.houses_e[1], info.scale, info.house_e_value, info.house_e_free, info.house_e_increment)

	print("Newly calculated value (2+2=4-1=3)")
	print(hd.houses_e[1].value)

	total_score = 0

	for i in range(1, info.house_e_number + 1):
		print(hd.houses_e[i].id)
		matrix.free_space(grid, hd.houses_e[i], hd.houses_e[i].id, info.house_e_length, info.house_e_width)
		score = matrix.score(hd.houses_e[i], info.scale, info.house_e_value, info.house_e_free, info.house_e_increment)
		total_score = total_score + score
		print(total_score)

	for i in range(1, info.house_b_number + 1):
		print(hd.houses_b[i].id)
		matrix.free_space(grid, hd.houses_b[i], hd.houses_b[i].id, info.house_b_length, info.house_b_width)
		score = matrix.score(hd.houses_b[i], info.scale, info.house_b_value, info.house_b_free, info.house_b_increment)
		total_score = total_score + score
		print(total_score)

	for i in range(1, info.house_m_number + 1):
		print(hd.houses_m[i].id)
		matrix.free_space(grid, hd.houses_m[i], hd.houses_m[i].id, info.house_m_length, info.house_m_width)
		score = matrix.score(hd.houses_m[i], info.scale, info.house_m_value, info.house_m_free, info.house_m_increment)
		total_score = total_score + score
		print(total_score)


	print(total_score)

	# export grid to csv file
	matrix.export(grid)


if __name__ == "__main__":
	main()
