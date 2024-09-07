import traceback
from playground.data_manipulation import inspect_house_data, inspect_abalone_data
from playground.custom_implementation.my_tensor import inspect_vectors
from playground.norm import visualize_norm
from playground.test_d2l import test_progress_board, test_hyper_parameter, test_custom_module

def run():
  try:
    inspect_house_data()
    inspect_abalone_data()
    inspect_vectors()
    # visualize_norm()
    # test_progress_board()
    test_hyper_parameter()
    test_custom_module()
  except Exception as e:
    print(f"Error while running playground: {e}")
    traceback.print_exc()
