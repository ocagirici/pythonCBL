class PositiveInfinity:

    def __cmp__(self, other):
        if other.__class__ == self.__class__:
            return 0
        else:
            return 1

    def __hash__(self):
        return 0

    def __repr__(self):
        return str(__name__) + ".PosInf"

    def __str__(self):
        return "PosInf"


class NegativeInfinity:

    def __cmp__(self, other):
        if other.__class__ == self.__class__:
            return 0
        else:
            return -1

    def __hash__(self):
        return 1

    def __repr__(self):
        return str(__name__) + ".NegInf"

    def __str__(self):
        return "NegInf"

PosInf = PositiveInfinity()

NegInf = NegativeInfinity()

default_tol = 1e-6


def tol_lt(a, b, tol="Default"):
    if tol == "Default":
        tol = default_tol
    if a == NegInf:
        return b != NegInf
    elif a == PosInf:
        return False
    elif b == PosInf:
        return a != PosInf
    elif b == NegInf:
        return False
    else:
        return b - a > tol


def tol_gt(a, b, tol="Default"):
    if tol == "Default":
        tol = default_tol
    if a == NegInf:
        return False
    elif a == PosInf:
        return b != PosInf
    elif b == NegInf:
        return a != NegInf
    elif b == PosInf:
        return False
    else:
        return a - b > tol


def tol_eq(a, b, tol="Default"):
    if tol == "Default":
        tol = default_tol
    if a == PosInf:
        return b == PosInf
    elif a == NegInf:
        return b == NegInf
    elif b == PosInf:
        return a == PosInf
    elif b == NegInf:
        return a == NegInf
    else:
        return abs(a - b) <= tol


def tol_lte(a, b, tol="Default"):
    return not tol_gt(a, b, tol)


def tol_gte(a, b, tol="Default"):
    return not tol_lt(a, b, tol)


def tol_compare(a, b, tol="Default"):
    if tol_lt(a, b, tol):
        return "<"
    elif tol_eq(a, b, tol):
        return "="
    elif tol_gt(a, b, tol):
        return ">"


def tol_round(val, tol="Default"):
    if tol == "Default":
        tol = default_tol
    return val - (val % tol)
