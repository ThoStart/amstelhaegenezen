#!/usr/bin/env python3

from classes.class_objects import House, Water, Matrix
import algorithm.random
import algorithm.greedy
import algorithm.hill_climbing
import algorithm.SimulatedAnnealing
import library.score as score
import library.setup as info
import library.house_dictionary as hd
import library.tk_export as tk_export
import library.free_space as free_space
import library.water as water
import numpy as np
import timeit
import sys
import importlib

def main():
	chosen_algorithm, water_layout, number_of_runs, visualize_data, plot_data = start()

	# Greedy does not work properly (yet)
	# if chosen_algorithm == 3 or chosen_algorithm == 4:
	# 	print("Sorry, this algorithm takes ages. Aborting.")
	# 	return 1

	# start runtime
	starttime = timeit.default_timer()

	# declare highest score with lowest possible score
	highest_score = 0

	# declare lowest score with highest possible score
	lowest_score = 10**10

	# declare data array of scores
	data = []

	run_iteration = number_of_runs

	# open csv file, write at start
	#fd = open('score.csv','w')

	while run_iteration > 0:
		hc_data = 0

		# create grid
		matrix = Matrix(info.grid_length,info.grid_width)
		grid = matrix.grid

		# fill grid with water
		water.fill(matrix, grid, water_layout)

		# fill grid with random algorithm
		if chosen_algorithm == 1 or chosen_algorithm == 2 or chosen_algorithm == 3:
			algorithm.random.fill(grid, matrix)

		# fill grid with greedy algorithm
		if chosen_algorithm == 4 or chosen_algorithm == 5 or chosen_algorithm == 6:
			algorithm.greedy.fill(grid, matrix)

		print("grid success")

		# execute hill climbing algorithm
		if chosen_algorithm == 2 or chosen_algorithm == 3 or chosen_algorithm == 5 or chosen_algorithm == 6:
			if visualize_data == 'Y':
				total_score = score.calculate(grid, matrix)
				if chosen_algorithm == 2 or chosen_algorithm == 5:
					tk_export.create(matrix, grid, (str(total_score) + " (before hill climbing)"))
				else:
					tk_export.create(matrix, grid, (str(total_score) + " (before simulated annealing)"))

				matrix_before = Matrix(info.grid_length,info.grid_width)
				matrix_before.grid = grid.copy()
				grid_before = matrix_before.grid
				score_before = total_score

			if chosen_algorithm == 2 or chosen_algorithm == 5:
				hc_data = algorithm.hill_climbing.start(matrix, grid)
			elif chosen_algorithm == 3 or chosen_algorithm == 6:
				hc_data = algorithm.SimulatedAnnealing.start(matrix, grid)

			if visualize_data == 'Y':
				total_score = score.calculate(grid, matrix)
				if chosen_algorithm == 2 or chosen_algorithm == 5:
					tk_export.create(matrix, grid, (str(total_score) + " (after hill climbing)"))
				else:
					tk_export.create(matrix, grid, (str(total_score) + " (after simulated annealing)"))

		# generate total score
		total_score = score.calculate(grid, matrix)

		# grid fill succeeded
		if total_score != 1:
			data.append(total_score)

			# add total score to csv file
			#fd.write(str(total_score) + ',')

			# save best grid
			if total_score > highest_score:

				if chosen_algorithm == 2 or chosen_algorithm == 3 or chosen_algorithm == 5 or chosen_algorithm == 6:
					# before HC
					highest_matrix_before = matrix_before
					highest_grid_before = grid_before
					highest_score_before = score_before

				# after HC
				highest_matrix = matrix
				highest_grid = grid
				highest_score = total_score
				hc_data_highest = hc_data
				#matrix.export(highest_grid)

			if total_score < lowest_score:
				lowest_matrix = matrix
				lowest_grid = grid
				lowest_score = total_score

			run_iteration-=1

		# reset dict files and values
		importlib.reload(hd)

	# close csv file
	#fd.close()

	# stop and show runtime
	stop = timeit.default_timer()
	print("runtime: {}" .format(stop-starttime))
	# use tkinter to visualize grid
	if visualize_data == 'Y':
		if number_of_runs == 1:
			if chosen_algorithm == 2 or chosen_algorithm == 5:
				tk_export.create(highest_matrix_before, highest_grid_before, (str(highest_score_before) + " (highest score before HC)"))
				tk_export.create(highest_matrix, highest_grid, (str(lowest_score) + " (highest score after HC)"))
			elif chosen_algorithm == 3 or chosen_algorithm == 6:
				tk_export.create(highest_matrix_before, highest_grid_before, (str(highest_score_before) + " (highest score before SA)"))
				tk_export.create(highest_matrix, highest_grid, (str(lowest_score) + " (highest score after SA)"))
		else:
			if chosen_algorithm == 2 or chosen_algorithm == 5:
				tk_export.create(highest_matrix_before, highest_grid_before, (str(highest_score_before) + " (before HC)"))
				tk_export.create(highest_matrix, highest_grid, (str(highest_score) + " (after HC)"))
			elif chosen_algorithm == 3 or chosen_algorithm == 6:
				tk_export.create(highest_matrix_before, highest_grid_before, (str(highest_score_before) + " (before SA)"))
				tk_export.create(highest_matrix, highest_grid, (str(highest_score) + " (after SA)"))
			tk_export.create(lowest_matrix, lowest_grid, (str(lowest_score) + " (lowest score)"))
			tk_export.create(highest_matrix, highest_grid, (str(highest_score) + " (highest score)"))

	# use matplotlib to visualize normal distribution graph
	# imported here due to matplotlib interfering with tkinter
	import library.plot_export as plot_export

	if (chosen_algorithm == 2 or chosen_algorithm == 3 or chosen_algorithm == 5 or chosen_algorithm == 6) and plot_data == 'Y':
		plot_export.line(hc_data_highest, chosen_algorithm)

	if plot_data == 'Y' and number_of_runs > 1:
		plot_export.normal(data, highest_score)

