# a python vector class
# A. Pletzer 5 Jan 00/11 April 2002
#
import math
import random
from functools import reduce

"""
A list based vector class that supports elementwise mathematical operations

In this version, the vector call inherits from list; this 
requires Python 2.2 or later.
"""


class vector(list):
    def __getslice__(self, i, j):
        try:
            # use the list __getslice__ method and convert
            # result to vector
            return vector(super(vector, self).__getslice__(i, j))
        except:
            raise TypeError('vector::FAILURE in __getslice__')

    def __add__(self, other):
        return vector(map(lambda x, y: x + y, self, other))

    def __neg__(self):
        return vector(map(lambda x: -x, self))

    def __sub__(self, other):
        return vector(map(lambda x, y: x - y, self, other))

    def __mul__(self, other):
        if type(other) == float:
            return vector(map(lambda x: x * other, self))
        return vector(map(lambda x, y: x * y, self, other))

    def __rmul__(self, other):
        return (self * other)

    def __truediv__(self, other):
        """
        Element by element division.
        """
        try:
            return vector(map(lambda x, y: x / y, self, other))
        except:
            return vector(map(lambda x: x / other, self))

    def __rdiv__(self, other):
        """
        The same as __div__
        """
        try:
            return vector(map(lambda x, y: x / y, other, self))
        except:
            # other is a const
            return vector(map(lambda x: other / x, self))

    def size(self):
        return len(self)

    def conjugate(self):
        return vector(map(lambda x: x.conjugate(), self))

    def ReIm(self):
        return [
            vector(map(lambda x: x.real, self)),
            vector(map(lambda x: x.imag, self)),
        ]

    def AbsArg(self):
        """
        Return modulus and phase parts
        """
        return [
            vector(map(lambda x: abs(x), self)),
            vector(map(lambda x: math.atan2(x.imag, x.real), self)),
        ]

    def out(self):
        """
        Prints out the vector.
        """
        print(self)


###############################################################################


def isVector(x):
    """
    Determines if the argument is a vector class object.
    """
    return hasattr(x, '__class__') and x.__class__ is vector


def zeros(n):
    """
    Returns a zero vector of length n.
    """
    return vector(map(lambda x: 0., range(n)))


def ones(n):
    """
    Returns a vector of length n with all ones.
    """
    return vector(map(lambda x: 1., range(n)))


def randvec(n, lmin=0.0, lmax=1.0, roundoff=0.0):
    """
    Returns a random vector of length n.
    """

    def _round(val, roundoff):
        if roundoff > 0:
            return val - (val % roundoff)
        else:
            return val

    return vector(map(lambda x: _round(random.uniform(lmin, lmax), roundoff),
                      range(n)))


def dot(a, b):
    return reduce(lambda x, y: x + y, a * b, 0.)


def cross(a, b):
    """
    cross product of two 3-vectors.
    """
    if len(a) == len(b) == 3:
        return vector([a[1] * b[2] - a[2] * b[1],
                       a[2] * b[0] - a[0] * b[2],
                       a[0] * b[1] - a[1] * b[0]])
    else:
        raise TypeError('vector.cross - args be 3-vectors')


def norm(a):
    try:
        return math.sqrt(abs(dot(a, a)))
    except:
        raise TypeError('vector::FAILURE in norm')


def sum(a):
    """
    Returns the sum of the elements of a.
    """
    try:
        return reduce(lambda x, y: x + y, a, 0)
    except:
        raise TypeError('vector::FAILURE in sum')


# elementwise operations

def log10(a):
    """
    log10 of each element of a.
    """
    try:
        return vector(map(math.log10, a))
    except:
        raise TypeError('vector::FAILURE in log10')


def log(a):
    """
    log of each element of a.
    """
    try:
        return vector(map(math.log, a))
    except:
        raise TypeError('vector::FAILURE in log')


def exp(a):
    """
    Elementwise exponential.
    """
    try:
        return vector(map(math.exp, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def sin(a):
    """
    Elementwise sine.
    """
    try:
        return vector(map(math.sin, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def tan(a):
    """
    Elementwise tangent.
    """
    try:
        return vector(map(math.tan, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def cos(a):
    """
    Elementwise cosine.
    """
    try:
        return vector(map(math.cos, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def asin(a):
    """
    Elementwise inverse sine.
    """
    try:
        return vector(map(math.asin, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def atan(a):
    """
    Elementwise inverse tangent.
    """
    try:
        return vector(map(math.atan, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def acos(a):
    """
    Elementwise inverse cosine.
    """
    try:
        return vector(map(math.acos, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def sqrt(a):
    """
    Elementwise sqrt.
    """
    try:
        return vector(map(math.sqrt, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def sinh(a):
    """
    Elementwise hyperbolic sine.
    """
    try:
        return vector(map(math.sinh, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def tanh(a):
    """
    Elementwise hyperbolic tangent.
    """
    try:
        return vector(map(math.tanh, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def cosh(a):
    """
    Elementwise hyperbolic cosine.
    """
    try:
        return vector(map(math.cosh, a))
    except:
        raise TypeError('vector::FAILURE in exp')


def pow(a, b):
    """
    Takes the elements of a and raises them to the b-th power
    """
    try:
        return vector(map(lambda x: x ** b, a))
    except:
        try:
            return vector(map(lambda x, y: x ** y, a, b))
        except:
            raise TypeError('vector::FAILURE in exp')


def atan2(a, b):
    """
    Arc tangent
    
    """
    try:
        return vector(map(math.atan2, a, b))
    except:
        raise TypeError('vector::FAILURE in exp')

###############################################################################
