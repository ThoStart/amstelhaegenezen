import numpy as np

# initialize matrix of 180x160 meters
def init(x, y):
    # put x and y size to half meters
    x = x * 2
    y = y * 2
    matrix = np.empty([x, y], dtype=int)
    return(matrix)
