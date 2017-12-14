from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd
import library.tk_export as tk_export
import library.score as score

def start(matrix, grid):

	simulated_annealing_matrix = Matrix(info.grid_length, info.grid_width)

	temperature = 0
	#min_temperature = 0
	max_temperature = 100
	save_best_grid()

	# before hill climbing algorithm
	total_score = score.calculate(grid, matrix)
	#tk_export.create(matrix, grid, (str(total_score) + " (before hill climbing)"))

	# create score list
	hc_data = []

	# swap E and B
	for i in hd.houses_e:
		for j in hd.houses_b:
			Matrix.swap(matrix, grid, hd.houses_e[i], hd.houses_b[j])
			total_score_new = score.calculate(grid, matrix)
			check_for_simulated_annealing(temperature, max_temperature, total_score, total_score_new)

	# swap B and M
	for i in hd.houses_b:
		for j in hd.houses_m:
			Matrix.swap(matrix, grid, hd.houses_b[i], hd.houses_m[j])
			total_score_new = score.calculate(grid, matrix)
			check_for_simulated_annealing(temperature, max_temperature, total_score, total_score_new)

	# swap E and M
	for i in hd.houses_e:
		for j in hd.houses_m:
			Matrix.swap(matrix, grid, hd.houses_e[i], hd.houses_m[j])
			total_score_new = score.calculate(grid, matrix)
			check_for_simulated_annealing(temperature, max_temperature, total_score, total_score_new)

def check_for_simulated_annealing(temperature, max_temperature, total_score, total_score_new):
	# if temperature is lower than max temperature save changes
	if temperature < max_temperature:

		# if score is not better than previous score increment temperature
		if total_score_new < total_score:
			temperature+=1

		# if new highest score save changes in best grid
		elif total_score_new > total_score:
			save_best_grid(grid)

		total_score = total_score_new
		hc_data.append(total_score)

	# when max temperature is reached end algorithm
	elif temperature == max_temperature:
			grid = simulated_annealing_matrix
			return hc_data

def save_best_grid(grid):
		simulated_annealing_matrix.grid = grid
