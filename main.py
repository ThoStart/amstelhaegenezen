#!/usr/bin/env python3

from class_objects import House, Water
from random import randint
import matrix as matrix

def main():

	# declare house variables
	house_e_counter, house_b_counter, house_m_counter = 0, 0, 0
	houses_e, houses_b, houses_m = dict(), dict(), dict()

	# create a house E object
	# houses_e[house_e_counter] = House("Eengezinswoning", house_e_counter, 8, 8, 2, 285000, 3)
	# house_e_counter = house_e_counter + 1

	# print(houses_e[house_e_counter-1].id)
	# print("E{0:03}".format(houses_e[0].id))
	# print(houses_e[0].width)

	# create a house B object
	houses_b[house_b_counter] = House("Bungalow", house_b_counter, 10, 7.5, 3, 399000, 4)
	house_b_counter = house_b_counter + 1

	# create a house M object
	houses_m[house_m_counter] = House("Maison", house_m_counter, 11, 10.5, 6, 610000, 6)
	house_m_counter = house_m_counter + 1

	# generate grid
	xsize = 5
	ysize = 5
	grid = matrix.init(xsize,ysize)

	# print grid
	print("start:")
	print(grid)


	#house E00

	x_opp = 3
	y_opp = 3

	# random x and y
	x_coordinate = randint(0, xsize * 2 - x_opp)
	y_coordinate = randint(0, ysize * 2 - x_opp)

	# check if house can be placed
	check = matrix.check(x_opp, y_opp, grid, x_coordinate, y_coordinate)

	# place house
	if check == 0:
		# create and place house
		houses_e[house_e_counter] = House("Eengezinswoning", house_e_counter, 8, 8, 2, 285000, 3)
		house_e_counter = house_e_counter + 1

		matrix.place(x_opp, y_opp, grid, x_coordinate, y_coordinate, ("E{0:02}".format(houses_e[house_e_counter-1].id)))

	print("check + place:")
	print(grid)


	# house E01

	x_opp = 3
	y_opp = 3
	x_coordinate = 0
	y_coordinate = 0

	# check if house can be placed
	check = matrix.check(x_opp, y_opp, grid, x_coordinate, y_coordinate)

	# place house
	if check == 0:

		# create and place house
		houses_e[house_e_counter] = House("Eengezinswoning", house_e_counter, 8, 8, 2, 285000, 3)
		house_e_counter = house_e_counter + 1

		matrix.place(x_opp, y_opp, grid, x_coordinate, y_coordinate, ("E{0:02}".format(houses_e[house_e_counter-1].id)))

	print("check + place:")
	print(grid)

	matrix.export(grid)


if __name__ == "__main__":
	main()
