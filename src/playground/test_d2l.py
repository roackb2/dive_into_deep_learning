import time
import numpy as np
import torch
from torch import nn
from d2l import torch as d2l

class B(d2l.HyperParameters):
  def __init__(self, a, b, c):
    self.save_hyperparameters(ignore=['c'])
    print('self.a =', self.a, 'self.b =', self.b)
    print('There is no self.c =', not hasattr(self, 'c'))

def test_progress_board():
  b = B(a=1, b=2, c=3)
  board = d2l.ProgressBoard('x')
  for x in np.arange(0, 10, 0.1):
    board.draw(x, np.sin(x), 'sin', every_n=2)
    board.draw(x, np.cos(x), 'cos', every_n=10)
