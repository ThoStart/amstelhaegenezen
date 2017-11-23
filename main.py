#!/usr/bin/env python3

from class_objects import House, Water, Matrix
import algorithm.random as random
import setup as info
import house_dictionary as hd

def main():

	matrix = Matrix(info.grid_length,info.grid_width)
	grid = matrix.grid

	# print grid
	print("start:")
	random.fill(grid, matrix)
	print(grid)

	total_score = 0

	for i in hd.houses_e:
		print("{} score: " .format(hd.houses_e[i].id))
		matrix.free_space(grid, hd.houses_e[i], hd.houses_e[i].id, info.house_e_length, info.house_e_width)
		score = matrix.score(hd.houses_e[i], info.scale, info.house_e_value, info.house_e_free, info.house_e_increment)
		total_score = total_score + score
		print(score)

	for i in hd.houses_b:
		print("{} score: " .format(hd.houses_b[i].id))
		matrix.free_space(grid, hd.houses_b[i], hd.houses_b[i].id, info.house_b_length, info.house_b_width)
		score = matrix.score(hd.houses_b[i], info.scale, info.house_b_value, info.house_b_free, info.house_b_increment)
		total_score = total_score + score
		print(score)

	for i in hd.houses_m:
		print("{} score: " .format(hd.houses_m[i].id))
		matrix.free_space(grid, hd.houses_m[i], hd.houses_m[i].id, info.house_m_length, info.house_m_width)
		score = matrix.score(hd.houses_m[i], info.scale, info.house_m_value, info.house_m_free, info.house_m_increment)
		total_score = total_score + score
		print(score)

	print("Total score: ")
	print(total_score)

	return matrix, grid, total_score

	# export grid to csv file
	#matrix.export(grid)

	# write to end of csv file
	#fd = open('score.csv','a')
	#fd.write(str(total_score) + ',')
	#fd.close()


if __name__ == "__main__":
	main()
