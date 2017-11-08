#!/usr/bin/env python3

from class_objects import House, Ground, Water
import matrix as matrix

house_e = House("Eengezinswoning", 16, 16, 4, 285000, 3)
house_b = House("Bungalow", 20, 15, 6, 399000, 4)
house_m = House("Maison", 22, 21, 12, 610000, 6)

ground = Ground()

def main():
	grid = matrix.init(5,5)
	print(grid)

if __name__ == "__main__":
	main()
