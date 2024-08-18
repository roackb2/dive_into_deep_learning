class Vector:
  def __init__(self, val):
    self.__name__ = 'Vector'
    assert isinstance(val, list), 'Error initializing Vector: value must be a list'
    self.val = val
    self.__dyda = None
    self.__dydb = None

  @property
  def size(self):
    return len(self.val)

  def clone(self):
    c = [None] * self.size
    for i in range(0, self.size):
      c[i] = self[i]
    return Vector(c)

  def sum(self):
    sum = 0
    for e in self.val:
      sum += e
    return sum

  def mean(self):
    return self.sum() / self.size

  @staticmethod
  def arange(n):
    Vector.__check_is_num(n)
    c = [None] * n
    for i in range(0, n):
      c[i] = i
    return c

  @staticmethod
  def ones_like(n):
    Vector.__check_is_num(n)
    c = [1] * n
    return Vector(c)

  @staticmethod
  def zeros_like(n):
    Vector.__check_is_num(n)
    c = [0] * n
    return Vector(c)

  @staticmethod
  def __check_is_num(n):
    assert Vector.__is_num(n), f"{n} is not a number"

  def __check_size(self, other):
    if Vector.__is_num(other):
      return
    assert self.size == other.size, f"Vector of size {self.size} is not addable to the other one of size {other.size}"

  @staticmethod
  def __is_num(x):
    return isinstance(x, (int, float, complex)) and not isinstance(x, bool)

  @staticmethod
  def __wrap_other(other):
    return other if Vector.__is_num(other) else other.clone()

  def __empty(self):
    return [None] * self.size

  def __bop(self, other, op):
    self.__check_size(other)
    c = self.__empty()
    for i in range(0, self.size):
      if Vector.__is_num(other):
        c[i] = op(self[i], other)
      else:
        c[i] = op(self[i], other[i])
    return Vector(c)

  def __getitem__(self, i):
    return self.val[i]

  def __setitem__(self, i, v):
    self.val[i] = v

  def __delitem__(self, i):
    self.val[i] = None

  def __add__(self, other):
    c = self.__bop(other, lambda x, y: x + y)
    c.__dyda = Vector.ones_like(c.size)
    c.__dydb = Vector.ones_like(c.size)
    return c

  def __sub__(self, other):
    c = self.__bop(other, lambda x, y: x - y)
    c.__dyda = Vector.ones_like(self.size)
    c.__dydb = Vector.ones_like(self.size) * (-1)
    return c

  def __mul__(self, other):
    c = self.__bop(other, lambda x, y: x * y)
    c.__dyda = Vector.__wrap_other(other)
    c.__dydb = self.clone()
    return c

  def __pow__(self, other):
    return self.__bop(other, lambda x, y: x ** y)

  def __truediv__(self, other):
    c = self.__bop(other, lambda x, y: x / y)
    o = Vector.__wrap_other(other)
    c.__dyda = o ** -1
    c.__dydb = self * (o ** -2)
    return c

  @property
  def grad(self):
    return self.__dyda, self.__dydb

  def __str__(self):
    return f"Vector({self.val})"

  def print(self):
    print(f"{self.__name__}, value: {str(self)}")
