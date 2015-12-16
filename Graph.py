import math
import sympy
import numpy as np
from Geometry.vector import Vector as vector

tol = 0


def quarilaterate(p, r):
    P1 = vector(p[0])
    P2 = vector(p[1])
    P3 = vector(p[2])
    ex = (P2 - P1) / abs(P2 - P1)
    i = ex * (P3 - P1)
    ey = (P3 - P1 - i * ex) / abs(P3 - P1 - i * ex)
    d = abs(P2 - P1)
    j = ey * (P3 - P1)
    x = (r[0] ** 2 - r[1] ** 2 + d ** 2)/(2 * d)
    y = (r[0] ** 2 - r[2] ** 2 - x ** 2 + (i - x) ** 2 + j ** 2) / 2 * j
    ez = ex ^ ey
    z = r[0] ** 2 - x ** 2 - y ** 2
    if z < 0:
        return False
    z1 = math.sqrt(r[0] ** 2 - x ** 2 - y ** 2)
    z2 = -z1
    p1 = P1 + x * ex + y * ey + z1 * ez
    p2 = P1 + x * ex + y * ey + z2 * ez
    return [p1, p2]


def trilaterate(p, r):
    P1 = vector(p[0])
    P2 = vector(p[1])
    ex = (P2 - P1) / abs(P2 - P1)
    d = abs(P2 - P1)
    x = (r[0] ** 2 - r[1] ** 2 + d ** 2)/(2 * d)
    y1 = math.sqrt(r[0] ** 2 - x ** 2)
    y2 = -y1
    p1 = P1 + x * ex + y1 * ex
    p2 = P1 + x * ex + y2 * ex
    return [p1, p2]

def dist(p, i, j):
    u = p[i]
    v = p[j]
    try:
        return math.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2 + (u[2] - v[2]) ** 2)
    except:
        print(p, i, j, u, v)


def coplanar(points):
    ij = dist(points, 0, 1)
    ik = dist(points, 0, 2)
    il = dist(points, 0, 3)
    jk = dist(points, 1, 2)
    jl = dist(points, 1, 3)
    kl = dist(points, 2, 3)
    M = [
        [0, 1, 1, 1, 1],
        [1, 0, ij ** 2, ik ** 2, il ** 2],
        [1, ij ** 2, 0, jk ** 2, jl ** 2],
        [1, ik ** 2, jk ** 2, 0, kl ** 2],
        [1, il **2, jl ** 2, kl ** 2, 0]
    ]

    det = np.linalg.det(M)
    V = math.sqrt(det/288)
    if V <= tol:
        return True
    return False


def collinear(points):
    ij = dist(points, 0, 1)
    ik = dist(points, 0, 2)
    jk = dist(points, 1, 2)
    M = [
        [0, 1, 1, 1],
        [1, 0, ij ** 2, ik ** 2],
        [1, ij ** 2, 0, jk ** 2],
        [1, ik ** 2, jk ** 2, 0]
    ]

    det = np.linalg.det(M)
    V = -math.sqrt(det/16)
    if V <= tol:
        return True
    return False


def dist3d(i, j):
    return math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2)


def dist2d(i, j):
    return math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2)

class WSN:
    V = 0
    E = 0
    R = 10.0
    adj = {}
    is_adj = []
    localized_neighbors_3d = {}
    localized_neighbors_2d = {}
    sensors = []
    localized = []
    unlocalized = []
    global_pos = {}
    local_pos = {}

    def clear_localization(self):
        self.localized_neighbors_3d = {}
        self.localized_neighbors_2d = {}
        for i in range(self.V):
            self.localized_neighbors_3d[i] = []
            self.localized_neighbors_2d[i] = []

    def __init__(self, sensors):
        self.sensors = sensors
        self.V = len(sensors)
        self.clear_localization()
        for i in range(self.V):
            self.adj[i] = []
        self.is_adj = [[False for i in range(self.V)] for j in range(self.V)]

        for i in range(self.V):
            self.unlocalized.append(i)
            for j in range(i + 1, self.V):
                distance = self.actual_distance(i, j)
                if distance <= self.R:
                    self.add_adj(i, j, distance)

    def add_adj(self, i, j, dist):
        self.adj[i].append(j)
        self.adj[j].append(i)
        self.is_adj[i][j] = dist
        self.is_adj[j][i] = dist

    def dist(self, u, v):
        return self.adj[u][v]

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
            try:
                r.append(self.dist(node, localized[i]))
            except:
                print(node, i, localized)
        if coplanar(p):
            return False
        sol = quarilaterate(p[:-1], r[:-1])
        if sol is False:
            return False
        if len(sol) == 0:
            return False
        if len(sol) == 1:
            self.global_pos[node] = sol[0]
        else:
            p1 = abs((vector(sol[0]) - vector(p[3])) - r[3]) <= r[3] * 0.05
            p2 = abs((vector(sol[1]) - vector(p[3])) - r[3]) <= r[3] * 0.05
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
        sol = trilaterate(p[:-1], r[:-1])
        if len(sol) == 0:
            return False
        if len(sol) == 1:
            node.set_local(sol[0])
        else:
            p1 = abs((vector(sol[0]) - vector(p[2])) - r[2]) <= r[2] * 0.05
            p2 = abs((vector(sol[1]) - vector(p[2])) - r[2]) <= r[2] * 0.05
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
                                if j not in self.localized:
                                    neighbors = self.localized_neighbors_3d[j]
                                    neighbors.append(i)
                                    if len(neighbors) >= 4:
                                        if self.localize3d(j, [neighbors[0], neighbors[1], neighbors[2], neighbors[-1]]):
                                            print(j, 'is localized')
                                            Q_process.append(j)
                                if len(F) == self.V:
                                    return F
                                if len(F) > len(F_best):
                                    F_best = F
                        self.clear_localization()
        return F_best

    def seed(self, seeds):
        print('seeds:', seeds)
        for i in range(4):
            self.global_pos[seeds[i]] = self.sensors[seeds[i]]
