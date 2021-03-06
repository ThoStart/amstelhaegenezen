from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd
import library.score as score
import library.progressbar as progressbar
import numpy as np
import random

def start(matrix, grid):

	# declare variables
	hc_data = []
	iteration = 0
	total = 1000

	print("Hill Climbing:")
	progressbar.printProgressBar(iteration, total, prefix = 'Progress:', suffix = 'Complete', length = 50)

	# swap all houses with one-another
	iteration = execute_swap(grid, matrix, hc_data, hd.houses_e, hd.houses_b, iteration, total)
	iteration = execute_swap(grid, matrix, hc_data, hd.houses_b, hd.houses_m, iteration, total)
	iteration = execute_swap(grid, matrix, hc_data, hd.houses_m, hd.houses_e, iteration, total)
	iteration = execute_swap(grid, matrix, hc_data, hd.houses_e, hd.houses_b, iteration, total)

	swap_number = len(hc_data)
	number_of_iterations = total - (swap_number * 2)

	# relocate houses
	for times in range(int(np.ceil(number_of_iterations / info.number_of_houses))):
		for i in hd.houses_e:
			if len(hc_data) >= number_of_iterations + swap_number:
				break
			iteration = execute_random(grid, matrix, hc_data,hd.houses_e[i], swap_number, iteration, total)
		for i in hd.houses_b:
			if len(hc_data) >= number_of_iterations + swap_number:
				break
			iteration = execute_random(grid, matrix, hc_data,hd.houses_b[i], swap_number, iteration, total)
		for i in hd.houses_m:
			if len(hc_data) >= number_of_iterations + swap_number:
				break
			iteration = execute_random(grid, matrix, hc_data,hd.houses_m[i], swap_number, iteration, total)

	# swap all houses with one-another
	iteration = execute_swap(grid, matrix, hc_data, hd.houses_e, hd.houses_b, iteration, total)
	iteration = execute_swap(grid, matrix, hc_data, hd.houses_b, hd.houses_m, iteration, total)
	iteration = execute_swap(grid, matrix, hc_data, hd.houses_m, hd.houses_e, iteration, total)
	iteration = execute_swap(grid, matrix, hc_data, hd.houses_e, hd.houses_b, iteration, total)

	return hc_data

# swap house a and house b
def execute_swap(grid, matrix, hc_data, houses_a, houses_b, iteration, total):
	total_score = score.calculate(grid, matrix, hd.houses_e, hd.houses_b, hd.houses_m)

	for i in houses_a:
		for j in houses_b:
			iteration+=1
			progressbar.printProgressBar(iteration, total, prefix = 'Progress:', suffix = 'Complete', length = 50)
			Matrix.swap(matrix, grid, houses_a[i], houses_b[j])
			total_score_new = score.calculate(grid, matrix, hd.houses_e, hd.houses_b, hd.houses_m)

			if total_score_new < total_score:
				hc_data.append(total_score)
				Matrix.swap(matrix, grid, houses_a[i], houses_b[j])
				total_score = score.calculate(grid, matrix, hd.houses_e, hd.houses_b, hd.houses_m)
			else:
				total_score = total_score_new
				hc_data.append(total_score)

	return iteration

# relocate house to free place
def execute_random(grid, matrix, hc_data, house, swap_number, iteration, total):

	if len(hc_data) >= (1000 - swap_number):
		return 0

	total_score = score.calculate(grid, matrix, hd.houses_e, hd.houses_b, hd.houses_m)

	# declare empty space variables
	house_x_free = eval("info.house_" + str.lower(house.id[:1]) + "_free")
	house_x_length = eval("info.house_" + str.lower(house.id[:1]) + "_length")
	house_x_width = eval("info.house_" + str.lower(house.id[:1]) + "_width")
	house_x_value = eval("info.house_" + str.lower(house.id[:1]) + "_value")
	house_x_type = eval("info.house_" + str.lower(house.id[:1]) + "_type")

	# check if house can be placed
	for i in range (10000):
		# random x and y
		x_coordinate = random.randint(house_x_free, info.grid_length - house_x_length - house_x_free)
		y_coordinate = random.randint(house_x_free, info.grid_width - house_x_width - house_x_free)

		check = matrix.check(house_x_length, house_x_width, house_x_free, x_coordinate, y_coordinate)
		if check == 0:
			break

	# create and place house
	if check == 0:
		temp_house = House(house_x_type, 'v', house_x_free, house_x_value, x_coordinate, y_coordinate, house_x_length, house_x_width)

		Matrix.swap(matrix, grid, house, temp_house)
		iteration+=1
		progressbar.printProgressBar(iteration, total, prefix = 'Progress:', suffix = 'Complete', length = 50)
		total_score_new = score.calculate(grid, matrix, hd.houses_e, hd.houses_b, hd.houses_m)

		if total_score_new < total_score:
			hc_data.append(total_score)
			Matrix.swap(matrix, grid, house, temp_house)
			total_score = score.calculate(grid, matrix, hd.houses_e, hd.houses_b, hd.houses_m)
		else:
			total_score = total_score_new
			hc_data.append(total_score)
	else:
		total_score = total_score_new
		hc_data.append(total_score)

	return iteration
