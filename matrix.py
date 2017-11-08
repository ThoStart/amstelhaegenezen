import numpy as np

# initialize matrix of 180x160 meters
def init(x, y):
    # put x and y size to half meters
    x = x * 2
    y = y * 2
    matrix = np.empty([x, y], dtype=str)
    matrix.fill('v')
    # print(matrix)
    return(matrix)

# max_maison = 3, max_bungalow = 5, max_eengezinswoning = 12

# # functie: check zijn welk huis past
# def check():
#     # check multiple fields at once
#
# # functie: beste huis pakken
# def choice():
#
# # place houses random
# def random_place():
#
#     # functie: huis plaatsen
# def fill(matrix)
#     #matrix.nparray(..., ...) = (...,...)
