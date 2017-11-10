import numpy as np

# initialize matrix of 180x160 meters
def init(x, y):
    # put x and y size to half meters
    x = x * 2
    y = y * 2

    # create matrix fill_value determines the amount of chars saved in array
    matrix = np.full((x, y), fill_value='xxxx', dtype=None)
    # matrix = np.array([a, b],dtype='S')
    matrix.fill('v')

    # put 0,1 to "B01"
    # matrix[2,2] = 'B01'

    # print(matrix[0,1])

    return(matrix)

# # functie: beste huis pakken
# def choice():
#

# functie: check of gekozen huis past
def check(x_opp, y_opp, grid, x_coordinate, y_coordinate):

    # search for empty spaces
    for x_coordinate in range(x_opp):
        for y_coordinate in range(y_opp):
            if (grid[x_coordinate, y_coordinate] != 'v'):
                print(x_coordinate ,",", y_coordinate)
                return 1;
    return 0;
        # a = np.where(matrix == 'v')
            # print(a)

def place(x_opp, y_opp, grid, x_coordinate, y_coordinate):
    for x_coordinate in range(x_opp):
        for y_coordinate in range(y_opp):
            grid[x_coordinate, y_coordinate] = 'B01'

    return(grid)
