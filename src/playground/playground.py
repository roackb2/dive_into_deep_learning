
def scratch_pad():
  print(f"scratch pad")
  pass

def run():
  try:
    scratch_pad()
  except Exception as e:
    print(f"Error while running playground: {e}")
