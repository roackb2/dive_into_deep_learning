import os
from definitions import DATA_DIR

def write_csv():
  house_dir_path = os.path.join(DATA_DIR, 'house_tiny.csv')
  print(f"Writing house values to {house_dir_path}")
  with open(house_dir_path, 'w') as file:
    file.write('''NumRooms,RoofType,Price
NA,NA,127500
2,NA,106000
4,Slate,178100
NA,NA,140000
''')

def scratch_pad():
  print(f"running scratch pad")
  write_csv()

def run():
  try:
    scratch_pad()
  except Exception as e:
    print(f"Error while running playground: {e}")
