import main
import house_dictionary as hd
import importlib
import sys
import tk_export
import numpy as np
import timeit

# start runtime
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
            highest_score = total_score

        i+=1

    # reset dict files and values
    importlib.reload(hd)

# close csv file
fd.close()

# stop and show runtime
stop = timeit.default_timer()
print("runtime: {}" .format(stop-start))

# use tkinter to visualize grid
tk_export.create(matrix,grid, total_score)

# use matplotlib to visualize normal distribution graph
import plot_export
plot_export.create(data, total_score)
