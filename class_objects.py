import numpy as np

class House:
    def __init__(self, type, id, free, value):
        self.type = type
        self.id = id
        self.free = free
        self.value = value

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
        #a = x_coordinate
        #b = y_coordinate
        for x in range(x_coordinate, x_opp+x_coordinate):
            for y in range(y_coordinate, y_opp+y_coordinate):
                self.grid[x, y] = name

        #return(grid)

    def export(self, grid):
        np.savetxt('grid.csv', grid, fmt='%s', delimiter=',')


