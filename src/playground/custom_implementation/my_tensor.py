from lib.math.vector import Vector
from lib.utils import nextl

def inspect_vectors():
  try:
    # Trying to initialize a vector with string should throw error
    vector = Vector("hello")
    vector.print()
  except Exception as e:
    print(e)
  val = [1,2,3,5,7]
  vector = Vector(val)
  sum = vector.sum()
  mean = vector.mean()
  print(f"Sum of the vector initialized with {val}: {vector.sum()}")
  print(f"Mean of vector initialized with {val}: {vector.mean()}")
  v1 = Vector([1,3,4,5])
  v2 = Vector([1,2,3])
  try:
    print(f"Adding two vectors {v1} and {v2}")
    print(v1 + v2)
  except Exception as e:
    print(e)
  v2 = Vector([2,4,5,9])
  print(f"v2: {v2}")
  print(f"Setting v2[2] to 99: {v2}")
  v2[2] = 99
  print(f"Delete v[2]: {v2}")
  del v2[2]
  print(f"v2: {v2}")
  v2[2] = 12
  print(v1, v2)
  a = v1 + v2
  dyda, dydb = a.grad
  print(f"v1 + v2: {a}, gradients: {dyda}, {dydb}")
  a = v1 - v2
  dyda, dydb = a.grad
  print(f"v1 - v2: {a}, gradients: {dyda}, {dydb}")
  a = v1 * v2
  dyda, dydb = a.grad
  print(f"v1 * v2: {a}, gradients: {dyda}, {dydb}")
  a = v1 / v2
  dyda, dydb = a.grad
  print(f"v1 / v2: {a}, gradients: {dyda}, {dydb}")
  print("Broadcast operations")
  print(f"v1 + 5: {v1 + 5}")
  print(f"v1 - 5: {v1 - 5}")
  print(f"v1 * 5: {v1 * 5}")
  print(f"v1 / 5: {v1 / 5}")
  print(f"v1 ** 2: {v1 ** 2}")
  a = Vector.arange(5)
  print(f"Vector.arange(5): {a}")
  a = Vector.ones_like(5)
  print(f"Vector.ones_like(5): {a}")
  a = Vector.zeros_like(5)
  print(f"Vector.zeros_like(5): {a}")
  print(f"Clone vectors")
  b = a.clone()
  print(a, b)
  print(f"id(a): {id(a)}, id(b): {id(b)}, id(a) == id(b): {id(a) == id(b)}")
  nextl()
