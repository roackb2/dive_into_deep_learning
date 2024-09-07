import time
import numpy as np
import torch
from torch import nn
from d2l import torch as d2l

class Module(nn.Module, d2l.HyperParameters):
  def __init__(self, plot_train_per_epoch=2, plot_valid_per_epoch=1):
    super().__init__()
    self.save_hyperparameters()
    self.board = d2l.ProgressBoard()

  def loss(self, y_hat, y):
    print('Not implemented')

  def forward(self, X):
    assert hasattr(self, 'net')
    return self.net(X)

  def plot(self, key, value, train):
    assert hasattr(self, 'trainer')
    self.board.xlabel = 'epoch'
    if train:
      x = self.trainer.train_batch_idx / self.trainer.num_train_batches
      n = self.trainer.num_train_batches / self.plot_train_per_epoch
    else:
      x = self.trainer.epoch + 1
      n = self.trainer.num_val_batches / self.plot_valid_per_epoch
    self.board.draw(x, value.to(
      d2l.cpu().detach().numpy(), ('train_' if train else 'val_') + key, every_n=int(n)
    ))

  def training_step(self, batch):
    l = self.loss(self(*batch[:-1]), batch[-1])
    self.plot('loss', l, train=True)
    return l

  def validation_step(self, batch):
    l = self.loss(self(*batch[:-1]), batch[-1])
    self.plot('loss', l, train=False)

  def configure_optimizers(self):
    print('Not implemented')
