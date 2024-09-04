import math
import numpy as np
import matplotlib.pyplot as plt

def norm(x, mu, sigma):
  p = 1 / math.sqrt(2 * math.pi * sigma ** 2)
  p *= np.exp(-(x - mu) ** 2 / (2 * sigma **2))
  return p

def visualize_norm():
  params = [(0, 1), (0, 3), (3, 1)]
  x = np.arange(-7, 7, 0.01)
  fig, ax = plt.subplots()
  legends = []
  for (mu, sigma) in params:
    ax.scatter(x, norm(x, mu, sigma))
    legends.append(f'mu: {mu}, sigma: {sigma}')
  ax.set_xlabel('x')
  ax.set_ylabel('p(x)')
  ax.legend(legends)
  plt.show()
