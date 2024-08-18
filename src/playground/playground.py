import traceback
from playground.data_manipulation import inspect_house_data, inspect_abalone_data

def run():
  try:
    inspect_house_data()
    inspect_abalone_data()
  except Exception as e:
    print(f"Error while running playground: {e}")
    traceback.print_exc()
