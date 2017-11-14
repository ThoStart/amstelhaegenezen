import numpy as np

# initialize matrix of 180x160 meters
def init(xsize, ysize):
    # put x and y size to half meters
    x = xsize
    y = ysize

    # create matrix fill_value determines the amount of chars saved in array
    matrix = np.full((x, y), fill_value='xxxx', dtype=None)
    # matrix = np.array([a, b],dtype='S')
    matrix.fill('v')

    # put 0,1 to "B01"
    # matrix[0,0] = 'B01'

    return(matrix)

# finds empty coordinate
def findemptyspot(xsize, ysize, grid):
    for x in range(xsize):
        for y in range(ysize):
            if (grid[x, y] == 'v'):
                return x,y;
    else:
        return 0;

# random kiezen welk huis meest waard is
#def worth
# dus eerste Eengezinswoning die is namelijk het meeste waard


# checks if enough space around empty coordinate
def check(x_opp, y_opp, grid, x_coordinate, y_coordinate):
    # search for empty spaces
    for x in range(x_coordinate, x_opp+x_coordinate):
        for y in range(y_coordinate, y_opp+y_coordinate):
            if (grid[x, y] != 'v'):
                return 1;
    return 0;
        # a = np.where(matrix == 'v')
            # print(a)

# puts a house on the empty space
def place(x_opp, y_opp, grid, x_coordinate, y_coordinate, name):
    #a = x_coordinate
    #b = y_coordinate
    for x in range(x_coordinate, x_opp+x_coordinate):
        for y in range(y_coordinate, y_opp+y_coordinate):
            grid[x, y] = name

    return(grid)

def export(grid):
    np.savetxt('grid.csv', grid, fmt='%s', delimiter=',')