# Request user input the first time
def start():
	print("1: Random")
	print("2: Random + Hill climbing")
	print("3: Random + Simulated annealing")
	print("4: Greedy")
	print("5: Greedy + Hill climbing")
	print("6: Greedy + Simulated annealing")

	chosen_algorithm = input("Algorithm: ")
	while (len(str(chosen_algorithm)) > 1 or
	chosen_algorithm.isdigit() == False or
	int(chosen_algorithm) > 6 or
	int(chosen_algorithm) <= 0):
		print("Invalid input, try again.")
		chosen_algorithm = input("Algorithm: ")

	print("1:            2:\n◼︎ ◼︎ ◼︎ ◼︎ ◻︎ ◻︎   ◼︎ ◼︎ ◻︎ ◻︎ ◼︎ ◼︎\n◼︎ ◼︎ ◻︎ ◻︎ ◻︎ ◻︎   ◼︎ ◼︎ ◻︎ ◻︎ ◼︎ ◼︎\n◼︎ ◼︎ ◻︎ ◻︎ ◻︎ ◻︎   ◻︎ ◻︎ ◻︎ ◻︎ ◻︎ ◻︎\n◻︎ ◻︎ ◻︎ ◻︎ ◼︎ ◼︎   ◻︎ ◻︎ ◻︎ ◻︎ ◻︎ ◻︎\n◻︎ ◻︎ ◻︎ ◻︎ ◼︎ ◼︎   ◼︎ ◼︎ ◻︎ ◻︎ ◼︎ ◼︎\n◻︎ ◻︎ ◼︎ ◼︎ ◼︎ ◼︎   ◼︎ ◼︎ ◻︎ ◻︎ ◼︎ ◼︎")
	water_layout = input("Water layout: ")
	while (len(str(water_layout)) > 1 or
	water_layout.isdigit() == False or
	int(water_layout) > 2 or
	int(water_layout) <= 0):
		print("Invalid input, try again.")
		water_layout = input("Water layout: ")

	number_of_runs = input("Number of runs: ")
	while (number_of_runs.isdigit() == False or int(number_of_runs) <= 0):
		print("Invalid input, try again.")
		number_of_runs = input("Number of runs: ")

	visualize_data = input("Visualize data (y/n): ")
	while (visualize_data.upper().startswith('Y') == False and
	visualize_data.upper().startswith('N') == False):
		print("Invalid input, try again.")
		visualize_data = input("Visualize data (y/n): ")

	plot_data = input("Plot data (y/n): ")
	while (plot_data.upper().startswith('Y') == False and
	plot_data.upper().startswith('N') == False):
		print("Invalid input, try again.")
		plot_data = input("Plot data (y/n): ")

	return int(chosen_algorithm), int(water_layout), int(number_of_runs), visualize_data.upper()[0], plot_data.upper()[0]

if __name__ == "__main__":
	main()
