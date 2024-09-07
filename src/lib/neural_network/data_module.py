import time
import numpy as np
import torch
from torch import nn
from d2l import torch as d2l
from definitions import DATA_DIR

class DataModule(d2l.HyperParameters):
  def __init__(self, root=DATA_DIR, num_workers=4):
    self.save_hyperparameters()

  def get_dataloader(self, train):
    print('Not implemented')

  def train_dataloader(self):
    return self.get_dataloader(train=True)

  def val_dataloader(self):
    return self.get_dataloader(train=False)
