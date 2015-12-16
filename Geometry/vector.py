import math


class Vector:
    i = 0
    j = 0
    k = 0
    len = 0

    def __init__(self, other):
        if type(other) == list:
            if len(other) == 2:
                self.i = other[0]
                self.j = other[1]
                self.len = 2
            if len(other) == 3:
                self.i = other[0]
                self.j = other[1]
                self.k = other[2]
                self.len = 3
        else:
            if len(other) == 2:
                self.i = other.i
                self.j = other.j
                self.len = 2
            if len(other) == 3:
                self.i = other.i
                self.j = other.j
                self.k = other.k
                self.len = 3

    def __add__(self, other):
        if type(other) in [int, float]:
            return Vector([self.i + other, self.j +other, self.k + other])
        return Vector([self.i + other.i, self.j + other.j, self.k + other.k])

    def __sub__(self, other):
        if type(other) in [int, float]:
            return Vector([self.i - other, self.j - other, self.k - other])
        return Vector([self.i - other.i, self.j - other.j, self.k - other.k])

    def __mul__(self, other):
        if type(other) in [int, float]:
            return self.i * other + self.j * other + self.k * other
        return self.i * other.i + self.j * other.j + self.k * other.k

    def __truediv__(self, other):
        if type(other) in [int, float]:
            return Vector([self.i/other, self.j/other, self.k/other])
        return Vector([self.i/other.i, self.j/other.j, self.k/other.k])

    def __abs__(self):
        return math.sqrt(self.i ** 2 + self.j ** 2 + self.k ** 2)

    def __xor__(self, other):  # cross product
        return Vector([self.j * other.k - self.k * other.k,
                       self.k * other.i - self.i * other.k,
                       self.i * other.j - self.j * other.i])

    def __eq__(self, other):
        self.i, self.j, self.k = [other.i, other.j, other.k]

    def __pow__(self, power, modulo=None):
        return

    def __repr__(self):
        st = '(' + str(self.i) + ', ' + str(self.j) + ', ' + str(self.k) + ')'
        return st

    def __len__(self):
        return self.len

    __rmul__ = __mul__
