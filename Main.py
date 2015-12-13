import Sensor
import graph
import random
import plotter

sensors = []

for i in range(5):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    z = random.uniform(0.0, 1.0)
    sensors.append(Sensor.Sensor(i, x, y, z))

g = graph.WSN(sensors)
plotter.plot_actual(g, False)





