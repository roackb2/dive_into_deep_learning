import d2l

class HyperParameters:
  def save_hyperparameters(self, ignore=[]):
    print("Not implemented")

class ProgressBoard(d2l.HyperParameters):
  def __init__(self,
    xlabel=None, ylabel=None,
    xlim=None, ylim=None,
    xscale='linear', yscale='linear',
    ls=['-', '--', '-', ':'], colors=['C0', 'C1', 'C2', 'C3'],
    fig=None, axes=None, figsize=(3.5, 2.5), display=True
  ):
    self.save_hyperparameters()

  def draw(self, x, y, label, every_n=1):
    print('Not implemented')

