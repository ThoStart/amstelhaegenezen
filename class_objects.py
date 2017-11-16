import numpy as np
import setup as info

class House:
    def __init__(self, type, id, free, value, xcor, ycor):
        self.type = type
        self.id = id
        self.free = free
        self.value = value
        self.xcor = xcor
        self.ycor = ycor

class Water:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Matrix:
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.grid = np.full((self.xsize, self.ysize), fill_value='xxxx', dtype=None)
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


    # checks if enough space around empty coordinate
    def check(self, x_opp, y_opp, free, x_coordinate, y_coordinate):
        # search for empty spaces
        for x in range((x_coordinate - free), (x_opp + x_coordinate + free)):
            for y in range((y_coordinate - free), (y_opp + y_coordinate + free)):
                if (self.grid[x, y] != 'v'):
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
            for x in range((house.xcor - free), x_opp + free+ house.xcor):
                for y in range((house.ycor - free), y_opp + free + house.ycor):
                    if (x >= info.grid_length or y >= info.grid_width or x < 0 or y < 0):
                        house.free = free - 1
                        return free - 1
                    elif (self.grid[x, y] != 'v' and self.grid[x, y] != name):
                        house.free = free - 1
                        return free - 1

            free+=1

        return

    def score (self, house, scale, default_value, default_free, default_increment):
        free = (int((house.free - default_free) / scale) * default_increment)

        house.value = int(default_value * (free + 1))

        return house.value
