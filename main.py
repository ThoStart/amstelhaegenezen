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
import library.start as start
import numpy as np
import timeit
import sys
import importlib

def main():
	chosen_algorithm, water_layout, number_of_runs, visualize_data, plot_data = start.start()

	# start runtime
	starttime = timeit.default_timer()

	# declare highest score with lowest possible score
	highest_score = 0

	# declare lowest score with highest possible score
	lowest_score = 10**10

	# declare data array of scores
	data = []

	run_iteration = number_of_runs

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

		print("Grid created successfully")

		# execute hill climbing or simulated annealing
		if chosen_algorithm == 2 or chosen_algorithm == 3 or chosen_algorithm == 5 or chosen_algorithm == 6:
			total_score = score.calculate(grid, matrix, hd.houses_e, hd.houses_b, hd.houses_m)

			if visualize_data == 'Y':
				if chosen_algorithm == 2 or chosen_algorithm == 5:
					tk_export.create(matrix, grid, (str(total_score) + " (before hill climbing)"))
				else:
					tk_export.create(matrix, grid, (str(total_score) + " (before simulated annealing)"))

			matrix_before = Matrix(info.grid_length,info.grid_width)
			matrix_before.grid = grid.copy()
			grid_before = matrix_before.grid
			score_before = total_score

			# execute hill climbing algorithm
			if chosen_algorithm == 2 or chosen_algorithm == 5:
				hc_data = algorithm.hill_climbing.start(matrix, grid)

			# execute simulated annealing
			elif chosen_algorithm == 3 or chosen_algorithm == 6:
				hc_data = algorithm.SimulatedAnnealing.start(matrix, grid)

			if visualize_data == 'Y':
				total_score = score.calculate(grid, matrix, hd.houses_e, hd.houses_b, hd.houses_m)
				if chosen_algorithm == 2 or chosen_algorithm == 5:
					tk_export.create(matrix, grid, (str(total_score) + " (after hill climbing)"))
				else:
					tk_export.create(matrix, grid, (str(total_score) + " (after simulated annealing)"))

		# generate total score
		total_score = score.calculate(grid, matrix, hd.houses_e, hd.houses_b, hd.houses_m)

		# grid fill succeeded
		if total_score != 1:
			data.append(total_score)

			# save best grid
			if total_score > highest_score:

				if chosen_algorithm == 2 or chosen_algorithm == 3 or chosen_algorithm == 5 or chosen_algorithm == 6:
					# before HC/SA
					highest_matrix_before = matrix_before
					highest_grid_before = grid_before
					highest_score_before = score_before

				# after HC/SA
				highest_matrix = matrix
				highest_grid = grid
				highest_score = total_score
				hc_data_highest = hc_data

			if total_score < lowest_score:
				lowest_matrix = matrix
				lowest_grid = grid
				lowest_score = total_score

			run_iteration-=1

		# reset dict files and values
		importlib.reload(hd)

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

if __name__ == "__main__":
	main()
