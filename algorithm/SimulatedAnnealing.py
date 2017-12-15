from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd
import library.tk_export as tk_export
import library.score as score
import numpy as np
from copy import copy, deepcopy
from time import sleep
import library.progressbar as progressbar

def start(matrix, grid):
	temp_houses_e, temp_houses_b, temp_houses_m = dict(), dict(), dict()

	simulated_annealing_matrix = Matrix(info.grid_length, info.grid_width)
	sa_grid = simulated_annealing_matrix.grid
	sa_grid = deepcopy(grid)

	sim_an_matrix = Matrix(info.grid_length, info.grid_width)
	thesims_grid = sim_an_matrix.grid
	# np.copyto(thesims_grid, grid)

	temp_houses_e = deepcopy(hd.houses_e)
	temp_houses_b = deepcopy(hd.houses_b)
	temp_houses_m = deepcopy(hd.houses_m)

	temperature = 0
	#min_temperature = 0
	max_temperature = 5
	#save_best_grid()
	iteration = 0
	total = 111

	print("Simulated Annealing:")
	# Initial call to print 0% progress
	progressbar.printProgressBar(iteration, total, prefix = 'Progress:', suffix = 'Complete', length = 50)

	# before simulated annealing algorithm
	total_score = score.calculate(grid, matrix)
	#tk_export.create(matrix, grid, (str(total_score) + " (before hill climbing)"))

	# create score list
	hc_data = []

	hc_data.append(total_score)
	# swap E and B
	for i in hd.houses_e:
		for j in hd.houses_b:

			 # Update Progress Bar
			iteration+=1
			progressbar.printProgressBar(iteration + 1, total, prefix = 'Progress:', suffix = 'Complete', length = 50)

			Matrix.swap(matrix, grid, hd.houses_e[i], hd.houses_b[j])
			total_score_new = score.calculate(grid, matrix)
			total_score_sims = score.calculate_annealing(thesims_grid, sim_an_matrix, temp_houses_e, temp_houses_b, temp_houses_m)

			if total_score_new >= total_score_sims:
				temp_houses_e = deepcopy(hd.houses_e)
				temp_houses_b = deepcopy(hd.houses_b)
				temp_houses_m = deepcopy(hd.houses_m)
				np.copyto(thesims_grid, grid)

			total_score_sims = score.calculate_annealing(thesims_grid, sim_an_matrix, temp_houses_e, temp_houses_b, temp_houses_m)

			total_score, temperature = check_for_simulated_annealing(hc_data, temperature, max_temperature, total_score, total_score_new, simulated_annealing_matrix, grid, sa_grid)

	# swap B and M
	for i in hd.houses_b:
		for j in hd.houses_m:

			# Update Progress Bar
			iteration+=1
			progressbar.printProgressBar(iteration + 1, total, prefix = 'Progress:', suffix = 'Complete', length = 50)

			Matrix.swap(matrix, grid, hd.houses_b[i], hd.houses_m[j])
			total_score_new = score.calculate(grid, matrix)

			total_score_sims = score.calculate_annealing(thesims_grid, sim_an_matrix, temp_houses_e, temp_houses_b, temp_houses_m)

			if total_score_new >= total_score_sims:
				temp_houses_e = deepcopy(hd.houses_e)
				temp_houses_b = deepcopy(hd.houses_b)
				temp_houses_m = deepcopy(hd.houses_m)
				np.copyto(thesims_grid, grid)

			total_score_sims = score.calculate_annealing(thesims_grid, sim_an_matrix, temp_houses_e, temp_houses_b, temp_houses_m)

			total_score, temperature = check_for_simulated_annealing(hc_data, temperature, max_temperature, total_score, total_score_new, simulated_annealing_matrix, grid, sa_grid)

	# swap E and M
	for i in hd.houses_e:
		for j in hd.houses_m:

			# Update Progress Bar
			iteration+=1
			progressbar.printProgressBar(iteration, total, prefix = 'Progress:', suffix = 'Complete', length = 50)

			Matrix.swap(matrix, grid, hd.houses_e[i], hd.houses_m[j])
			total_score_new = score.calculate(grid, matrix)

			total_score_sims = score.calculate_annealing(thesims_grid, sim_an_matrix, temp_houses_e, temp_houses_b, temp_houses_m)

			if total_score_new >= total_score_sims:
				temp_houses_e = deepcopy(hd.houses_e)
				temp_houses_b = deepcopy(hd.houses_b)
				temp_houses_m = deepcopy(hd.houses_m)
				np.copyto(thesims_grid, grid)

			total_score_sims = score.calculate_annealing(thesims_grid, sim_an_matrix, temp_houses_e, temp_houses_b, temp_houses_m)

			total_score, temperature = check_for_simulated_annealing(hc_data, temperature, max_temperature, total_score, total_score_new, simulated_annealing_matrix, grid, sa_grid)

	if total_score_new > total_score:
		total_score = total_score_new
		sa_grid = grid.copy()

	total_score_lala = score.calculate_annealing(thesims_grid, sim_an_matrix, temp_houses_e, temp_houses_b, temp_houses_m)

	if total_score_lala >= total_score:
		total_score = total_score_lala
		hd.houses_e = deepcopy(temp_houses_e)
		hd.houses_b = deepcopy(temp_houses_b)
		hd.houses_m = deepcopy(temp_houses_m)
		grid = np.copy(thesims_grid)

	total_score = score.calculate(grid, matrix)
	total_score = score.calculate(sa_grid, simulated_annealing_matrix)


	return hc_data

def check_for_simulated_annealing(hc_data, temperature, max_temperature, total_score, total_score_new, simulated_annealing_matrix, grid, sa_grid):
	# if temperature is lower than max temperature
	if temperature < max_temperature:
		temperature+=1
		hc_data.append(total_score_new)

	# when max temperature is reached end algorithm
	elif temperature == max_temperature:
		# grid = simulated_annealing_matrix.grid
		if total_score_new > total_score:
			total_score = total_score_new
			sa_grid = deepcopy(grid)
			hc_data.append(total_score_new)
		else:
			grid = deepcopy(sa_grid)
			hc_data.append(total_score_new)

			for i in range(max_temperature):
				hc_data.pop()

		temperature = 0

	return total_score, temperature
