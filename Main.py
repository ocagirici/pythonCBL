import Sensor
import random

sensors = []

for i in range(1, 10):
    x = random.uniform(0.0, 10.0)
    y = random.uniform(0.0, 10.0)
    z = random.uniform(0.0, 10.0)
    sensors.append(Sensor.Sensor(i, x, y, z))


for sensor in sensors:
    print(sensor)




