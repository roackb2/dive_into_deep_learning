import os
import time
import pandas as pd
from enum import Enum
from definitions import DATA_DIR

ABALONE_DATA_PATH = os.path.join(DATA_DIR, 'abalone', 'abalone.data')
COL_NAMES = [
    'Sex', 'Length', 'Diameter', 'Height', 'Whole Weight',
    'Shucked Weight', 'Viscera Weight', 'Shell Weight', 'Rings'
  ]

def read_abalone_data():
  start = time.perf_counter()
  data = pd.read_csv(ABALONE_DATA_PATH, names=COL_NAMES)
  end = time.perf_counter()
  print(f"Time elapsed reading data set: {(end - start) * 10e3:.2f}ms")
  print(f"Inspect first few rows of the Abalone data set:\n{data.head()}\n")
  inputs, targets = data.iloc[:,0:len(COL_NAMES)-1], data['Rings']
  print(f"inputs shape: {inputs.shape}, targets shape: {targets.shape}")
  print(f"input and target types: {type(inputs), type(targets)}\n")
  print(f"inputs:\n{inputs.head()}\n")
  print(f"targets:\n{targets[:5]}\n")
  return inputs, targets

def inspect_abalone_data():
  print('inspecting Abalone data set')
  inputs, targets = read_abalone_data()

