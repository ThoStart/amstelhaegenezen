from classes.class_objects import House, Water, Matrix
import random
import library.setup as info
import library.house_dictionary as hd

def fill(grid, matrix):

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

		# create and place house
		if check == 0:
			hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, x_coordinate, y_coordinate, info.house_e_length, info.house_e_width)
			matrix.place(info.house_e_length, info.house_e_width, x_coordinate, y_coordinate, hd.houses_e[hd.house_e_counter].id)

			print("success {}".format(hd.houses_e[hd.house_e_counter].id))

			hd.house_e_counter = hd.house_e_counter + 1

	# Bungalows

	for i in range(info.house_b_number):

		# check if house can be placed
		for i in range(10000):
			# random x and y
			x_coordinate = random.randint(info.house_b_free, info.grid_length - info.house_b_length - info.house_b_free)
			y_coordinate = random.randint(info.house_b_free, info.grid_width - info.house_b_width - info.house_b_free)

			check = matrix.check(info.house_b_length, info.house_b_width, info.house_b_free, x_coordinate, y_coordinate)
			if check == 0:
				break

		# create and place house
		if check == 0:
			hd.houses_b[hd.house_b_counter] = House(info.house_b_type, ("B{0:02}".format(hd.house_b_counter)), info.house_b_free, info.house_b_value, x_coordinate, y_coordinate, info.house_b_length, info.house_b_width)
			matrix.place(info.house_b_length, info.house_b_width, x_coordinate, y_coordinate, hd.houses_b[hd.house_b_counter].id)

			print("success {}".format(hd.houses_b[hd.house_b_counter].id))

			hd.house_b_counter = hd.house_b_counter + 1

		# if check failed, rotate house and check if house can be placed
		else:
			for i in range (10000):
				# random x and y
					x_coordinate = random.randint(info.house_b_free, info.grid_length - info.house_b_width - info.house_b_free)
					y_coordinate = random.randint(info.house_b_free, info.grid_width - info.house_b_length - info.house_b_free)

					check = matrix.check(info.house_b_width, info.house_b_length, info.house_b_free, x_coordinate, y_coordinate)
					if check == 0:
						break

			# create and place house
			if check == 0:
				hd.houses_b[hd.house_b_counter] = House(info.house_b_type, ("B{0:02}".format(hd.house_b_counter)), info.house_b_free, info.house_b_value, x_coordinate, y_coordinate, info.house_b_width, info.house_b_length)
				matrix.place(info.house_b_width, info.house_b_length, x_coordinate, y_coordinate, hd.houses_b[hd.house_b_counter].id)

				print("success {}".format(hd.houses_b[hd.house_b_counter].id))

				hd.house_b_counter = hd.house_b_counter + 1

			# house placement failed
			else:
				return 1

	# Maisons

	for i in range(info.house_m_number):

		# check if house can be placed
		for i in range(10000):
			# random x and y
			x_coordinate = random.randint(info.house_m_free, info.grid_length - info.house_m_length - info.house_m_free)
			y_coordinate = random.randint(info.house_m_free, info.grid_width - info.house_m_width - info.house_m_free)

			check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, x_coordinate, y_coordinate)
			if check == 0:
				break

		# create and place house
		if check == 0:
			hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value,  x_coordinate, y_coordinate, info.house_m_length, info.house_m_width)
			matrix.place(info.house_m_length, info.house_m_width, x_coordinate, y_coordinate, hd.houses_m[hd.house_m_counter].id)

			print("success {}".format(hd.houses_m[hd.house_m_counter].id))

			hd.house_m_counter = hd.house_m_counter + 1

		# if check failed, rotate house and check if house can be placed
		else:
			for i in range(10000):
				# random x and y
				x_coordinate = random.randint(info.house_m_free, info.grid_length - info.house_m_width - info.house_m_free)
				y_coordinate = random.randint(info.house_m_free, info.grid_width - info.house_m_length - info.house_m_free)

				check = matrix.check(info.house_m_width, info.house_m_length, info.house_m_free, x_coordinate, y_coordinate)
				if check == 0:
					break

			# create and place house
			if check == 0:
				hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value,  x_coordinate, y_coordinate, info.house_m_width, info.house_m_length)
				matrix.place(info.house_m_width, info.house_m_length, x_coordinate, y_coordinate, hd.houses_m[hd.house_m_counter].id)

				print("success {}".format(hd.houses_m[hd.house_m_counter].id))

				hd.house_m_counter = hd.house_m_counter + 1

			# house placement failed
			else:
				return 1
