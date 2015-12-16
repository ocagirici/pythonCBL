import math
import sympy
from vector import Vector as vector

import Geometry.vector as point


def quarilaterate(u, v, w, r1, r2, r3):
    P1 = vector(u)
    P2 = vector(v)
    P3 = vector(w)
    ex = (P2 - P1) / abs(P2 - P1)
    i = ex * (P3 - P1)
    ey = (P3 - P1 - i * ex) / abs(P3 - P1 - i * ex)
    d = abs(P2 - P1)
    j = ey * (P3 - P1)
    x = (r1 ** 2 - r2 ** 2 + d ** 2)/(2 * d)
    y = (r1 ** 2 - r3 ** 2 - x ** 2 + (i + x) ** 2 + j ** 2) / 2 * j
    ez = ex ^ ey
    z1 = math.sqrt(r1 ** 2 - x ** 2 - y ** 2)
    z2 = -z1
    p1 = P1 + x * ex + y * ey + z1 * ez
    p2 = P1 + x * ex + y * ey + z2 * ez
    return [p1, p2]


def trilaterate(u, v, r1, r2):
    P1 = vector(u)
    P2 = vector(v)
    ex = (P2 - P1) / abs(P2 - P1)
    d = abs(P2 - P1)
    x = (r1 ** 2 - r2 ** 2 + d ** 2)/(2 * d)
    y1 = math.sqrt(r1 ** 2 - x ** 2)
    y2 = -y1
    p1 = P1 + x * ex + y1 * ey
    p2 = P1 + x * ex + y2 * ey
    return [p1, p2]


def coplanar(points):
    i = sympy.Point3D(points[0][0], points[0][1], points[0][2])
    j = sympy.Point3D(points[1][0], points[1][1], points[1][2])
    k = sympy.Point3D(points[2][0], points[2][1], points[2][2])
    l = sympy.Point3D(points[3][0], points[3][1], points[3][2])
    return sympy.Point3D.are_coplanar(i, j, k, l)


def collinear(*points):
    i = sympy.Point(points[0])
    j = sympy.Point(points[1])
    k = sympy.Point(points[2])
    return sympy.Point.is_collinear(i, j, k)


def dist3d(i, j):
    return math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2)


def dist2d(i, j):
    return math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2)


class WSN:
    V = 0
    E = 0
    R = 10.0
    adj = []
    is_adj = []
    localized_neighbors_3d = {}
    localized_neighbors_2d = {}
    sensors = []
    localized = []
    unlocalized = []
    global_pos = []
    local_pos = []

    def clear_localization(self):
        self.localized_neighbors_3d = {}
        self.localized_neighbors_2d = {}
        self.global_pos = [[] for i in range(self.V)]
        self.local_pos = [[] for i in range(self.V)]

    def __init__(self, sensors):
        self.sensors = sensors
        self.V = len(sensors)
        self.clear_localization()
        self.adj = [[] for i in range(self.V)]
        self.is_adj = [[False for i in range(self.V)] for j in range(self.V)]

        for i in range(self.V):
            self.unlocalized.append(i)
            for j in range(i + 1, self.V):
                distance = self.actual_distance(i, j)
                if distance <= self.R:
                    self.add_adj(i, j, distance)

    def add_adj(self, i, j, dist):
        self.adj[i].append((j, dist))
        self.adj[j].append((i, dist))
        self.is_adj[i][j] = True
        self.is_adj[j][i] = True

    def actual_distance(self, i, j):
        return dist3d(self.sensors[i], self.sensors[j])

    def neighbor_localized_3d(self, node):
        for neighbor in self.adj[node]:
            self.localized_neighbors_3d[neighbor].append(node)

    def neighbor_localized_2d(self, node):
        for neighbor in self.adj[node]:
            self.localized_neighbors_2d[neighbor].append(node)

    def __repr__(self):
        st = ''
        for v in range(self.V):
            st += str(v)
            st += ': '
            for w in self.adj[v]:
                st += "({0} ,{1:.2f}), ".format(w[0], w[1])
            st = st[:-2]
            st += '\n'
        # for i in range(self.V):
        #     for j in range(self.V):
        #         st += self.is_adj[i][j]
        #     st += '\n'

        return st

    def localize3d(self, node, localized):
        p = []
        r = []
        for i in range(4):
            p.append(self.global_pos[localized[i]])
            r.append(self.adj[i][localized[i]][1])
        if coplanar(p):
            return False
        sol = sss_int(p[:-1], r[:-1])
        if len(sol) == 0:
            return False
        if len(sol) == 1:
            self.global_pos[node] = sol[0]
        else:
            p1 = abs(point.norm(point.vector(sol[0]) - point.vector(p[3])) - r[3]) <= r[3] * 0.05
            p2 = abs(point.norm(point.vector(sol[1]) - point.vector(p[3])) - r[3]) <= r[3] * 0.05
            if p1 and p2:
                return False
            if p1:
                self.global_pos[node] = sol[0]
            if p2:
                self.global_pos[node] = sol[1]

            return True

    def localize2d(self, node, localized):
        p = []
        r = []
        for i in range(4):
            p.append(self.global_pos[localized[i]])
            r.append(dist2d(node, localized[i]))

        if collinear(p):
            return False
        sol = cc_int(p[:-1], r[:-1])
        if len(sol) == 0:
            return False
        if len(sol) == 1:
            node.set_local(sol[0])
        else:
            p1 = abs(point.norm(point.vector(sol[0]) - point.vector(p[2])) - r[3]) <= r * 0.05
            p2 = abs(point.norm(point.vector(sol[1]) - point.vector(p[2])) - r[3]) <= r * 0.05
            if p1 and p2:
                return False
            if p1:
                self.local_pos[node] = sol[0]
            if p2:
                self.local_pos[node] = sol[1]
            return True

    def quadrilateration(self):
        print('quad')
        F_best = []
        for a in range(self.V - 3):
            for b in range(a + 1, self.V - 2):
                for c in range(b + 1, self.V - 1):
                    for d in range(c + 1, self.V):
                        F = {}
                        self.seed([a, b, c, d])
                        Q_process = [a, b, c, d]
                        while Q_process:
                            i = Q_process[-1]
                            del Q_process[-1]
                            self.localized.append(i)
                            F[i] = self.global_pos[i]
                            for j in self.adj[i]:
                                if j[0] not in self.localized:
                                    neighbors = self.localized_neighbors_3d[j[0]]
                                    neighbors.append(i)
                                    if len(neighbors) >= 4:
                                        if self.localize3d(j[0], [neighbors[0], neighbors[1], neighbors[2], neighbors[-1]]):
                                            Q_process.append(j[0])
                                if len(F) == self.V:
                                    return F
                                if len(F) > len(F_best):
                                    F_best = F
                            print(Q_process)
                        self.clear_localization()
        return F_best

    def seed(self, seeds):
        for i in range(4):
            self.global_pos[seeds[i]] = self.sensors[seeds[i]]
