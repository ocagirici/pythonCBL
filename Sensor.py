import Geometry.vector as point


class Sensor:
    actualPos = []
    localPos = [0, 0]
    globalPos = []
    localized_neighbors_3d = []
    localized_neighbors_2d = []
    localized_2d = False
    localized_3d = False

    def __init__(self, node, x, y, z):
        self.id = node
        self.actualPos = point.vector([x, y, z])

    def actual_distance(self, other):
        return point.norm(self.actualPos - other.actualPos)

    def neighbor_localized_2d(self, neighbor):
        if self.localized_2d:
            return
        self.localized_neighbors_2d.append(neighbor)

    def neighbor_localized_3d(self, neighbor):
        if self.localized_3d:
            return
        self.localized_neighbors_3d.append(neighbor)

    def set_local(self, pos):
        self.localPos = pos
        self.localized_2d = True

    def set_global(self, pos):
        self.globalPos = pos
        self.localized_3d = True

    def seed(self):
        self.set_global(self.actualPos)

    def __repr__(self):
        instr = "{0}: ({1:.2f}, {2:.2f}, {3:.2f})".format(self.id,
                                                          self.actualPos[0], self.actualPos[1], self.actualPos[2])
        return instr
