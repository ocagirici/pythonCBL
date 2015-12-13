# Copyright Rick van der Meiden 2004

"""Basic toleranced comparison functions. Intended for use on double values,
   and extention to positive and negative infinity, represented by
   PosInf and NegInf respectively.
   Note that tol_eq(PosInf,PosInf)=True. This is matematically acceptable
   if we consider PosInf as a single value, greater than any other value that
   can be represented by a computer. Same for NegInf.
   All toleranced comparison function accept a tolerance value. When it is
   ommited or when "Default" is specified, a default value is used. This default
   value is stored in the variable: default_tol.
"""

class positiveinfinity:
    """Positive Infinity, a value greater then any other value except itself.
    Only one instance of this class is needed, instantiated in this module as
    PosInf."""
    def __cmp__(self, other):
        if other.__class__ == self.__class__:
            return 0
        else:
            return 1

    def __hash__(self):
        return 0

    def __repr__(self):
        return str(__name__)+".PosInf"

    def __str__(self):
        return "PosInf"
# end class positiveinfinity

class negativeinfinity:
    """Negative Infinity, a value greater then any other value except itself.
    Only one instance of this class is needed, instantiated in this module as
    NegInf."""
    def __cmp__(self, other):
        if other.__class__ == self.__class__:
            return 0
        else:
            return -1

    def __hash__(self):
            return 1

    def __repr__(self):
        return str(__name__)+".NegInf"

    def __str__(self):
        return "NegInf"
# end class positiveinfinity


#Positive infinity. This variable is an instance of positiveinfinity.
#No other instances need to be created.
PosInf = positiveinfinity()

#Negative infinity. This variable is an instance of negativeinfinity.
#No other instances need to be created.
NegInf = negativeinfinity()

# The default tolerance, used when no tolerance argument is given
# to the comparion functions, or when "Default" is passed.
default_tol = 1e-6

def tol_lt(a,b,tol="Default"):
    """Tolerant less-than: return b-a>tol"""
    if tol=="Default":
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
        return b-a>tol

def tol_gt(a,b,tol="Default"):
    if tol=="Default":
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
        return a-b>tol

def tol_eq(a,b,tol="Default"):
    if tol=="Default":
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
        return abs(a-b)<=tol

def tol_lte(a,b,tol="Default"):
    return not tol_gt(a,b,tol)

def tol_gte(a,b,tol="Default"):
    return not tol_lt(a,b,tol)


def tol_compare(a,b,tol="Default"):
    if tol_lt(a,b,tol):
        return "<"
    elif tol_eq(a,b,tol):
        return "="
    elif tol_gt(a,b,tol):
        return '>'
    

def tol_round(val,tol="Default"):
    if tol=="Default":
        tol = default_tol
    return val - (val % tol)

def test():
    tol = 0.005
    print("tolerance =", tol)
    values = [NegInf, -1.001, -1.0, -0.999, 0.0, 0.01, 0.02, PosInf]

    #print header
    head = ""
    for v in values:
        head += '\t'
        head += str(v)
    print(head)
    # rows rows
    for v1 in values:
        row = str(v1) + '\t'
        for v2 in values:
            row += tol_compare(v1,v2,tol) + '\t'
        print(row)

if __name__ == "__main__":
    test()


def cc_int(p1, r1, p2, r2):
    """
    Intersect circle (p1,r1) circle (p2,r2)
    where p1 and p2 are 2-vectors and r1 and r2 are scalars
    Returns a list of zero, one or two solution points.
    """
    d = vector.norm(p2-p1)
    if not tol_gt(d, 0):
        return []
    u = ((r1*r1 - r2*r2)/d + d)/2
    if tol_lt(r1*r1, u*u):
        return []
        elif r1*r1 < u*u:
            v = 0.0
        else:
            v = math.sqrt(r1*r1 - u*u)
    s = (p2-p1) * u / d
    if tol_eq(vector.norm(s),0):
            p3a = p1+vector.vector([p2[1]-p1[1],p1[0]-p2[0]])*r1/d
            if tol_eq(r1/d,0):
                    return [p3a]
                else:
                    p3b = p1+vector.vector([p1[1]-p2[1],p2[0]-p1[0]])*r1/d
                    return [p3a,p3b]
    else:
            p3a = p1 + s + vector.vector([s[1], -s[0]]) * v / vector.norm(s)
                if tol_eq(v / vector.norm(s),0):
                    return [p3a]
                else:
                    p3b = p1 + s + vector.vector([-s[1], s[0]]) * v / vector.norm(s)
                    return [p3a,p3b]

def sss_int(p1, r1, p2, r2, p3, r3):
    """Intersect three spheres, centered in p1, p2, p3 with radius r1,r2,r3 respectively.
       Returns a list of zero, one or two solution points.
    """
    solutions = []
    # plane though p1, p2, p3
    n = vector.cross(p2-p1, p3-p1)
    n = n / vector.norm(n)
    # intersect circles in plane
    cp1 = vector.vector([0.0,0.0])
    cp2 = vector.vector([vector.norm(p2-p1), 0.0])
    cpxs = cc_int(cp1, r1, cp2, r2)
    if len(cpxs) == 0:
        return []
    # px, rx, nx is circle
    px = p1 + (p2-p1) * cpxs[0][0] / vector.norm(p2-p1)
    rx = abs(cpxs[0][1])
    # plane of intersection cicle
    nx = p2-p1
    nx = nx / vector.norm(nx)
    # print "px,rx,nx:",px,rx,nx
    # py = project p3 on px,nx
    dy3 = vector.dot(p3-px, nx)
    py = p3 - (nx * dy3)
    if tol_gt(dy3, r3):
        return []
    ry = math.sin(math.acos(abs(dy3/r3)))*r3
    # print "py,ry:",py,ry
    cpx = vector.vector([0.0,0.0])
    cpy = vector.vector([vector.norm(py-px), 0.0])
    cp4s = cc_int(cpx, rx, cpy, ry)
    for cp4 in cp4s:
        p4 = px + (py-px) * cp4[0] / vector.norm(py-px) + n * cp4[1]
        solutions.append(p4)
    return solutions
