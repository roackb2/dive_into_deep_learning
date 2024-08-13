import os
import pandas as pd
import torch
from definitions import DATA_DIR, ROOT_PATH
from lib.utils import nextl

HOUSE_DATA_PATH = os.path.join(DATA_DIR, 'house_tiny.csv')

def write_house_data():
  print(f"Writing house values to {HOUSE_DATA_PATH}\n")
  with open(HOUSE_DATA_PATH, 'w') as file:
    file.write('''NumRooms,RoofType,Price
NA,NA,127500
2,NA,106000
4,Slate,178100
NA,NA,140000
''')

def read_house_data():
  print("Reading house data using pandas")
  data = pd.read_csv(HOUSE_DATA_PATH)
  print(f"Data read:\n{data}\n")
  inputs, targets = data.iloc[:,0:2], data.iloc[:,2]
  return inputs, targets

def clean_house_inputs(inputs):
  inputs = pd.get_dummies(inputs, dummy_na=True)
  print(f"Input mean:\n{inputs.mean()}\n")
  inputs = inputs.fillna(inputs.mean())
  return inputs

def to_tensors(inputs, targets):
  X = torch.tensor(inputs.to_numpy(dtype=float))
  Y = torch.tensor(targets.to_numpy(dtype=float))
  return X, Y

def scratch_pad():
  print(f"running scratch pad")
  write_house_data()
  inputs, targets = read_house_data()
  inputs = clean_house_inputs(inputs)
  print(f"Cleaned inputs:\n{inputs}\n")
  print(f"Targets:\n{targets}\n")
  X, Y = to_tensors(inputs, targets)
  print(f"X, Y as pytorch tensors:\n{X}\n{Y}\n")

def run():
  try:
    scratch_pad()
  except Exception as e:
    print(f"Error while running playground: {e}")
