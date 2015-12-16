import math
import numpy as np


class Vector:
    i = 0
    j = 0
    k = 0

    def __init__(self, v):
        if len(v) == 2:
            self.i, self.j = v
        if len(v) == 3:
            self.i, self.j, self.k = v

    def __add__(self, other):
        return Vector([self.i + other.i, self.j + other.j, self.k + other.k])

    def __sub__(self, other):
        return Vector([self.i - other.i, self.j - other.j, self.k - other.k])

    def __mul__(self, other):
        if type(other) == int:
            return Vector([self.i * other, self.j * other, self.k * other])
        return Vector([self.i * other.i + self.j * other.j + self.k + other.k])

    def __abs__(self):
        return math.sqrt(self.i ** 2 + self.j ** 2)

    def __xor__(self, other):  # cross product
        return Vector([self.j * other.k - self.k * other.k,
                       self.k * other.i - self.i * other.k,
                       self.i * other.j - self.j * other.i])
