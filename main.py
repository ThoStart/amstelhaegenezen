#!/usr/bin/env python3

from class_objects import House, Water, Matrix
import algorithm.random_fill as algorithm
import score
import setup as info
import house_dictionary as hd

def main():

	# create grid
	matrix = Matrix(info.grid_length,info.grid_width)
	grid = matrix.grid

	# fill grid with algorithm and print grid
	algorithm.fill(grid, matrix)
	print(grid)

	# generate total score
	total_score = score.calculate(grid, matrix)
	#print("Total score: {}" .format(total_score))

	return matrix, grid, total_score

	# # export grid to csv file
	# matrix.export(grid)
    #
	# write to end of csv file
	# fd = open('score.csv','a')
	# fd.write(str(total_score) + ',')
	# fd.close()

if __name__ == "__main__":
	main()
