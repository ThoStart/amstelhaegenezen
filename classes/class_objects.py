import numpy as np
import library.setup as info

class House:
	def __init__(self, type, id, free, value, xcor, ycor, length, width):
		self.type = type
		self.id = id
		self.free = free
		self.value = value
		self.xcor = xcor
		self.ycor = ycor
		self.length = length
		self.width = width

class Water:
	def __init__(self, length, width):
		self.length = length
		self.width = width

class Matrix:
	def __init__(self, xsize, ysize):
		self.xsize = xsize
		self.ysize = ysize
		self.grid = np.full((self.xsize, self.ysize), fill_value='xxx', dtype=None)
		self.grid.fill('v')
		#return(grid)

	# finds empty coordinate
	def findemptyspot(self, xsize, ysize):
		for x in range(xsize):
			for y in range(ysize):
				if (self.grid[x, y] == 'v'):
					return x,y
		else:
			return 0

	# random kiezen welk huis meest waard is
	# def worth
	# dus eerste Eengezinswoning die is namelijk het meeste waard


	# checks if enough space around empty coordinate for house
	def check(self, x_opp, y_opp, free, x_coordinate, y_coordinate):
		# search for empty spaces
		for x in range((x_coordinate - free), (x_opp + x_coordinate + free)):
			for y in range((y_coordinate - free), (y_opp + y_coordinate + free)):
				if (x >= info.grid_length or y >= info.grid_width or x < 0 or y < 0 or self.grid[x, y] != 'v'):
					return 1

		# check if house isn't interfering with Bungalow
		for x in range((x_coordinate - info.house_b_free), (x_opp + x_coordinate + info.house_b_free)):
			for y in range((y_coordinate - info.house_b_free), (y_opp + y_coordinate + info.house_b_free)):
				if (x >= info.grid_length or y >= info.grid_width or x < 0 or y < 0 or 'B' in self.grid[x, y]):
					return 1

		# check if house isn't interfering with Maison
		for x in range((x_coordinate - info.house_m_free), (x_opp + x_coordinate + info.house_m_free)):
			for y in range((y_coordinate - info.house_m_free), (y_opp + y_coordinate + info.house_m_free)):
				if (x >= info.grid_length or y >= info.grid_width or x < 0 or y < 0 or 'M' in self.grid[x, y]):
					return 1
		return 0
	# a = np.where(matrix == 'v')
	# print(a)

	# puts a house on the empty space
	def place(self, x_opp, y_opp, x_coordinate, y_coordinate, name):
		for x in range(x_coordinate, x_opp+x_coordinate):
			for y in range(y_coordinate, y_opp+y_coordinate):
				self.grid[x, y] = name

		#return(grid)

	def export(self, grid):
		np.savetxt('grid.csv', grid, fmt='%s', delimiter=',')

	def free_space(self, grid, house, name, x_opp, y_opp):
		free = 1

		while(free > 0):
			#for x in set.union(set(range(house.xcor - free, house.xcor - free + 1)), set(range(house.xcor + x_opp + free - 1, house.xcor + x_opp + free))):
			for x in set.union(set(range(house.xcor - free, house.xcor)), set(range(house.xcor + x_opp, house.xcor + x_opp + free))):
			#for x in range((house.xcor - free), x_opp + free+ house.xcor):
				#for y in set.union(set(range(house.ycor - free, house.ycor - free + 1)), set(range(house.ycor + y_opp + free - 1, house.ycor + y_opp + free))):
				for y in set.union(set(range(house.ycor - free, house.ycor)), set(range(house.ycor + y_opp, house.ycor + y_opp + free))):
				#for y in range((house.ycor - free), y_opp + free + house.ycor):
					if (x >= info.grid_length or y >= info.grid_width or x < 0 or y < 0):
						house.free = free - 1
						# print(house.free)
						return free - 1
					elif (self.grid[x, y] != 'v' and self.grid[x, y] != name):
						house.free = free - 1
						# print(house.free)
						return free - 1

			free+=1

		return

	def score (self, house, scale, default_value, default_free, default_increment):
		free = (int((house.free - default_free) / scale) * default_increment)

		house.value = int(default_value * (free + 1))

		return house.value

	def swap(self, grid, house_a, house_b):
		# clear houses
		self.place(house_a.length, house_a.width, house_a.xcor, house_a.ycor, 'v')
		self.place(house_b.length, house_b.width, house_b.xcor, house_b.ycor, 'v')

		house_a_xcor_new = int(house_b.xcor + int(1/2 * house_b.length) - int(1/2 * house_a.length))
		house_a_ycor_new = int(house_b.ycor + int(1/2 * house_b.width) - int(1/2 * house_a.width))
		house_b_xcor_new = int(house_a.xcor + int(1/2 * house_a.length) - int(1/2 * house_b.length))
		house_b_ycor_new = int(house_a.ycor + int(1/2 * house_a.width) - int(1/2 * house_b.width))

		# check if houses can be swapped
		check_a = self.check(house_a.length, house_a.width, eval("info.house_" + str.lower(house_a.id[:1]) + "_free"), house_a_xcor_new, house_a_ycor_new)

		if house_b.id == 'v':
			check_b = self.check(house_b.length, house_b.width, eval("info.house_" + str.lower(house_a.id[:1]) + "_free"), house_b_xcor_new, house_b_ycor_new)
		else:
			check_b = self.check(house_b.length, house_b.width, eval("info.house_" + str.lower(house_b.id[:1]) + "_free"), house_b_xcor_new, house_b_ycor_new)
		# print("checks: {}, {}" .format(check_a, check_b))

		# if houses can be swapped, place houses on new location
		if (check_a == 0 and check_b == 0):
			# print("old: house_a.xcor, ycor: {}, {}" .format(house_a.xcor, house_a.ycor))
			self.place(house_a.length, house_a.width, house_a_xcor_new, house_a_ycor_new, house_a.id)
			self.place(house_b.length, house_b.width, house_b_xcor_new, house_b_ycor_new, house_b.id)

			# update dictionary
			house_a.xcor, house_a.ycor = house_a_xcor_new, house_a_ycor_new
			house_b.xcor, house_b.ycor = house_b_xcor_new, house_b_ycor_new
			# print("new: house_a.xcor, ycor: {}, {}" .format(house_a.xcor, house_a.ycor))

		# if houses cannot be swapped, place houses on original location
		else:
			self.place(house_a.length, house_a.width, house_a.xcor, house_a.ycor, house_a.id)
			self.place(house_b.length, house_b.width, house_b.xcor, house_b.ycor, house_b.id)
