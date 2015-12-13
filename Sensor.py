from Goulib.geom import Point3, Point2


class Sensor:

    actualPos = Point3(0, 0, 0)
    localPos = Point2(0, 0)
    globalPos = Point3(0, 0, 0)
    neighbors = {}

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
        print(self.id, ':', self.neighbors)

    def __repr__(self):
        instr = "{0}: ({1:.2f}, {2:.2f}, {3:.2f})".format(self.id, self.actualPos.x, self.actualPos.y, self.actualPos.z)
        return instr







