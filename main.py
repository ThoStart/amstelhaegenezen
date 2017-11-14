#!/usr/bin/env python3

from class_objects import House, Water, Matrix
import random
import setup as info

def main():

	# declare house variables
	house_e_counter, house_b_counter, house_m_counter = 1, 1, 1
	houses_e, houses_b, houses_m = dict(), dict(), dict()

	matrix = Matrix(info.grid_length,info.grid_width)
	grid = matrix.grid

	# print grid
	print("start:")
	print(grid)


	# Water
	matrix.place(info.water_length, info.water_width, 0, 0, "~")

	# place 10 sets of houses
	for i in range(7):

		# Eengezinswoningen

		# random x and y
		for i in range(info.house_e_ratio):

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
				houses_e[house_e_counter] = House(info.house_e_type, house_e_counter, info.house_e_length, info.house_e_width, info.house_e_free, info.house_e_value, info.house_e_increment)

				matrix.place(info.house_e_length, info.house_e_width, x_coordinate, y_coordinate, ("E{0:02}".format(houses_e[house_e_counter].id)))
			
				print("success E{0:02}".format(houses_e[house_e_counter].id))

				house_e_counter = house_e_counter + 1


		# Bungalows

		for i in range(info.house_b_ratio):

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
				houses_b[house_b_counter] = House(info.house_b_type, house_b_counter, info.house_b_length, info.house_b_width, info.house_b_free, info.house_b_value, info.house_b_increment)

				matrix.place(info.house_b_length, info.house_b_width, x_coordinate, y_coordinate, ("B{0:02}".format(houses_b[house_b_counter].id)))
			
				print("success B{0:02}".format(houses_b[house_b_counter].id))

				house_b_counter = house_b_counter + 1


		# Maisons

		# random x and y
		for i in range(info.house_m_ratio):

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
				houses_m[house_m_counter] = House(info.house_m_type, house_m_counter, info.house_m_length, info.house_m_width, info.house_m_free, info.house_m_value, info.house_m_increment)

				matrix.place(info.house_m_length, info.house_m_width, x_coordinate, y_coordinate, ("M{0:02}".format(houses_m[house_m_counter].id)))
			
				print("success M{0:02}".format(houses_m[house_m_counter].id))

				house_m_counter = house_m_counter + 1


	print(grid)

	# export grid to csv file
	matrix.export(grid)


if __name__ == "__main__":
	main()
