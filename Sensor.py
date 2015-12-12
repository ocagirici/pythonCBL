from Goulib.geom import Point3, Point2


class Sensor:

    id = 0
    actualPos = Point3(0,0,0)
    localPos = Point2(0,0)
    globalPos = Point3(0,0,0)
    neighbors = []




    def __init__(self, id, x,y,z):
        self.id = id
        self.actualPos = Point3(x,y,z)

    def actualPos(self):
        return [self.actualPos.x(), self.actualPos.y(), self.actualPos.z()]

    def actualDistance(self, other):
        return self.actualPos.distance(other.actualPos)

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __repr__(self):
        instr = "{0}: ({1:.2f}, {2:.2f}, {3:.2f})".format(self.id, self.actualPos.x, self.actualPos.y, self.actualPos.z)
        return instr







