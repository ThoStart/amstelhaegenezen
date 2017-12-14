from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd
import library.score as score
import numpy as np
import random

def start(matrix, grid):
	hc_data = []

	execute_swap(grid, matrix, hc_data, hd.houses_e, hd.houses_b)
	execute_swap(grid, matrix, hc_data, hd.houses_b, hd.houses_m)
	execute_swap(grid, matrix, hc_data, hd.houses_m, hd.houses_e)
	execute_swap(grid, matrix, hc_data, hd.houses_e, hd.houses_b)

	swap_number = len(hc_data)
	number_of_iterations = 1000 - (swap_number * 2)

	for times in range(int(np.ceil(number_of_iterations / info.number_of_houses))):
		for i in hd.houses_e:
			if len(hc_data) >= number_of_iterations + swap_number:
				break
			execute_random(grid, matrix, hc_data,hd.houses_e[i], swap_number)
		for i in hd.houses_b:
			if len(hc_data) >= number_of_iterations + swap_number:
				break
			execute_random(grid, matrix, hc_data,hd.houses_b[i], swap_number)
		for i in hd.houses_m:
			if len(hc_data) >= number_of_iterations + swap_number:
				break
			execute_random(grid, matrix, hc_data,hd.houses_m[i], swap_number)

	execute_swap(grid, matrix, hc_data, hd.houses_e, hd.houses_b)
	execute_swap(grid, matrix, hc_data, hd.houses_b, hd.houses_m)
	execute_swap(grid, matrix, hc_data, hd.houses_m, hd.houses_e)
	execute_swap(grid, matrix, hc_data, hd.houses_e, hd.houses_b)

	print(len(hc_data))

	# print(hc_data)

	return hc_data

def execute_swap(grid, matrix, hc_data, houses_a, houses_b):
	total_score = score.calculate(grid, matrix)

	for i in houses_a:
		for j in houses_b:
			Matrix.swap(matrix, grid, houses_a[i], houses_b[j])
			total_score_new = score.calculate(grid, matrix)

			if total_score_new < total_score:
				hc_data.append(total_score)
				Matrix.swap(matrix, grid, houses_a[i], houses_b[j])
				total_score = score.calculate(grid, matrix)
			else:
				total_score = total_score_new
				hc_data.append(total_score)

def execute_random(grid, matrix, hc_data, house, swap_number):

	if len(hc_data) >= (1000 - swap_number):
		return 0

	total_score = score.calculate(grid, matrix)

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
		total_score_new = score.calculate(grid, matrix)

		if total_score_new < total_score:
			hc_data.append(total_score)
			Matrix.swap(matrix, grid, house, temp_house)
			total_score = score.calculate(grid, matrix)
		else:
			total_score = total_score_new
			hc_data.append(total_score)
	else:
		total_score = total_score_new
		hc_data.append(total_score)
