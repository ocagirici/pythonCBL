import numpy as np


class Matrix:
    m = np.matrix()

    def __init__(self, m):
        self.m = np.matrix(m)

    def transpose(self):
        return np.transpose(self.m)

    def __mul__(self, other):
        return np.transpose(self.m, other.m)

    def __add__(self, other):
        return np.add(self.m, other.m)
