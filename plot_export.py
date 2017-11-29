import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# use matplotlib to visualize normal distribution graph
def create(data, score):

    mu, std = norm.fit(data)

    plt.hist(data, bins=25, normed=True, alpha=0.6, color='g')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f, max score = %i" % (mu, std, score)
    plt.title(title)

    plt.show()

    return(0)
