from class_objects import House, Water, Matrix
import random
import setup as info


def fill_random(matrix, grid, house_e_counter):


	# random x and y
	x_coordinate = random.randint(0, info.grid_length - info.house_e_length)
	y_coordinate = random.randint(0, info.grid_width - info.house_e_width)

	# check if house can be placed
	check = matrix.check(info.house_e_length, info.house_e_width, x_coordinate, y_coordinate)

	# place house
	if check == 0:
		# create and place house
		houses_e[house_e_counter] = House("Eengezinswoning", house_e_counter, info.house_e_length, info.house_e_width, info.house_e_free, info.house_e_value, info.house_e_increment)

		matrix.place(info.house_e_length, info.house_e_width, x_coordinate, y_coordinate, ("E{0:02}".format(houses_e[house_e_counter].id)))

		house_e_counter = house_e_counter + 1

	return grid