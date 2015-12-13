import Sensor

class Graph:
    V = 0
    E = 0
    R = 1.0
    adjList = []
    adjMatrix = [[]]

    def __init__(self, *sensors):
        self.V = len(sensors)
        for i in range(self.V):
            self.adjList.append([])

        for i in range(self.V-1):
            for j in range(i+1, self.V):
                dist = sensors[i].actualDistance(sensors[j])
                if(dist <= 1.0):
                    addEdge(i, j, dist)

    def addEdge(self, i, j, w):
        self.adjList[i]


