from Goulib.geom import Point3, Point2, Sphere
import numpy
import sympy

class Sensor:

    actualPos = Point3(0, 0, 0)
    localPos = Point2(0, 0)
    globalPos = Point3(0, 0, 0)
    neighbors = {}
    localized_neighbors = []

    def __init__(self, node, x, y, z):
        self.id = node
        self.actualPos = Point3(x, y, z)
        print('Sensor', id, 'created')

    def actual_pos(self):
        return [self.actualPos.x(), self.actualPos.y(), self.actualPos.z()]

    def actual_distance(self, other):
        return self.actualPos.distance(other.actualPos)

    def add_neighbor(self, neighbor, distance):
        self.neighbors[neighbor] = distance

    def neighbor_localized(self, neighbor):
        self.localized_neighbors.append(neighbor)

    def dist(self, neighbor):
        return self.neighbors[neighbor]

    def localize_self_3d(self):
        if len(self.localized_neighbors) <= 4:
            return False
        i = self.neighbors[self.localized_neighbors[0]].localPos
        j = self.neighbors[self.localized_neighbors[1]].localPos
        k = self.neighbors[self.localized_neighbors[2]].localPos
        l = self.neighbors[self.localized_neighbors[3]].localPos
        if self.coplanar(i, j, k, l):
            return False
        sympy.

    def coplanar(self, *points):
        i = sympy.Point3D(points[0].x, points[0].y, points[0].z)
        j = sympy.Point3D(points[1].x, points[1].y, points[1].z)
        k = sympy.Point3D(points[2].x, points[2].y, points[2].z)
        l = sympy.Point3D(points[3].x, points[3].y, points[3].z)
        return sympy.Point.is_collinear(i, j, k, l)





    def __repr__(self):
        instr = "{0}: ({1:.2f}, {2:.2f}, {3:.2f})".format(self.id, self.actualPos.x, self.actualPos.y, self.actualPos.z)
        return instr







