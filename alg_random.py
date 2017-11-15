from class_objects import House, Water, Matrix
import random
import setup as info
import house_dictionary as hd

def fill(grid, matrix):
	# place 7 sets of houses

	# Eengezinswoningen

	# random x and y
	for i in range(info.house_e_number):

		# check if house can be placed
		for i in range (10000):
			# random x and y
			x_coordinate = random.randint(info.house_e_free, info.grid_length - info.house_e_length - info.house_e_free)
			y_coordinate = random.randint(info.house_e_free, info.grid_width - info.house_e_width - info.house_e_free)

			check = matrix.check(info.house_e_length, info.house_e_width, info.house_e_free, x_coordinate, y_coordinate)
			if check == 0:
				break

		# place house
		if check == 0:
			# create and place house
			hd.houses_e[hd.house_e_counter] = House(info.house_e_type, hd.house_e_counter, info.house_e_free, info.house_e_value, x_coordinate, y_coordinate)

			matrix.place(info.house_e_length, info.house_e_width, x_coordinate, y_coordinate, ("E{0:02}".format(hd.houses_e[hd.house_e_counter].id)))

			print("success E{0:02}".format(hd.houses_e[hd.house_e_counter].id))

			hd.house_e_counter = hd.house_e_counter + 1


	# Bungalows

	for i in range(info.house_b_number):

		for i in range(10000):
			# random x and y
			x_coordinate = random.randint(info.house_b_free, info.grid_length - info.house_b_length - info.house_b_free)
			y_coordinate = random.randint(info.house_b_free, info.grid_width - info.house_b_width - info.house_b_free)

			# check if house can be placed
			check = matrix.check(info.house_b_length, info.house_b_width, info.house_b_free, x_coordinate, y_coordinate)
			if check == 0:
				break

		# place house
		if check == 0:
			# create and place house
			hd.houses_b[hd.house_b_counter] = House(info.house_b_type, hd.house_b_counter, info.house_b_free, info.house_b_value, x_coordinate, y_coordinate)

			matrix.place(info.house_b_length, info.house_b_width, x_coordinate, y_coordinate, ("B{0:02}".format(hd.houses_b[hd.house_b_counter].id)))

			print("success B{0:02}".format(hd.houses_b[hd.house_b_counter].id))

			hd.house_b_counter = hd.house_b_counter + 1

	# Maisons

	for i in range(info.house_m_number):

		for i in range(10000):
			# random x and y
			x_coordinate = random.randint(info.house_m_free, info.grid_length - info.house_m_length - info.house_m_free)
			y_coordinate = random.randint(info.house_m_free, info.grid_width - info.house_m_width - info.house_m_free)

			# check if house can be placed
			check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, x_coordinate, y_coordinate)
			if check == 0:
				break

		# place house
		if check == 0:
			# create and place house
			hd.houses_m[hd.house_m_counter] = House(info.house_m_type, hd.house_m_counter, info.house_m_free, info.house_m_value,  x_coordinate, y_coordinate)

			matrix.place(info.house_m_length, info.house_m_width, x_coordinate, y_coordinate, ("M{0:02}".format(hd.houses_m[hd.house_m_counter].id)))

			print("success M{0:02}".format(hd.houses_m[hd.house_m_counter].id))

			hd.house_m_counter = hd.house_m_counter + 1
