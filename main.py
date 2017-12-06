#!/usr/bin/env python3

from class_objects import House, Water, Matrix
#import algorithm as algorithm
import algorithm.random_fill
import algorithm.greedy
import algorithm.hill_climbing
import score
import setup as info
import house_dictionary as hd

def main():

	hc_data = 0
	# create grid
	matrix = Matrix(info.grid_length,info.grid_width)
	grid = matrix.grid

	# fill grid with algorithm and print grid
	algorithm.random_fill.fill(grid, matrix)
	print(grid)

	#hc_data = algorithm.hill_climbing.execute(matrix, grid)

	# generate total score
	total_score = score.calculate(grid, matrix)
	#print("Total score: {}" .format(total_score))

	return matrix, grid, total_score, hc_data

	# # export grid to csv file
	# matrix.export(grid)
    #
	# write to end of csv file
	# fd = open('score.csv','a')
	# fd.write(str(total_score) + ',')
	# fd.close()

if __name__ == "__main__":
	main()
