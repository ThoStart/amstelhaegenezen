from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd
import library.tk_export as tk_export
import library.score as score
import numpy as np
from copy import copy, deepcopy

def start(matrix, grid):

	simulated_annealing_matrix = Matrix(info.grid_length, info.grid_width)
	sa_grid = simulated_annealing_matrix.grid
	np.copyto(sa_grid, grid)

	sim_an_matrix = Matrix(info.grid_length, info.grid_width)
	thesims_grid = sim_an_matrix.grid
	# np.copyto(thesims_grid, grid)

	hd.temp_houses_e = deepcopy(hd.houses_e)
	hd.temp_houses_b = deepcopy(hd.houses_b)
	hd.temp_houses_m = deepcopy(hd.houses_m)

	temperature = 0
	#min_temperature = 0
	max_temperature = 5
	#save_best_grid()

	# before hill climbing algorithm
	total_score = score.calculate(grid, matrix)
	#tk_export.create(matrix, grid, (str(total_score) + " (before hill climbing)"))

	# create score list
	hc_data = []

	hc_data.append(total_score)
	# swap E and B
	for i in hd.houses_e:
		for j in hd.houses_b:
			Matrix.swap(matrix, grid, hd.houses_e[i], hd.houses_b[j])
			total_score_new = score.calculate(grid, matrix)

			if total_score_new >= total_score:
				hd.temp_houses_e = deepcopy(hd.houses_e)
				hd.temp_houses_b = deepcopy(hd.houses_b)
				hd.temp_houses_m = deepcopy(hd.houses_m)
				np.copyto(thesims_grid, grid)

			total_score_sims = score.calculate_deux(thesims_grid, sim_an_matrix)

			total_score, temperature = check_for_simulated_annealing(hc_data, temperature, max_temperature, total_score, total_score_new, simulated_annealing_matrix, grid, sa_grid)

	# swap B and M
	for i in hd.houses_b:
		for j in hd.houses_m:
			Matrix.swap(matrix, grid, hd.houses_b[i], hd.houses_m[j])
			total_score_new = score.calculate(grid, matrix)

			# total_score_sims = score.calculate_deux(thesims_grid, sim_an_matrix)

			if total_score_new >= total_score:
				hd.temp_houses_e = deepcopy(hd.houses_e)
				hd.temp_houses_b = deepcopy(hd.houses_b)
				hd.temp_houses_m = deepcopy(hd.houses_m)
				np.copyto(thesims_grid, grid)

			total_score_sims = score.calculate_deux(thesims_grid, sim_an_matrix)

			total_score, temperature = check_for_simulated_annealing(hc_data, temperature, max_temperature, total_score, total_score_new, simulated_annealing_matrix, grid, sa_grid)

	# swap E and M
	for i in hd.houses_e:
		for j in hd.houses_m:
			Matrix.swap(matrix, grid, hd.houses_e[i], hd.houses_m[j])
			total_score_new = score.calculate(grid, matrix)

			total_score_sims = score.calculate_deux(thesims_grid, sim_an_matrix)

			if total_score_new >= total_score:
				hd.temp_houses_e = deepcopy(hd.houses_e)
				hd.temp_houses_b = deepcopy(hd.houses_b)
				hd.temp_houses_m = deepcopy(hd.houses_m)
				np.copyto(thesims_grid, grid)

			total_score_sims = score.calculate_deux(thesims_grid, sim_an_matrix)

			total_score, temperature = check_for_simulated_annealing(hc_data, temperature, max_temperature, total_score, total_score_new, simulated_annealing_matrix, grid, sa_grid)

	if total_score_new > total_score:
		total_score = total_score_new
		sa_grid = grid.copy()
		print("yeah")


	total_score_lala = score.calculate_deux(thesims_grid, sim_an_matrix)

	if total_score_lala >= total_score:
		total_score = total_score_lala
		hd.houses_e = deepcopy(hd.temp_houses_e)
		hd.houses_b = deepcopy(hd.temp_houses_b)
		hd.houses_m = deepcopy(hd.temp_houses_m)
		grid = np.copy(thesims_grid)
		print("sims")


	print(hd.houses_m)
	print(hd.temp_houses_m)

	# grid = sa_grid.copy()
	print(hc_data)
	print("yolo {}".format(total_score))
	total_score = score.calculate(grid, matrix)
	print("yolo2 {}".format(total_score))
	total_score = score.calculate(sa_grid, simulated_annealing_matrix)
	print("yolo3 {}".format(total_score))


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
			np.copyto(sa_grid, grid)
			print("yoyoyoyo")
			hc_data.append(total_score_new)
		else:
			np.copyto(grid, sa_grid)
			hc_data.append(total_score_new)

			for i in range(max_temperature):
				hc_data.pop()

		# 	# verwijder laatste temp keer uit hc data
			# del hc_data[-(temperature)]
			# hc_data = hc_data[-temperature]

		temperature = 0

	return total_score, temperature
