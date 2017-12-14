import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# use matplotlib to visualize normal distribution graph
def normal(data, score):

    mu, std = norm.fit(data)

    plt.hist(data, bins=25, weights=np.ones_like(data)/len(data), alpha=0.6, color='g')
    #plt.hist(data, bins=25, normed=True, alpha=0.6, color='g')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f,\n max score = %i, n = %i" % (mu, std, score, len(data))
    plt.title(title)

    #plt.figure(figsize=(20,10))


    plt.savefig("export/normal.png")

    plt.show()

    return(0)

# use matplotlib to visualize line graph
def line(data):

    xaxis_array = []

    for i in range(len(data)):
        xaxis_array.append(i)

    plt.plot(xaxis_array, data, 'r--')
    plt.axis([0, len(data), min(data) - 500000, max(data) + 500000])

    title = "Hill climbing"

    plt.title(title)

    plt.savefig("export/hill_climbing.png")

    plt.show()

    return(0)
