import sensor
import graph
import random
import plotter


sensors = []

for i in range(10):
    x = random.uniform(0.0, 3.0)
    y = random.uniform(0.0, 3.0)
    z = random.uniform(0.0, 3.0)
    sensors.append([x, y, z])

g = graph.WSN(sensors)
print(g.quadrilateration())





