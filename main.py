#!/usr/bin/env python3

from class_objects import House, Water
import matrix as matrix

house_e = House("Eengezinswoning", 8, 8, 2, 285000, 3)
house_b = House("Bungalow", 10, 7.5, 3, 399000, 4)
house_m = House("Maison", 11, 10.5, 6, 610000, 6)

def main():

	grid = matrix.init(5,5)

	print(grid)

if __name__ == "__main__":
	main()
