#!/usr/bin/env python3

from class_objects import House, Water
import matrix as matrix

def main():

	# declare house variables
	house_e_counter, house_b_counter, house_m_counter = 0, 0, 0
	houses_e, houses_b, houses_m = dict(), dict(), dict()

	# create a house E object
	houses_e[house_e_counter] = House("Eengezinswoning", house_e_counter, 8, 8, 2, 285000, 3)

	# print(houses_e[house_e_counter].id)
	# print("E{0:03}".format(houses_e[0].id))
	# print(houses_e[0].width)

	house_e_counter = house_e_counter + 1

	# create a house B object
	houses_b[house_b_counter] = House("Bungalow", house_b_counter, 10, 7.5, 3, 399000, 4)

	house_b_counter = house_b_counter + 1

	# create a house M object
	houses_m[house_m_counter] = House("Maison", house_m_counter, 11, 10.5, 6, 610000, 6)

	house_m_counter = house_m_counter + 1

	# generate grid
	grid = matrix.init(5,5)

	print(grid)

if __name__ == "__main__":
	main()
