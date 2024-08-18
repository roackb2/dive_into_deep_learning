import traceback
from playground.data_manipulation import inspect_house_data, inspect_abalone_data
from playground.custom_implementation.my_tensor import inspect_vectors

def run():
  try:
    inspect_house_data()
    inspect_abalone_data()
    inspect_vectors()
  except Exception as e:
    print(f"Error while running playground: {e}")
    traceback.print_exc()
