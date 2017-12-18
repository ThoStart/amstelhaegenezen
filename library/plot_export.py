import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# use matplotlib to visualize normal distribution graph
def normal(data, score):

    mu, std = norm.fit(data)

    plt.hist(data, bins=25, weights=np.ones_like(data)/len(data), alpha=0.6, color='g')

    # plot normal distirbution stack overflow(https://stackoverflow.com/questions/20011122/fitting-a-normal-distribution-to-1d-data)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f,\n max score = %i, n = %i" % (mu, std, score, len(data))
    plt.title(title)

    plt.savefig("export/normal.png")

    plt.show()

    return(0)

# use matplotlib to visualize line graph
def line(data, chosen_algorithm):

    xaxis_array = []

    for i in range(len(data)):
        xaxis_array.append(i)

    plt.plot(xaxis_array, data, 'r--')
    plt.axis([0, len(data), min(data) - 500000, max(data) + 500000])

    if chosen_algorithm == 2 or chosen_algorithm == 5:
        title = "Hill climbing"
    else:
        title = "Simulated annealing"

    plt.title(title)

    if chosen_algorithm == 2 or chosen_algorithm == 5:
        plt.savefig("export/hill_climbing.png")
    else:
        plt.savefig("export/simulated_annealing.png")

    plt.show()

    return(0)
