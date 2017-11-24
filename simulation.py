import main
import house_dictionary as hd
import importlib
import sys
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import timeit

start = timeit.default_timer()

# declare highest score
highest_score = 0

# get number of runs from command line argument
number_of_runs = int(sys.argv[1])

# open csv file, write at start
fd = open('score.csv','w')

data = []

# repeat number_of_runs times
i = 0
while i < number_of_runs:

    # run main file
    matrix, grid, total_score = main.main()

    if total_score != 1:

        data.append(total_score)

        # add total score to csv file
        fd.write(str(total_score) + ',')

        # save best grid
        if total_score > highest_score:
            matrix.export(grid)

        i+=1

    # reset dict files and values
    importlib.reload(hd)

# close csv file
fd.close()

stop = timeit.default_timer()

print("runtime: {}" .format(stop-start))

# generate normal distribution graph
mu, std = norm.fit(data)

plt.hist(data, bins=25, normed=True, alpha=0.6, color='g')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)

plt.show()
