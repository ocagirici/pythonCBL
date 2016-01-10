import sensor
import graph
import random
import plotter


sensors = []

for i in range(20):
    x = random.uniform(0.0, 15.0)
    y = random.uniform(0.0, 15.0)
    z = random.uniform(0.0, 15.0)
    sensors.append([x, y, z])

g = graph.WSN(sensors)
print(g.quadrilateration())
print('quad complete')





