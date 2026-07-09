import math

class SciCal:
  def __init__(self, num):
    self.num = num
  def square_root(self):
    return math.sqrt(self.num)
  def cube_root(self):
    return math.cbrt(self.num)
  def square(self):
    return self.num**2
  def cube(self):
    return self.num**3
  def factorial(self):
    return math.factorial(self.num)
  def cosine(self):
    return math.cos(math.radians(self.num))
  def sine(self):
    return math.sin(math.radians(self.num))
  def tangent(self):
    return math.tan(math.radians(self.num))
