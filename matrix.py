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
    matrix[0,1] = 'B01'

    print(matrix[0,1])

    return(matrix)

# functie: check zijn welk huis past
def search():
    # search for B01
    a = np.where(matrix == 'B01')
    print(a)


# # functie: beste huis pakken
# def choice():
#
# # place houses random
# def random_place():
#
#     # functie: huis plaatsen
# def fill(matrix)
#     #matrix.nparray(..., ...) = (...,...)
